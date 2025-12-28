import random

# 电脑随机生成1-100之间的数字
secret_number = random.randint(1, 100)
print("🎮 欢迎来到猜数字游戏！")
print("我已经想好了一个1-100之间的数字，你能猜到吗？")

while True:
    try:
        guess = int(input("请输入你猜的数字："))
        
        if guess < secret_number:
            print("📈 太小啦！往大一点猜~")
        elif guess > secret_number:
            print("📉 太大啦！修改你个凤！！~")

        else:
            print(f"🎉 恭喜你！猜对了！答案就是 {secret_number}！")
            break  # 猜对后退出循环
            
    except ValueError:
        print("⚠️ 请输入有效的数字哦！666666666666")

print("游戏结束，谢谢参与！")