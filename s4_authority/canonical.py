import hashlib, json

def canonical_bytes(payload: dict) -> bytes:
    scope = payload["scope"]
    if isinstance(scope, str) or any(not isinstance(x, str) for x in scope):
        raise ValueError("scope must be a sequence of strings")
    body = {
        "version": payload["version"],
        "authority_id": payload["authority_id"],
        "action": payload["action"],
        "subject": payload["subject"],
        "scope": sorted(scope),
        "valid_from": payload["valid_from"],
        "valid_until": payload["valid_until"],
        "policy_version": payload["policy_version"],
        "transition_id": payload["transition_id"],
        "canonicalization_version": payload["canonicalization_version"],
    }
    return json.dumps(body, separators=(",", ":"), sort_keys=True).encode("utf-8")

def digest(payload: dict) -> bytes:
    return hashlib.sha256(canonical_bytes(payload)).digest()
