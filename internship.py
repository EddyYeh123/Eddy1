import random
target = random.randint(1,100)
total = 5
count = 0

while True:
    n = int(input("请猜一个1—100的整数： "))
    if   n > target:
        print('你猜大了！')
    elif n < target:
        print('你猜小了！')
    elif n == target:
        print('恭喜你，猜对了！')
        break

    count += 1
    if count >= total:
        print('您的5次机会已经用完，请再次尝试吧！')
        break

print("Haha!")