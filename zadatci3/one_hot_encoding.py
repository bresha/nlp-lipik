import pandas as pd

text= "Marko igra nogomet u svom gradu, igra i tenis"

print(pd.get_dummies(text.split()))