import numpy as np

def ema (self, array, period ):

    ema = np.zeros_like(array) 
    ema[0] = np.mean(array[0] , dtype=np.float32)
    alpha = 2 / (period + 1)

    for i in range(1 , len(array) ):
          ema[i] = np.array( (array[i] * alpha +  ema[i-1]  * (1-alpha) ) , dtype=np.float32 )
    
    return ema 

def gmma(close, **kwargs):

    gmma = np.empty((len(close), len(kwargs.keys()) ))
    for i, (key, value) in enumerate(kwargs.items()):
        gmma[: , i] = ema( close , value )

    return gmma  
  
  
""" Example
gmma(close , ema1=3 ,ema2=5 ,ema3=8 ,ema4=10 ,ema5=12 ,ema6=15 ,ema7=30 ,ema8=35 ,ema9=40 ,ema10=45 ,ema11=50 ,ema12=60 )

"""
