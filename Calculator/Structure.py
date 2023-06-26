from Calculator.Constants import CONSTANTS
from Calculator.Calculate import CaclDifusion

class Structure():
    def __init__(self, layers=None):
        if layers is not None:
            self.layers: str = layers
    
    def parseLayers(self, delimeter: str = ""):
        self.list_layers = self.layers.split(delimeter)
        return self.list_layers
    
    def getConstantsLayers(self):
        dict_constant = {}
        for lrs in self.list_layers:
            dict_constant[lrs] = CONSTANTS[lrs]
        return dict_constant
        
    @classmethod
    def initModel(self):
        clc = CaclDifusion()
        clc.W = 5e-5
        clc.Ea = 43421
        clc.T = 438
        clc.R = 0.00625
        clc.D0 = 5.65e-4
        clc.jn = 2.404
        return clc
        


        


