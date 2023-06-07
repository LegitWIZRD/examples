from UtilPackage import *
def Hasher(HashingFunc: callable, s: str) -> str:
    s = s.encode()
    try:
        return HashingFunc(s).hexdigest()
    except Exception:
        return HASHING["Doc"]
    