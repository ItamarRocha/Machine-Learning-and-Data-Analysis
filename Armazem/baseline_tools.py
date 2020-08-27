import numpy as np

def naive_forecast(data):
    """
        Input : data to be forecasted

        Return : the naive forecast and the data sliced to the same date interval of the naive forecast
    """
    naive = data.copy().shift(1) #o naive é o do dia anterior
    naive = naive[1:] 
    return naive, data[1:] #exclui a primeira observação já que ela não tem uma anterior

def moving_average(series, window_size):
    """
        Input : series to be forecasted and the movidn window_size

        return : forecast and real data
    """
    forecast = []
    for time in range(len(series) - window_size): # if you dont subtract the window size, you'll not compute right in the last 30 examples
        forecast.append(series[time:time + window_size].mean())
    return np.array(forecast), data[window_size:]
