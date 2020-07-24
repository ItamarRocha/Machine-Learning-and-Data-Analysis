from datetime import datetime, timedelta
import pandas as pd
import numpy as np

'''
    Precisamos ter consiciência desde quando se começa os registros de um
    determinado produto e se ele parou de ser registrado por sair de circulação.
    
    Os unicos produtos que são realmente relevantes para serem previstos são
    aqueles que atualmente tem um bom numero de registros de vendas e estão sendo
    hoje vendidos.
'''
#fonte: Analyser.py
def preProcessing(loja : str):   
    vendas = pd.read_csv(loja + ".csv", parse_dates=['Unnamed: 0'])
    vendas = vendas.rename(columns={"Unnamed: 0": "Data"})
    vendas.set_index(['Data'], inplace = True)
    #vendas.index = pd.to_datetime(vendas.index)    
    '''
        Primeiro, precisamos pegar os produtos que hoje tem uma boa variação de vendas
            Solução: Pegar produtos que em 2019 tenha menos de 60% dos seus registros igual a 0
    '''
    dataVendas = '2019-01-02'
    #dataVendas = '02/01/2019'
    #dataVendas = datetime.strptime(dataVendas , '%d/%m/%Y')
    #print("Porcentagem dos registros de 0 vendas que desde o inicio de 2019:\n", vendas[dataVendas:].fillna(0).isin([0]).mean())
    vendas = vendas.loc[:, vendas[dataVendas:].fillna(0).isin([0]).mean() < .6]
    
    ''' 
        Segundo, nos precisamos ver se eles tem um bom numero de registros validos 
        desde o começo do histórico
            Solução: Pegar produtos cuja porcentagem de valores nans seja menor que
                    60% dos registros colhidos
    '''
    #print("Porcentagem da falta de registros de produtos com vendas relevantes para a loja:\n", vendas.isnull().mean())
    vendas = vendas.loc[:, vendas.isnull().mean() < .6]
    vendas = vendas.fillna(0).astype(np.float32)
    return vendas


    