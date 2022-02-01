import pandas as pd

ind = ["A", "B", "C"]

data = ["Marwan", "Niheng", "Adam"]

list_tub = list(zip(ind, data))

df = pd.DataFrame(list_tub, columns= ["Index", "Data"])

print(df)
