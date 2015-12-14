from selenium import selenium
import unittest, time, re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#driver = webdriver.Firefox()

#Test 1: Presence of Navbar in login file

#driver.get("http://127.0.0.1:8000/login/")

#print("chocolate")

#navBar = driver.find_elements_by_class_name("jumbotron")

#driver.quit()


#Test 1
"""
class TestOne(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		#self.selenium = selenium("localhost", 4444, "*firefox", "http://127.0.0.1:8000/")
		#self.selenium.start()
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/login")

	def test_new(self):
		val = self.driver.getCurrentUrl().text
		link = self.driver.find_element_by_xpath("//a")
		link.click()
		nval = self.driver.getCurrentUrl().text
		assert val != nval
		
	
		sel = self.selenium
		sel.open("/")
		sel.clickAndWait(xpath=id('list')/a)
		sel.waitForPageToLoad("http://localhost:8000/item/{{listing_id}}")
		sel.failUnless(sel.is_text_present("id"))

	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()
"""

class TestTwo(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		#self.selenium = selenium("localhost", 4444, "*firefox", "http://127.0.0.1:8000/")
		#self.selenium.start()
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/base1")

	def test_new(self):
		assert 'Music Swap' in self.driver.title
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()



class TestTwo(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		#self.selenium = selenium("localhost", 4444, "*firefox", "http://127.0.0.1:8000/")
		#self.selenium.start()
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/base2")

	def test_new(self):
		assert 'Music Swap' in self.driver.title
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()





		#self.assertEqual([], self.verificationErrors)

		"""
		sel = self.selenium
		sel.open("/")
		sel.clickAndWait(xpath=id('list')/a)
		sel.waitForPageToLoad("http://localhost:8000/item/{{listing_id}}")
		sel.failUnless(sel.is_text_present("id"))

		"""



if __name__ == '__main__':
	unittest.main()