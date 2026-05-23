import tkinter as tk
import random


class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 猜數字遊戲")
        self.root.geometry("350x250")

        self.reset_game()

        # 標題
        self.label = tk.Label(
            root,
            text="請猜一個 1 ~ 100 的數字",
            font=("Arial", 14)
        )
        self.label.pack(pady=15)

        # 輸入框
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()

        # 按鈕
        self.button = tk.Button(
            root,
            text="確認",
            command=self.check_guess,
            font=("Arial", 12)
        )
        self.button.pack(pady=10)

        # 結果顯示
        self.result = tk.Label(
            root,
            text="",
            font=("Arial", 12)
        )
        self.result.pack()

        # 次數
        self.count_label = tk.Label(
            root,
            text="猜測次數：0",
            font=("Arial", 10)
        )
        self.count_label.pack()

        # Enter 可送出
        self.entry.bind("<Return>", lambda e: self.check_guess())

    def reset_game(self):
        self.answer = random.randint(1, 100)
        self.count = 0

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result.config(text="請輸入數字！")
            return

        self.count += 1
        self.count_label.config(text=f"猜測次數：{self.count}")

        if guess < self.answer:
            self.result.config(text="⬆️ 太小了")
        elif guess > self.answer:
            self.result.config(text="⬇️ 太大了")
        else:
            self.result.config(
                text=f"🎉 猜對了！答案是 {self.answer}"
            )

            self.root.after(2000, self.new_round)

        self.entry.delete(0, tk.END)

    def new_round(self):
        self.reset_game()
        self.result.config(text="重新開始！再猜一次～")
        self.count_label.config(text="猜測次數：0")


root = tk.Tk()
app = GuessNumberGame(root)

root.mainloop()