import numpy as np
import matplotlib.pyplot as plt

how_many_items = int(input("how many items in gacha? >>"))
how_much_one_gacha = int(input("how much one play? >>"))

def calc_probability(count):
    lose_proba = 1
    for c in range(count):
        lose_proba = (how_many_items-1)/(how_many_items)*lose_proba
    return 1 - lose_proba

times_list = np.linspace(1,100,100, dtype=int)
proba_list = list(map(calc_probability, times_list))
print("t ", times_list)
print("p ", proba_list)
plt.plot(times_list, proba_list)
plt.show()

