import pandas as pd
from Lotto import LottoNum


lotto = LottoNum(1)
num_df , num_dict = lotto.crawl()
# 
# num_df.to_csv("/Users/raphaelseo/projects/lotto/result.csv")
# print(num_dict)

# print(sum(list(num_dict.values()))/len(list(num_dict.values())))

# pred = lotto.predict(num_df, num_dict)

print(lotto.pred)