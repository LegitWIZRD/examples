ENCODE, DECODE = 0, 1

def EncodingManager(Func: callable, Op=ENCODE | DECODE) -> str:
    if Op == ENCODE:

        def Func_(s: str):
            try:
                s = s.encode()
                return Func(s).decode()
            except Exception as e:
                return f"Error: {str(e).capitalize()}."

    elif Op == DECODE:

        def Func_(s: str):
            try:
                return Func(s).decode()
            except Exception as e:
                return f"Error: {str(e).capitalize()}."

    return Func_
