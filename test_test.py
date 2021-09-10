import pytest
import time


class Testtest():

    @pytest.fixture(scope='function')
    def test_inout(self):
        print('成功打开浏览器并进入禅道')
        yield 1
        time.sleep(2)
        print('退出成功！')
        time.sleep(5)
        print('成功关闭浏览器！')

    def test_login1(self, test_inout):
        assert test_inout == 1
        print("登录成功")

    def test_login2(self,test_inout):
        assert test_inout == 1
        print('测试用例执行成功')


if __name__ == '__main__':
    pytest.main(['-vs', 'test_test.py'])
