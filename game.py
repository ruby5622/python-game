import random

print("🎮 歡迎來到猜數字遊戲！")
print("我已經想好 1 到 100 之間的一個數字...")

number = random.randint(1, 100)
guess = None
count = 0

while guess != number:
    guess = int(input("請輸入你的猜測："))
    count += 1
    
    if guess < number:
        print("太小了！再試一次 🔼")
    elif guess > number:
        print("太大了！再試一次 🔽")
    else:
        print(f"🎉 恭喜你猜對了！總共猜了 {count} 次！")
