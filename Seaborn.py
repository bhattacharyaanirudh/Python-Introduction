# # import numpy as np
# # import matplotlib.pyplot as plt

# # n,p,size = 10,0.5,1000
# # data = np.random.binomial(n,p)
# # count,bins,ignored = plt.hist(data,bins=11,density=True)
# # plt.show()


# import numpy as np
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.normal(loc= 50,scale = 5,size = 1000),hist=False,label="normal")
# plt.show()

# from numpy import random
# import numpy as np
# import matplotlib.pyplot as plt

# # Generate 100 random numbers from a uniform distribution between 0 and 1
# x = np.random.uniform(size=100)

# # Plot a histogram of the data
# plt.hist(x, bins=10, edgecolor='black')

# # Show the plot
# plt.show()

# from numpy import random

# x = random.logistic(loc=1,scale=2,size=(2,3))
# print(x)

# import numpy as np
# import matplotlib.pyplot as plt

# degree_of_freedom = 3
# data = np.random.chisquare(degree_of_freedom, size=1000)
# plt.hist(data, bins=50, density=True,alpha=0.5,color='blue',edgecolor='black')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# shape_parameter = 2.5
# data = np.random.pareto(shape_parameter,size=1000)
# plt.hist(data,bins=50,density=True,alpha=0.7,color='blue',edgecolor='black')
# plt.show()

# import numpy as np


# def myadd(a, b):
#     return a + b


# myadd = np.frompyfunc(myadd, 2, 1)
# print(myadd([1, 2, 3, 4, 5], [6, 7, 8, 9]))

# import pandas as pd

# a = [7,5,9]
# myvar = pd.Series(a)
# print(myvar)

# import pandas as pd

# data_dict = {'Name':['Alice','Bob','Charlie'],
#              'Age':[21,22,33],
#              'City':['London','Paris','Berlin']}

# df = pd.DataFrame(data_dict)
# print("Create a new DataFrame : ")
# print(df)

# import pandas as pd

# file_path = 'data.csv'
# df = pd.read_csv(file_path)
# print("DataFrame from csv: ")
# print(df)

# import pandas as pd


# file_path = 'team.json'
# pd = pd.read_json(file_path)
# print(pd)

import pandas as pd

data = {"Duration":{
                    "0":60,
                    "1":59,
                    "2":60,
                    "3":45},
        "Pulse":{
                    "0":110,
                    "1":119,
                    "2":103,
                    "3":109},
        "Maxpulse":{
                    "0":130,
                    "1":145,
                    "2":135,
                    "3":175},
        "Calories":{
                    "0":409,
                    "1":479,
                    "2":340,
                    "3":282
            }
        }

df = pd.DataFrame(data)
print(df)

import pandas as pd

data_with_empty_cells = {'Name':['alice','bob','carol',None,'david','eve'],
                         'Age':[18,20,21,None,31,28],
                         'Salary':[50000,35000,None,30000,40000,67000]}
df_with_empty_cells = pd.DataFrame(data_with_empty_cells)
cleaned_df_rows = df_with_empty_cells.dropna()
print("\nRemoving row with empty cells")
print(cleaned_df_rows)

