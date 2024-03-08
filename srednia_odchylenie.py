import numpy as np

##Zdefiniowanie średniej ucinanej
def trim_mean(data, k):
    size = len(data)
    new_data = data[k:size - k]
    new_size = len(new_data)
    return sum(new_data) / new_size

##Zdefiniowawnie średniej winsorowskiej
def winsorized_mean(data, k):
    size = len(data)
    new_data = data[k:size - k]
    low = min(new_data)
    high = max(new_data)

    return (sum(new_data) + k * (low + high)) / size

##Zdefiniowanie odchylenia przeciętnego od wartości średniej
def mad(data):
    return np.mean(abs(data - np.mean(data)))