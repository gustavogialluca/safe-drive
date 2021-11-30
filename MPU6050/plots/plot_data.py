import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(('E:\\Gustavo\\GENERA\\Direção Segura\\MPU6050\\dados\\testes_dia_2\\13_desaceleracao_media.txt'))
print(df.head())

fig, (ax1, ax2) = plt.subplots(2)
# df.plot(y=["az"], kind="line", ax=ax1, color=['blue'])
# df.plot(y=["ax", "ay"], kind="line", ax=ax2, color=['red', 'orange'])
df.plot(y=["ax", "ay", "az"], kind="line", ax=ax1, color=['red', 'orange', "blue"])
df.plot(y=["gx", "gy", "gz"], kind="line", ax=ax2, color=['red', 'orange', 'blue'])
plt.show()