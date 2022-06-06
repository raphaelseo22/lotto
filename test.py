import time

from tqdm import tqdm


for i in tqdm(range(1000), desc="1st loop"):
    for j in tqdm(range(10), leave=False, desc="2nd loop"):
        time.sleep(0.1)
        continue