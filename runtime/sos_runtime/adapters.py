from __future__ import annotations
import json, subprocess, urllib.request
from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass
class AdapterResult:
    system: str
    connected: bool
    status: str
    capabilities: list[str]
    details: Dict[str,Any]

class Adapter:
    name="UNNAMED"
    def probe(self)->AdapterResult: raise NotImplementedError

class HttpAdapter(Adapter):
    def __init__(self,name,health_url,capabilities=None):
        self.name=name; self.health_url=health_url; self.capabilities=capabilities or []
    def probe(self):
        try:
            with urllib.request.urlopen(self.health_url,timeout=5) as r:
                body=r.read().decode()
                try: details=json.loads(body)
                except json.JSONDecodeError: details={"body":body[:2000]}
                return AdapterResult(self.name,True,"ONLINE",self.capabilities,details)
        except Exception as e:
            return AdapterResult(self.name,False,"UNAVAILABLE",self.capabilities,{"error":str(e)})

class KCNAdapter(HttpAdapter):
    def __init__(self,base_url="http://127.0.0.1:8000"):
        super().__init__("KCN",base_url.rstrip("/")+"/health",
                         ["intelligence","research","verification","security","execution"])

class GenericHttpAdapter(HttpAdapter): pass

class CommandAdapter(Adapter):
    def __init__(self,name,command,capabilities=None):
        self.name=name; self.command=command; self.capabilities=capabilities or []
    def probe(self):
        try:
            p=subprocess.run(self.command,shell=True,capture_output=True,text=True,timeout=15)
            return AdapterResult(self.name,p.returncode==0,"ONLINE" if p.returncode==0 else "ERROR",
                                  self.capabilities,{"stdout":p.stdout[-4000:],"stderr":p.stderr[-4000:]})
        except Exception as e:
            return AdapterResult(self.name,False,"UNAVAILABLE",self.capabilities,{"error":str(e)})

def discover_adapters(config:Optional[Dict[str,Any]]=None):
    config=config or {}
    adapters=[KCNAdapter(config.get("kcn_url","http://127.0.0.1:8000"))]
    for item in config.get("http",[]): adapters.append(GenericHttpAdapter(item["name"],item["health_url"],item.get("capabilities",[])))
    for item in config.get("commands",[]): adapters.append(CommandAdapter(item["name"],item["command"],item.get("capabilities",[])))
    return adapters
