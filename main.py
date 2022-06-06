import pandas as pd
from matplotlib import pyplot as plt
from Lotto import LottoNum


lotto = LottoNum(1018)
num_df , num_dict = lotto.crawl()

num_df.to_csv("/home/raphael/project/lotto/result.csv")
print(num_dict)