import unittest

# 4、匹配目录下以XX开头的用例，执行这些用例
# 创建目录
testdir = "./"
# 匹配文件夹里面的test开头的测试用例
pipeideceshiyongli = unittest.defaultTestLoader.discover(testdir, pattern="test*.py")
# 运行测试用例
unittest.TextTestRunner(verbosity=2).run(pipeideceshiyongli)