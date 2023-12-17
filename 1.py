import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

pd.get_dummies(data["whoAmI"])

val = list(data['whoAmI'].values)

for i in range(len(val)):
    if val[i] == "robot":
        val[i] = 1
    else: val[i] = 0

def reverse(c):
    if c == 0:
        c = 1
    else:
        c = 0
    return c

x = pd.DataFrame({"robot": val, "human": [reverse(i) for i in val]})
print(x)