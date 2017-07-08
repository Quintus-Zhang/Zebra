#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:26:08 2017

@author: Quintus
"""

import numpy as np
from CM_OTM import CM_OTM

class CM_OTM_M76(CM_OTM):
    def __init__(self, S0, K, r, T, sigma, N, dk, alpha, lamb, m, d, is_call=True):
        super(CM_OTM_M76, self).__init__(S0, K, r, T, sigma, N, dk, alpha, is_call)              
        ''' 
        params
            lamb: jump intensity
            m: expected jump size
            d: standard deviation of jump size
        '''
        self.lamb = lamb
        self.m = m
        self.d = d

    def charaFuncUnderlyingPrice(self, v):
        ''' characteristic function of log price with jump
        params
            v: radian
        returns
            phi: characteristic function value
        '''
        mu = self.r - 0.5 * self.sigma**2 - self.lamb * (np.exp(self.m + 0.5 * self.d**2) - 1)
        phi = np.exp(1j * (np.log(self.S0) + self.T * mu) * v - 0.5 * self.sigma**2 * v**2 * self.T
                     + self.lamb * self.T * (np.exp(1j * self.m * v - 0.5 * self.d**2 * v**2) - 1))
        return phi