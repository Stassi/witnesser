from hashlib import sha256


def hash_digest(json_string: str) -> str:
    return sha256(
        json_string.encode('utf-8')
    ).hexdigest()
