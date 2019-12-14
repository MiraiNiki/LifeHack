import random
import numpy as np
total_money = input('how many 100 yen >>')
total_gacha = 0
if(total_money.isnumeric()):
    total_money = int(total_money)
    total_gacha = int(total_money/2)
else:
    total_gacha = int(input('how many times >>'))

lose_proba = 1
for gacha in range(total_gacha):
    lose_proba = 4/5*lose_proba
calced_proba = 1-lose_proba
print("calced proba ", 1-lose_proba)

exp_num_list = [1,10,100,1000,10000,100000]
proba_list = []
item_num = 5

for exp_num in exp_num_list:
    win_count = 0
    for exp_id in range(exp_num):
        for gacha in range(total_gacha):
            result = random.randrange(item_num)
            if result == 1:
                win_count = win_count + 1
                break
    proba_list.append(win_count/exp_num)
    
for i in range(len(proba_list)):
    print(exp_num_list[i], proba_list[i], np.abs(proba_list[i]-calced_proba))

