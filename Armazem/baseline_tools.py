import numpy as np
import matplotlib.pyplot as plt

class LinearRegressor:
    def execute(self, X, y):
        X = np.array(X)
        y = np.array(y)
        XTX = np.dot(X.transpose(), X)
        inverse = np.linalg.inv(XTX)
        self.W = np.dot(np.dot(inverse, X.transpose()), y)
    
    def predict(self, X):
        return [np.dot(self.W, d) for d in X]

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

def plot_series(time, series, format = "-", start = 0, end = None, label = None):
    plt.plot(time[start:end], series[start:end], format, label = label)
    plt.xlabel("Time")
    plt.ylabel("Value")
    if label:
        plt.legend(fontsize = 14)
    plt.grid(True)

def reverse_cumsum(series, initial = 0):
	"""
		Input: 
			series : series with accumulated sum
			initial : initial value to be subtracted

		Return:
			series subtracted
	"""
    series = series - series.shift(1).replace(np.nan, 0)
    series[0] -= initial
    return series