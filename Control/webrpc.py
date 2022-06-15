import json as js
def rjs(code:int,mess:str):
    return js.dumps({"code":code,"mess":mess})