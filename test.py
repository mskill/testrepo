def describe(df, col):



desc = df[col].describe()



idx = desc.index.tolist()



idx[5] = 'median'



desc.index = idx



return desc