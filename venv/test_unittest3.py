import unittest


# 被测试方法
class testclass:
    def beiceshi(self, b):
        print("被测试的方法")
        a = 10
        return a / b

# 测试用例
class testOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.shili = testclass()
        print('set up class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown class')

    def testequal(self):
        print('断言方法测试')
        self.assertNotEqual(20,21,"判断1不等于1")
        # self.assertEqual(54,55,"判断55==55")
    def test_1(self):
        print("开始测试用例")
        # 实例对象
        # aa = testclass()
        b = self.shili.beiceshi(2)
        assert 5 == b
        print('用例测试完成')

    def test_2(self):
        print("开始测试用例2")
        # 实例对象
        # aa = testclass()
        b = self.shili.beiceshi(2)
        assert 5 == b
        print('用例测试完成2')

    def test_3(self):
        print("开始测试用例3")
        # 实例对象
        # aa = testclass()
        b = self.shili.beiceshi(2)
        assert 5 == b
        print('用例测试完成3')
# 测试用例2
class testTwo(unittest.TestCase):
    #测试开始前准备
    @classmethod
    def setUpClass(cls) -> None:
        cls.shili = testclass()
        print('set up class2')
    #测试结束后清除内容
    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown class2')

    def test_1(self):
        print("开始测试用例2")
        # 实例对象
        # aa = testclass()
        b = self.shili.beiceshi(2)
        assert 5 == b
        print('用例测试完成22')

    def test_2(self):
        print("开始测试用例22")
        # 实例对象
        # aa = testclass()
        b = self.shili.beiceshi(2)
        assert 5 == b
        print('用例测试完成22')

    def test_3(self):
        print("开始测试用例23")
        # 实例对象
        # aa = testclass()
        b = self.shili.beiceshi(2)
        assert 5 == b
        print('用例测试完成23')



if __name__ =='__main__':
    # 1、执行所有的
    # unittest.main()

    # 2、执行指定的测试用例
    # 创建测试套
    # testsuite1 = unittest.TestSuite()
    # # 给测试套加用例
    # testsuite1.addTest(testOne("testequal"))
    # testsuite1.addTest(testOne("test_2"))
    # # 运行测试套
    # unittest.TextTestRunner().run(testsuite1)

    # 3、批量执行某个测试类
    # 匹配类里面的测试用例
    # testsuite1 = unittest.TestLoader().loadTestsFromTestCase(testTwo)
    # testsuite2 = unittest.TestLoader().loadTestsFromTestCase(testOne)
    # #创建测试套件
    # s2 = unittest.TestSuite([testsuite1,testsuite2])
    # #运行测试套件
    # unittest.TextTestRunner(verbosity=2).run(s2)

    # 4、匹配目录下以XX开头的用例，执行这些用例
    # 创建目录
    testdir = "./"
    # 匹配文件夹里面的test开头的测试用例
    pipeideceshiyongli =unittest.defaultTestLoader.discover(testdir,pattern="test*.py")
    # 运行测试用例
    unittest.TextTestRunner(verbosity=2).run(pipeideceshiyongli)