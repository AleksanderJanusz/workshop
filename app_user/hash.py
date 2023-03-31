import hashlib


def hash_password(password):
    t_sha = hashlib.sha256()
    t_sha.update(password.encode('utf-8'))
    return t_sha.hexdigest()
