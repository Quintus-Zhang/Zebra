#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:57:56 2017

@author: Quintus
"""

import numpy as np
from FourierTransform import FourierTransform

class CM_ITM(FourierTransform):
    def __init__(self, S0, K, r, T, sigma, N, dk, alpha, is_call=True):
        super(CM_ITM, self).__init__(S0, K, r, T, sigma, N, dk, alpha, is_call)              

    def charaFuncUnderlyingPrice(self, v):
        ''' characteristic function of log price
        params
            v: radian
        returns
            phi: characteristic function value
        '''
        phi = np.exp(1j * (np.log(self.S0) \
                           + (self.r - 0.5 * self.sigma**2) * self.T) * v \
                     - 0.5 * self.sigma**2 * self.T * v**2)
        return phi
        
    def FTmodOptionPrice(self):
        ''' Fourier transformation of modified option price
        returns
            psi
        '''
        vNew = self.v - (self.alpha + 1) * 1j
        psi = np.exp(-self.r * self.T) * self.charaFuncUnderlyingPrice(vNew) \
              / (self.alpha**2 + self.alpha - self.v**2 + 1j * (2 * self.alpha + 1) * self.v)
        return psi
        
    def simpsonWeight(self):
        ''' 
        '''
        # Kronecker delta function
        kronDelta = np.zeros(self.N, dtype=np.float) 
        kronDelta[0] = 1
        # generate composite simpson weights
        weight = (3 + (-1)**(self.u + 1) - kronDelta) / 3
        return weight
        
    def price(self):
        ''' 
        
        '''
        x = np.exp(1j * self.b * self.v) * self.FTmodOptionPrice() \
            * self.dv * self.simpsonWeight()
        callPrices = np.exp(-self.alpha * self.k) / np.pi * np.fft.fft(x).real
        pos = int((np.log(self.K) + self.b) / self.dk) # N/2
        return callPrices, callPrices[pos], pos
