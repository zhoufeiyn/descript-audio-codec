
class ToyModel:
    def __init__(self,dim = 128,lr =0.1):
        self.dim = dim
        self.lr = lr
    def __repr__(self):
        return f"ToyModel(dim = {self.dim},lr = {self.lr})"