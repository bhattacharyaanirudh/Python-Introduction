# # import pandas as pd

# # data_wrong_format = {'ProductID': ['P001','P002','P003','P004'],
# #                      'Price': ['50.25$','45.50$','60.00#','35.75$']}

# # df_wrong_formates = pd.DataFrame(data_wrong_format)

# # wrong_format_info = df_wrong_formates.applymap(lambda x: not x.replace('.','.').replace('.','').isdigit())
# # print("Wrong data format:")
# # print(wrong_format_info)

# # import pandas as pd

# # data_wrong_format = {'ProductID': ['P001','P002','P003','P004'],
# #                      'Price': ['50.25$','45.50$','60.00#','35.75$']}

# # df_wrong_formates = pd.DataFrame(data_wrong_format)

# # df_remove_symbols = df_wrong_formates.applymap(lambda x: float(''.join(filter(str.isdigit, x))) if not x.isdigit() else x)
# # print("\nCleaning Data-Removing symbols")
# # print(df_remove_symbols)

# import pandas as pd
# import matplotlib.pyplot as plt

# data_distribution = {'Values':[11,28,33,42,52,12]}
# df_distribution = pd.DataFrame(data_distribution)

# df_distribution['Values'].plot(kind='hist',bins=5,color='orange',edgecolor='black')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title("Histogram")
# plt.show()

import scipy.constants as constants

speed_of_light = constants.c
gravity = constants.g
boltzmann = constants.k

print(f"Speed of Light: {speed_of_light} m/s")
print(f"Gravitational Acceleration: {gravity} m/s²")
print(f"Boltzmann Constant: {boltzmann} J/K")

pi = constants.pi
euler_gamma = constants.gam
golden_ratio = constants.phi

print(f"Euler Gamma: {euler_gamma}")
print(f"Golden Ratio: {golden_ratio}")
print(f"Pi: {pi}")



