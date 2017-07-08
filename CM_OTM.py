#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 23:09:47 2017

@author: Quintus
"""

import numpy as np
from CM_ITM import CM_ITM

class CM_OTM(CM_ITM):
    def __init__(self, S0, K, r, T, sigma, N, dk, alpha, is_call=True):
        super(CM_OTM, self).__init__(S0, K, r, T, sigma, N, dk, alpha, is_call)              
    
    def FToptionPrice(self, v):
        zeta = np.exp(-self.r * self.T) * (1 / (1 + 1j * v) \
                                            - np.exp(-self.r * self.T) / (1j * v)
                                            - self.charaFuncUnderlyingPrice(v - 1j) / (v**2 - 1j * v))
        return zeta
        
    def FTmodOptionPrice(self):
        v1 = self.v - 1j * self.alpha
        v2 = self.v + 1j * self.alpha
        gamma = (self.FToptionPrice(v1) - self.FToptionPrice(v2)) / 2
        return gamma
    
    def price(self):
        x = np.exp(1j * self.b * self.v) * self.FTmodOptionPrice() * self.dv * self.simpsonWeight()
        callPrices = 1 / np.sinh(self.alpha * self.k) / np.pi * np.fft.fft(x).real
        pos = int((np.log(self.K) + self.b) / self.dk)
        return callPrices, callPrices[pos], pos