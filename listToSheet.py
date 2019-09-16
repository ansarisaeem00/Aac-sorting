import pandas as pd
merge = [1,2,3,4]
insert = [5,6]
blank = [""]
insert = insert + blank*2
heap = [5,6,7,8]
df = pd.DataFrame.from_dict({'merge':merge , 'insert':insert})
merge2 = [3,4,5,5]
df.to_excel('test.xlsx', header=True, index=False)
