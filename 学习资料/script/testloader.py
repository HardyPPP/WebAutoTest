import unittest

# suite = unittest.TestLoader().discover("../cases")
# 在指定目录下测试所有test开头的.py文件（默认）

suite = unittest.TestLoader().discover("../cases", pattern="tpshop*.py")
# 在指定目录下测试所有给定pattern开头的.py文件（tpshop）

unittest.TextTestRunner().run(suite)
