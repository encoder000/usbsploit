from .keycode import Keycode

def get(symb:str):
    if symb.isdigit():
        # 1,2,3...9,0 -> 0,1,2,3...8,9 -> 39,30,31...37,38
        return 30+(9+int(symb))%10

    return vars(Keycode)[symb.upper()]
