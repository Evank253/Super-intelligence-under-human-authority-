"""Verify-only S4 channel. This package cannot originate a sovereign act."""
from .authorization import AuthorizationPayload
from .verifier import AuthorizationVerdict, verify_authorization
