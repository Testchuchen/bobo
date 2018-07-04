# #模拟器自带计算器运算测试
# #coding=utf-8
from appium import webdriver
import unittest

class Test(unittest.TestCase):

      def setUp(self):
          desired_caps = {}
          desired_caps['platformName'] = 'Android'
          desired_caps['platformVersion'] = '4.4.2'
          desired_caps['deviceName'] = 'emulator-5554'
          desired_caps['appPackage'] = 'com.android.calculator2'
          desired_caps['appActivity'] = 'com.android.calculator2.Calculator'

          self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
          print('start test')


      def test_1(self):
          self.driver.find_element_by_name("1").click()

          self.driver.find_element_by_name("5").click()

          self.driver.find_element_by_name("9").click()

          self.driver.find_element_by_name("delete").click()

          self.driver.find_element_by_name("9").click()

          self.driver.find_element_by_name("5").click()

          self.driver.find_element_by_name("+").click()

          self. driver.find_element_by_name("6").click()

          self.driver.find_element_by_name("=").click()


      def tearDown(self):
           self.driver.quit()
           print('test end')


if __name__ == '__main__':
    unittest.main()




