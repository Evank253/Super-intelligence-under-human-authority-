"""Minimal SHA-256 content-addressed historical evidence archive for EA-G2."""
from __future__ import annotations
import hashlib, os
from pathlib import Path
class IntegrityError(Exception): pass
class ArchiveWriteError(Exception): pass
def _digest(content: bytes)->str: return hashlib.sha256(content).hexdigest()
class ContentAddressedArchive:
    def __init__(self, root: Path|str):
        self._root=Path(root); self._root.mkdir(parents=True,exist_ok=True)
    def put(self, content: bytes)->str:
        if not isinstance(content,bytes): raise TypeError("content must be bytes")
        digest=_digest(content); path=self._path_for(digest); path.parent.mkdir(parents=True,exist_ok=True)
        if path.exists():
            if self._verified_read(digest)!=content: raise IntegrityError("existing CAS object failed verification")
            return digest
        tmp=path.with_name(path.name+".tmp")
        try:
            with open(tmp,"xb") as f:
                f.write(content); f.flush(); os.fsync(f.fileno())
            os.replace(tmp,path)
        except FileExistsError:
            if self._verified_read(digest)!=content: raise IntegrityError("existing CAS object failed verification")
        finally:
            try: tmp.unlink()
            except FileNotFoundError: pass
        return digest
    def get(self,digest:str)->bytes: return self._verified_read(digest)
    def has(self,digest:str)->bool:
        try: self._verified_read(digest); return True
        except (FileNotFoundError,IntegrityError): return False
    def _verified_read(self,digest:str)->bytes:
        path=self._path_for(digest); data=path.read_bytes()
        if _digest(data)!=digest: raise IntegrityError("CAS hash mismatch")
        return data
    def _path_for(self,digest:str)->Path:
        if not isinstance(digest,str) or len(digest)!=64: raise ValueError("digest must be a 64-character SHA-256 hex digest")
        try: int(digest,16)
        except ValueError as exc: raise ValueError("digest must be hexadecimal") from exc
        return self._root/digest[:2]/digest
