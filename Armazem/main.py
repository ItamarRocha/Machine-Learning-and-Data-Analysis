import pandas as pd
from Preprocessor import preProcessing

vendas = preProcessing('13')
vendasM = vendas.resample('M').sum()