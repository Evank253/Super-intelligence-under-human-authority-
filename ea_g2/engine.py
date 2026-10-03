"""EA-G2 evolutionary state with external historical archive ownership."""
from __future__ import annotations
import hashlib
from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping
from evidence_archive import ContentAddressedArchive, HistoricalEvidenceReference, PrimaryIdentity, IntegrityError
from .models import ChallengeRecord, EvolutionRecord, HumanRatificationRecord, Provenance
class AuthorityBoundaryError(PermissionError): pass
class HistoricalReferenceError(ValueError): pass
class ProvenanceError(ValueError): pass
class RuntimeIntegrityError(RuntimeError): pass
@dataclass(frozen=True,slots=True)
class ArchiveReader:
    _archive: ContentAddressedArchive
    def get(self,digest): return self._archive.get(digest)
    def has(self,digest): return self._archive.has(digest)
    def put(self,*args,**kwargs): raise AuthorityBoundaryError("evolutionary runtime has no archive write capability")
class EvolutionaryState:
    __slots__=("__archive_reader","__challenges","__evolutions","__ratifications","__initialized")
    AUTHORITY_BOUNDARY="EXTERNAL_HUMAN"
    def __init__(self,archive):
        if not isinstance(archive,ContentAddressedArchive): raise TypeError("archive must be ContentAddressedArchive")
        object.__setattr__(self,"_EvolutionaryState__archive_reader",ArchiveReader(archive))
        object.__setattr__(self,"_EvolutionaryState__challenges",{})
        object.__setattr__(self,"_EvolutionaryState__evolutions",{})
        object.__setattr__(self,"_EvolutionaryState__ratifications",{})
        object.__setattr__(self,"_EvolutionaryState__initialized",True)
    @property
    def authority_boundary(self): return type(self).AUTHORITY_BOUNDARY
    @property
    def archive(self): return self.__archive_reader
    @property
    def challenges(self)->Mapping[str,ChallengeRecord]: return MappingProxyType(dict(self.__challenges))
    @property
    def evolutions(self)->Mapping[str,EvolutionRecord]: return MappingProxyType(dict(self.__evolutions))
    @property
    def ratifications(self)->Mapping[str,HumanRatificationRecord]: return MappingProxyType(dict(self.__ratifications))
    @staticmethod
    def _check_provenance(p):
        if not isinstance(p,Provenance): raise ProvenanceError("valid Provenance is required")
    def add_challenge(self,record):
        self._check_provenance(record.provenance)
        if record.challenge_id in self.__challenges: raise ValueError("duplicate challenge_id")
        self.__challenges={**self.__challenges,record.challenge_id:record}
    def add_evolution(self,record):
        self._check_provenance(record.provenance)
        if record.evolution_id in self.__evolutions: raise ValueError("duplicate evolution_id")
        ref=HistoricalEvidenceReference(record.historical_record_id,PrimaryIdentity("sha256-raw",record.historical_hash,"SHA-256","raw-bytes","primary"),provenance=record.provenance)
        if not self.__archive_reader.has(ref.content_hash): raise HistoricalReferenceError("historical reference is absent or fails primary verification")
        self.__evolutions={**self.__evolutions,record.evolution_id:record}
    def add_ratification(self,record):
        self._check_provenance(record.provenance)
        if record.ratification_id in self.__ratifications: raise ValueError("duplicate ratification_id")
        self.__ratifications={**self.__ratifications,record.ratification_id:record}
    def retrieve_verified(self,reference):
        if not isinstance(reference,HistoricalEvidenceReference): raise HistoricalReferenceError("typed historical reference required")
        try: data=self.__archive_reader.get(reference.content_hash)
        except (FileNotFoundError,IntegrityError) as exc: raise HistoricalReferenceError("primary verification failed") from exc
        if hashlib.sha256(data).hexdigest()!=reference.primary_identity.content_identifier: raise HistoricalReferenceError("primary verification failed")
        return data
    def authorize_from_challenge(self,*args,**kwargs): raise AuthorityBoundaryError("challenge cannot create authority")
    def authorize_from_evidence(self,*args,**kwargs): raise AuthorityBoundaryError("evidence cannot create authority")
    def authorize_from_qualification(self,*args,**kwargs): raise AuthorityBoundaryError("qualification cannot create authority")
    def upgrade_from_consensus(self,*args,**kwargs): raise AuthorityBoundaryError("consensus cannot create truth or authority")
    def modify_historical(self,*args,**kwargs): raise AuthorityBoundaryError("evolutionary runtime has no historical write capability")
    def modify_architecture_from_inside(self,*args,**kwargs): raise AuthorityBoundaryError("internal state cannot acquire authority")
    def verify(self): return {"historical_state_owned":False,"authority_boundary":self.authority_boundary,"primary_verification_required":True,"archive_write_capability":False}
    def __setattr__(self,name,value):
        if getattr(self,"_EvolutionaryState__initialized",False): raise AttributeError("EA-G2 runtime state is not directly reassignable")
        object.__setattr__(self,name,value)
