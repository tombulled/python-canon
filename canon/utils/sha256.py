import hashlib

def sha256(data):
    """
    Returns: hashlib.sha256(data.encode()).hexdigest()
    """

    return hashlib.sha256(data.encode()).hexdigest()
