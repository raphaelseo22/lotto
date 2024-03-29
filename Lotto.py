from typing import Tuple
import random

import requests
import numpy as np
import pandas as pd
from scipy import rand
from tqdm import tqdm


class LottoNum:
    def __init__(self, start_drw:int) -> None:
        self.start_drw = start_drw # latest lotto round
        self.url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" # dhlottery API url
        self.num_df, self.num_dict = self.crawl()
        self.mean_num = round(sum(list(self.num_dict.values()))/len(list(self.num_dict.values())))
        self.pred = self.predict()


    def crawl(self) -> Tuple[pd.DataFrame, dict]:
        num_dict = {}
        start_drw = self.start_drw
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
        while True:
            url = self.url + "{0}".format(start_drw)
            req = requests.get(url)
            json_data = req.json()

            if json_data["returnValue"] == "fail":
                break
            
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
            
            round_num.append(start_drw)
            bonus_num.append(json_data["bnusNo"])
            start_drw += 1

        num_df = pd.DataFrame({"round":round_num, "num1":num1, "num2":num2, "num3":num3, 
                                "num4":num4, "num5":num5, "num6": num6, "bonus":bonus_num})
        
        total_num = num1 + num2 + num3 + num4 + num5 + num6 + bonus_num
        for n in total_num:
            num_dict["{0}".format(n)] = num_dict["{0}".format(n)] + 1
        
        # self.num_df = num_df
        # self.num_dict = num_dict
        return num_df, num_dict
    
    
    def predict(self) -> list:
        res = []
        nums = []
        dict_res = []
        dict_res2 = []
        #df_res = []
        number = np.array(range(45)) + 1
        prob = []
        
        for i in number:
            p = 0.022 + (0.001 * (self.mean_num - self.num_dict[f"{i}"]))
            prob.append(p)
        
        if sum(prob) < 1:
            d =  1 - sum(prob)
            number = np.append(number, 0)
            prob.append(d)
        
        for i in range(5):
            val = True
            while val:
                result_number = np.random.choice(number, 6, p=prob, replace=False)
                if not 0 in result_number:
                    val = False
            res.append(result_number)

        # for i in range(45):
        #     i = i+1
        #     num_ls = [i]
        #     num_ls = num_ls * (50+(self.mean_num - self.num_dict[f"{i}"]))
        #     nums.extend(num_ls)
        
        # for i in range(5):
        #     out = []
        #     nums2 = nums
        #     for j in range(6):
        #         choice_num = random.choice(nums2)
        #         out.append(choice_num)
        #         while choice_num in nums2:
        #             nums2.remove(choice_num)
        #     out.sort()
        #     res.append(out)
        
        # sorted_dict = sorted(self.num_dict.items(), key = lambda item: item[1])
        
        # for i in range(6):
        #     dict_res.append(int(sorted_dict[i][0]))
        #     dict_res2.append(int(sorted_dict[-(i+1)][0]))
        #     # df_res.append(round(float(self.num_df["num{0}".format(i+1)].describe()["mean"])))
        # dict_res.sort()
        # dict_res2.sort()
        # res.append(dict_res)
        # res.append(dict_res2)        
        
        return res
