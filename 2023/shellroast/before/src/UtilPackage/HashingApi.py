def Hasher(HashingFunc: callable, s: str) -> str:
    s = s.encode()
    try:
        return HashingFunc(s).hexdigest()
    except Exception as e:
        return f"Error: {str(e).capitalize()}"
    