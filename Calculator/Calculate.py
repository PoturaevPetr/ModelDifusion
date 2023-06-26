import numpy as np
import math
from scipy.special import j1



class CaclDifusion():
    def __init__(self):

        self.R = None
        self.W = None
        self.Rt = 8.314
        self.Ea = None
        self.D0 = None
        self.T = None
        self.jn = None
    
    def searchKD(self, mode:str = ""):
        if mode == "":
            self.D = self.D0 * math.exp(-self.Ea / (self.Rt * self.T))
            return self.D

    
    def searchTime(self, time):
        self.time_n = time + pow(self.W, 2)/(8 * self.D)
        return self.time_n
    

    def searchSorb(self):
        """Пока по Фику"""
        return 1 - (2 * math.exp(-(pow(self.jn, 2) * self.D * self.time_n) / pow(self.R, 2))) / (self.jn * j1(self.jn))

    def searchDesorb(self):
        return (2 * math.exp(-(pow(self.jn, 2) * self.D * self.time_n) / pow(self.R, 2))) / (self.jn * j1(self.jn))