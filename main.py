import pandas as pd
from matplotlib import pyplot as plt
from Lotto import LottoNum


lotto = LottoNum(1018)
# num_df , num_dict = lotto.crawl()

# # num_df.to_csv("/home/raphaelseo/personal/lotto/result.csv")
# # print(num_dict)

# pred = lotto.predict(num_df, num_dict)

print(lotto.pred)