import random

# 隨機產生 1~100 的數字
answer = random.randint(1, 100)

print("🎯 歡迎來玩猜數字！")
print("請猜一個 1 到 100 的數字")

count = 0

while True:
    guess = int(input("請輸入數字："))
    count += 1

    if guess < answer:
        print("太小了！")
    elif guess > answer:
        print("太大了！")
    else:
        print(f"恭喜猜對！答案是 {answer}")
        print(f"你總共猜了 {count} 次")
        break