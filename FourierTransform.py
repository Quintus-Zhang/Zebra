#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:00:39 2017

@author: Quintus
"""

import numpy as np
from OptionsPricing import OptionsPricing

class FourierTransform(OptionsPricing):
    """ Shared attributes and functions of FourierTransformPricing """

    def __init__(self, S0, K, r, T, sigma, N, dk, alpha, is_call=True):
        super(FourierTransform, self).__init__(S0, K, r, T, sigma, is_call)
        self.N = N
        self.dk = dk # sampling interval size in the log strike space
        self.alpha = alpha
        
        self.dv = 2 * np.pi / (N * dk) # sampling interval size in the angular frequency domain
        self.b = N * dk / 2 - np.log(self.K) # sampling half-range in the log strike space, 
                                             # [-b, b] is symmetrical with respect to log(K)
        self.u = np.arange(0, N) # counter of the sampling instants
        self.k = -self.b + self.u * dk
        self.v = self.u * self.dv
              
    def charaFuncLogPrice(self, v):
        pass
    
    def FTmodOptionPrice(self):
        pass
    
    def simpsonWeight(self):
        pass
    
    def price(self):
        pass