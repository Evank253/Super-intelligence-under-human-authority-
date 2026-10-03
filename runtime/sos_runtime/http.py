import json, os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from .runtime import SoSRuntime

runtime=SoSRuntime(os.environ.get("SOS_DATA_DIR","runtime-data"))

class Handler(BaseHTTPRequestHandler):
    def _json(self,status,payload):
        raw=json.dumps(payload,indent=2).encode()
        self.send_response(status)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        if self.path=="/health":
            return self._json(200,runtime.health())
        if self.path=="/api/index":
            return self._json(200,{"artifacts":[a.__dict__ for a in runtime.index.artifacts.values()]})
        return self._json(404,{"error":"not found"})

    def do_POST(self):
        try:
            n=int(self.headers.get("Content-Length","0"))
            body=json.loads(self.rfile.read(n) or b"{}")
            if self.path=="/api/discover":
                return self._json(201,runtime.index.register(**body).__dict__)
            if self.path=="/api/evidence":
                return self._json(201,runtime.evidence.observe(**body).__dict__)
            if self.path=="/api/reindex":
                return self._json(201,runtime.index.reindex(body["artifact_id"],body["changes"]).__dict__)
            if self.path=="/api/execute":
                return self._json(200,runtime.execute(**body))
            return self._json(404,{"error":"not found"})
        except PermissionError as e:
            return self._json(403,{"error":str(e)})
        except Exception as e:
            return self._json(400,{"error":type(e).__name__,"message":str(e)})

def main():
    ThreadingHTTPServer(("0.0.0.0",int(os.environ.get("SOS_PORT","8080"))),Handler).serve_forever()

if __name__=="__main__":
    main()
