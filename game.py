import random

x = random.randint(1, 50)
print(x)
times = 15

for i in range(1, times + 1):
    y = eval(input("請猜一個數字: "))
    if x == y:
        print("猜對了！")
        break
    if i == times:
        print(f"很可惜，正確答案是{x}")
        break
    print(f"猜錯了！剩{times-i}次機會")
