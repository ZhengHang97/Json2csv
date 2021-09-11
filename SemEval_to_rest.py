import pandas as pd
from sklearn.utils import shuffle

data = pd.read_csv('SemEval14_rest.csv')
data = pd.DataFrame(data, columns=['text', 'aspectTerms'])

# data = pd.DataFrame(data, columns=['text', 'ac1', 'acp1', 'ac2', 'acp2', 'ac3', 'acp3', 'ac4', 'acp4', 'ac5', 'acp5'])
# df1 = data[data['ac1'].isin(['ambience'])]
# df1 = df1.rename(columns={'ac1': 'AC', 'acp1': 'ACP'})
# df2 = data[data['ac2'].isin(['ambience'])]
# df2 = pd.DataFrame(df2, columns=['text', 'ac2', 'acp2'])
# df2 = df2.rename(columns={'ac2': 'AC', 'acp2': 'ACP'})
# df3 = data[data['ac3'].isin(['ambience'])]
# df3 = pd.DataFrame(df3, columns=['text', 'ac3', 'acp3'])
# df3 = df3.rename(columns={'ac3': 'AC', 'acp3': 'ACP'})
# df4 = data[data['ac4'].isin(['ambience'])]
# df4 = pd.DataFrame(df4, columns=['text', 'ac4', 'acp4'])
# df4 = df4.rename(columns={'ac4': 'AC', 'acp4': 'ACP'})
# df5 = data[data['ac5'].isin(['ambience'])]
# df5 = pd.DataFrame(df5, columns=['text', 'ac5', 'acp5'])
# df5 = df5.rename(columns={'ac5': 'AC', 'acp5': 'ACP'})
# data = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
# print(data.ACP.value_counts())

#  删除conflict数据来做3分类
data_pos = data[data['ACP'].isin(['positive'])]
data_neg = data[data['ACP'].isin(['negative'])]
data_neu = data[data['ACP'].isin(['neutral'])]
data_con = data[data['ACP'].isin(['conflict'])]
data = shuffle(pd.concat([data_pos, data_neg, data_neu, data_con], ignore_index=True))
print(data.ACP.value_counts())

# pos对应3，neu对应2，neg对应1
data.loc[data.ACP == 'positive', 'label'] = 3
data.loc[data.ACP == 'neutral', 'label'] = 2
data.loc[data.ACP == 'negative', 'label'] = 1
data.to_csv('SemEval14_ambience_with_conflict.csv', index=False)
