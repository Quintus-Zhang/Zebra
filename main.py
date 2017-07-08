#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:14:51 2017

@author: Quintus
"""
from FourierTransform import FourierTransform
from CM_ITM import CM_ITM
from CM_OTM import CM_OTM
from CM_ITM_M76 import CM_ITM_M76
from CM_OTM_M76 import CM_OTM_M76
from matplotlib import pyplot as plt
import numpy as np

S0 = 100.0
K = 100.0
r = 0.05
T = 1.0
sigma = 0.4
N = 4096 * 2
dk = (2 * 150)**(-1)
alpha = 1.5

lamb = 1.0
m = -0.2
d = 0.1

is_call = True

FT = CM_ITM_M76(S0, K, r, T, sigma, N, dk, alpha, lamb, m, d, is_call)
p = FT.price()

#FT = CM_ITM(S0, K, r, T, sigma, N, dk, alpha, is_call)
#p = FT.price()