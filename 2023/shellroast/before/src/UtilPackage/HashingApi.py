def Hasher(HashingFunc: callable, s: str) -> str:
    s = s.encode()
    return HashingFunc(s).hexdigest()
