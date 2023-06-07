ENCODE, DECODE = 0, 1


def EncodingManager(Func: callable, Op=ENCODE | DECODE) -> str:
    if Op == ENCODE:

        def Func_(s: str):
            s = s.encode()
            return Func(s).decode()

    elif Op == DECODE:

        def Func_(s: str):
            return Func(s).decode()

    return Func_
