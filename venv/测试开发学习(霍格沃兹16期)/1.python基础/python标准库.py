import os
import time

# if "测试开发学习" not in os.listdir("./"):
#     os.mkdir("测试开发学习")

if not os.path.exists("测试开发学习"):
    os.mkdir("测试开发学习")

# print(os.listdir("./"))  # ==ls
# os.removedirs("测试开发学习")
# print(os.getcwd())

if not os.path.exists("测试开发学习/python标准库1.txt"):
    with open("测试开发学习/python标准库1.txt","w",encoding="utf-8") as f:
        f.write("你好")