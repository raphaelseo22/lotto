from typing import Tuple
import requests
import pandas as pd
from tqdm import tqdm


class LottoNum:
    def __init__(self, max_round:int) -> None:
        self.max_round = max_round # latest lotto round
        self.url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" # dhlottery API url

    def crawl(self) -> Tuple[pd.DataFrame, dict]:
        num_dict = {}

        for i in range(45):
            num_dict["{}".format(i+1)] = 0
        
        round_num = []
        num1 = []
        num2 = []
        num3 = []
        num4 = []
        num5 = []
        num6 = []
        bonus_num = []
 
        for r in tqdm(range(self.max_round)):
            url = self.url + "{0}".format(r+1)
            round_num.append(r+1)
            req = requests.get(url)
            json_data = req.json()
            
            for i in range(6):
                n = i+1
                if n == 1:
                    num1.append(json_data["drwtNo1"])
                elif n == 2:
                    num2.append(json_data["drwtNo2"])
                elif n == 3:
                    num3.append(json_data["drwtNo3"])
                elif n == 4:
                    num4.append(json_data["drwtNo4"])
                elif n == 5:
                    num5.append(json_data["drwtNo5"])
                elif n == 6:
                    num6.append(json_data["drwtNo6"])
                else:
                    continue
            bonus_num.append(json_data["bnusNo"])

        num_df = pd.DataFrame({"num1":num1, "num2":num2, "num3":num3, 
                                "num4":num4, "num5":num5, "num6": num6, "bonus":bonus_num},
                                index=round_num)
        
        total_num = num1 + num2 + num3 + num4 + num5 + num6 + bonus_num
        for n in total_num:
            num_dict["{0}".format(n)] = num_dict["{0}".format(n)] + 1

        return num_df, num_dict