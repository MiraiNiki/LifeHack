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
    
print(1-lose_proba)
