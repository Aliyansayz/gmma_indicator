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

def ema(price, period):

        price = np.array(price)
        alpha = 2 / (period + 1.0)
        alpha_reverse = 1 - alpha
        data_length = len(price)

        power_factors = alpha_reverse ** (np.arange(data_length + 1))
        initial_offset = price[0] * power_factors[1:]

        scale_factors = 1 / power_factors[:-1]

        weight_factor = alpha * alpha_reverse ** (data_length - 1)

        weighted_price_data = price * weight_factor * scale_factors
        cumulative_sums = weighted_price_data.cumsum()
        ema_values = initial_offset + cumulative_sums * scale_factors[::-1]

        return ema_values


