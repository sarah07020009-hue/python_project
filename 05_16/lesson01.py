import random


def main():
    print("猜數字遊戲！")
    print("我已經想好一個 1 到 100 的整數，你可以猜看看！")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess_text = input("請輸入你的猜測：")
        attempts += 1

        if not guess_text.strip():
            print("請輸入一個數字。")
            continue

        if not guess_text.strip().isdigit():
            print("輸入格式錯誤，請輸入正整數。")
            continue

        guess = int(guess_text)

        if guess < secret:
            print("再大一點！")
        elif guess > secret:
            print("再小一點！")
        else:
            print(f"恭喜你！你猜對了，答案是 {secret}。")
            print(f"你總共猜了 {attempts} 次。")
            break



if __name__ == "__main__":
    main()
