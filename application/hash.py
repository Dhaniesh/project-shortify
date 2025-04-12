import hashlib


def get_hash(long_url):
    hash_object = hashlib.sha256(long_url.encode())
    short_code = hash_object.hexdigest()[:8]
    return short_code
