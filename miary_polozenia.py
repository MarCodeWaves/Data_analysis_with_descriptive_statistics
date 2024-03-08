import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
import pandas as pd
from srednia_odchylenie import mad

##Funkcja zwracająca wyniki wszystkich ważniejszych miar rozproszenia itp
def calculate_data(data_1):
    data_1 = sorted(data_1['citric acid'])

    print('Średnia arytmetyczna \n1:', np.mean(data_1))
    print('\nŚrednia harmoniczna \n1:', stats.hmean(data_1))
    print('\nŚrednia geometryczna \n1:', stats.gmean(data_1))

    print('\nMediana \n1:', np.median(data_1))
    print('\nQ1 \n1:', np.quantile(data_1, 0.25))
    print('\nQ3 \n1:', np.quantile(data_1, 0.75))
    print('\nIQR \n1:', stats.iqr(data_1, interpolation="midpoint"))

    print('\nWariancja \n1:', np.var(data_1))
    print('\nOdchylenie standardowe \n1:', np.std(data_1))
    print('\nOdchylenie przeciętne od wartości średniej \n1:', mad(data_1))

    print('\nWspółczynnik zmienności \n1:', stats.variation(data_1))
    print('\nWspółczynnik skośności \n1:', stats.skew(data_1))
    print('\nKurtoza \n1:', stats.kurtosis(data_1, fisher=False))

data_1 = pd.read_csv('WineQT.csv')

calculate_data(data_1)
