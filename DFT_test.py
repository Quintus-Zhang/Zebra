#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 21:47:02 2017

@author: Quintus
"""

import numpy as np
from numpy import exp
from matplotlib import pyplot as plt
#==============================================================================
#  call DFT pricing
#==============================================================================

# parameters setup
S0 = 50
r = 0.05
q = 0.02
T = 0.25
sigma = 0.2

alpha = 1
N = 4096 
dk = 0.005
dw = 2*np.pi/(N*dk)


k = -N*dk/2 + np.arange(0, N+1)*dk
w = -N*dw/2 + np.arange(0, N+1)*dw



def PSI(w, S0, r, q, T, sigma):
    psiValue = exp(-r*T) * CF(w-(alpha+1)*1j, S0, r, q, T, sigma) / (alpha**2 + alpha - w**2 + (2*alpha+1)*1j*w)
    return psiValue


def CF(w, S0, r, q, T, sigma):
    '''
    characteristic function of log price
    '''
    cfValue = exp((np.log(S0) + (r-q-sigma**2/2)*T) * 1j * w - 0.5*sigma**2*T*w**2) 
    return cfValue
    

weight = np.ones(N+1)
weight[0], weight[-1] = 0.5, 0.5

test = weight * exp(1j*np.pi*np.arange(0, N+1)) * PSI(w, S0, r, q, T, sigma)


sumTest = np.sum(test * exp(-1j * 2*np.pi * np.arange(0, N+1) * np.arange(0, N+1) / N))

callPrice = np.zeros(N+1)
for n in range(0, N+1):
    callPrice[n] = exp(-alpha*k[n] + 1j * np.pi * n - 1j*np.pi*N/2) / dk * (1/N) \
                    * np.sum(test * exp(-1j * 2*np.pi * np.arange(0, N+1) * n / N))
                
plt.plot(exp(k)[:2900], callPrice[:2900])

#==============================================================================
# FFT 
#==============================================================================
callPrice = exp(-alpha*k) / (2*np.pi) * (np.fft.fft(exp(1j * N*dk/2 * w) * weight * PSI(w, S0, r, q, T, sigma) * dw)).real
    