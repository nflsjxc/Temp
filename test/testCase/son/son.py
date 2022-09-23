from .. import father

def func(param):
    param+=1
    return param

class son(father):
    def __init__(self) -> None:
        super().__init__()
        param=func(self.id)
        self.id2=self.id
        print(self.id)
        print("son instance")
        print(param)