#사탕 뽑기 기계 만들기

import random

random.randint(1,10)

Candy = [
    "딸기맛",
    "누룽지맛",
    "박하맛",
    "매실맛",
    "사과맛",
    "포도맛",
    "꽝"
]
item = input("사탕을 뽑아주세요.")

idx = random.randint(0, len(Candy)-1)
# print(Candy[idx])
# ri = Candy.index(item)

print(Candy[idx])

Candy.remove(Candy[idx])

idx = 1
print(str(idx) + ' : ' + Candy[idx])

idx = idx + 1
print(str(idx) + ' : ' + Candy[idx])

idx = idx + 1
print(str(idx) + ' : ' + Candy[idx])

idx = idx + 1
print(str(idx) + ' : ' + Candy[idx])

idx = idx + 1
print(str(idx) + ' : ' + Candy[idx])

idx = idx 
print(str(idx) + ' : ' + Candy[idx])
