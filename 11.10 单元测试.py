import unittest


class TestAddition(unittest.TestCase):

    # 开始的时候运行，可以在这里进行初始化
    def setUp(self):
        print('Setting the test')

    # 结束的时候运行，在这里销毁相关量
    def tearDown(self):
        print('Tearing down the test')

    # 测试的内容
    def test_addition(self):
        total = 2 + 2
        self.assertEqual(4, total)

    def test_name(self):
        name = 'Patrick'
        self.assertEqual('Patrick', name)

# 注意上面有两个测试
# setUp和tearDown是每个测试开始结束都要运行的
# 这里是输出两次Setting the test，Tearing down the test
# 而不是一次
if __name__ == '__main__':
    unittest.main()
