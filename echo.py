import sys
def echo():
    shout = "\-s" in sys.argv
    message = input("输入内容：")  # 提示文本已修改
    print(message.upper() if shout else message)
if __name__ == "__main__":
    echo()