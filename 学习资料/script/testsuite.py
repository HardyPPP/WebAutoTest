import unittest
from 学习资料.script.test1_testcase import Test01
from 学习资料.script.test2_testcase import Test02
suite = unittest.TestSuite()
# 实例化
case1 = Test01("test_add")
# suite.addTest(Test01("test_add"))
# 调用一个添加方法

suite.addTest(unittest.makeSuite(Test02))
runner = unittest.TextTestRunner()
runner.run(suite)
