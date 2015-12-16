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

class TestTitle1(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/base1")

	def test_new(self):
		assert 'Music Swap' in self.driver.title
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()



class TestTitle2(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/base2")

	def test_new(self):
		assert 'Music Swap' in self.driver.title
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()



class TestTitle3(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/base3")

	def test_new(self):
		assert 'Music Swap' in self.driver.title
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()


############################################################################################################################


class TestLink(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/login")

	def test_new(self):
		about = self.driver.find_element_by_link_text('About')
		self.driver.get_screenshot_as_file("/tmp/link.png") ################SCREENSHOT#################
		about.click()
		assert self.driver.current_url == "http://127.0.0.1:8000/about/"
		self.driver.get_screenshot_as_file("/tmp/link_about.png") ################SCREENSHOT#################
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()




class TestLogin(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/login")

	def test_new(self):
		self.driver.find_element_by_id("id_uname").send_keys('bob')
		self.driver.find_element_by_id("id_pword").send_keys('bob')
		self.driver.get_screenshot_as_file("/tmp/login.png") ################SCREENSHOT#################
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		assert self.driver.current_url == "http://127.0.0.1:8000/profile/"
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()


#Include test for when not all values are submitted

class TestLogin_inc(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/login")

	def test_new(self):
		self.driver.find_element_by_id("id_uname").send_keys('bob')
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		assert self.driver.find_element_by_class_name("errorlist").text == "This field is required."
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()




class TestAcct(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/create_user")

	def test_new(self):
		self.driver.find_element_by_id("id_first_name").send_keys('bob')
		self.driver.find_element_by_id("id_last_name").send_keys('bob')
		self.driver.find_element_by_id("id_username").send_keys('bob')
		self.driver.find_element_by_id("id_password").send_keys('bob')
		self.driver.find_element_by_css_selector("select#id_type_of_user > option[value='Artist']").click()
		self.driver.get_screenshot_as_file("/tmp/acct.png") ################SCREENSHOT#################
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		assert self.driver.current_url == "http://127.0.0.1:8000/home/"
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()


#Include test for when not all values are submitted

class TestAcct_inc(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/create_user")

	def test_new(self):
		self.driver.find_element_by_id("id_first_name").send_keys('bob')
		self.driver.find_element_by_id("id_last_name").send_keys('bob')
		self.driver.find_element_by_id("id_username").send_keys('bob')
		self.driver.find_element_by_css_selector("select#id_type_of_user > option[value='Artist']").click()
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		assert self.driver.find_element_by_class_name("errorlist").text == "This field is required."
	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()


#Test CreateListing

class TestCreate(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/create_user")

	def test_new(self):
		self.driver.find_element_by_id("id_first_name").send_keys('bob')
		self.driver.find_element_by_id("id_last_name").send_keys('bob')
		self.driver.find_element_by_id("id_username").send_keys('bob')
		self.driver.find_element_by_id("id_password").send_keys('bob')
 		self.driver.find_element_by_css_selector("select#id_type_of_user > option[value='Artist']").click()
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		prof = self.driver.find_element_by_link_text('Profile')
		prof.click()
		create = self.driver.find_element_by_link_text('Create a Listing')
		create.click()
		self.driver.find_element_by_id("id_title").send_keys('anything')
		self.driver.find_element_by_id("id_description").send_keys('anything')
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		assert self.driver.current_url == "http://127.0.0.1:8000/create_listing_success/"

	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()

#Test CreateListing Incomplete Form
class TestCreate_inc(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/create_user")

	def test_new(self):
		self.driver.find_element_by_id("id_first_name").send_keys('bob')
		self.driver.find_element_by_id("id_last_name").send_keys('bob')
		self.driver.find_element_by_id("id_username").send_keys('bob')
		self.driver.find_element_by_id("id_password").send_keys('bob')
 		self.driver.find_element_by_css_selector("select#id_type_of_user > option[value='Artist']").click()
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		prof = self.driver.find_element_by_link_text('Profile')
		prof.click()
		create = self.driver.find_element_by_link_text('Create a Listing')
		create.click()
		self.driver.find_element_by_id("id_title").send_keys('anything')
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		assert self.driver.find_element_by_class_name("errorlist").text == "This field is required."

	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()


#Test Search : CreateUser, Navigate to Homepage, Go to Profile, Search, Hit results Page 
class TestSearch(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/create_user")

	def test_new(self):
		self.driver.find_element_by_id("id_first_name").send_keys('bob')
		self.driver.find_element_by_id("id_last_name").send_keys('bob')
		self.driver.find_element_by_id("id_username").send_keys('bob')
		self.driver.find_element_by_id("id_password").send_keys('bob')
 		self.driver.find_element_by_css_selector("select#id_type_of_user > option[value='Artist']").click()
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		prof = self.driver.find_element_by_link_text('Profile')
		prof.click()
		self.driver.find_element_by_id("id_search_input").send_keys('anything')
		assert self.driver.current_url == "http://127.0.0.1:8000/searchresults/"

	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()



#Test Logout

class TestLogout(unittest.TestCase):

	def setUp(self):
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		self.driver.get("http://127.0.0.1:8000/create_user")

	def test_new(self):
		self.driver.find_element_by_id("id_first_name").send_keys('bob')
		self.driver.find_element_by_id("id_last_name").send_keys('bob')
		self.driver.find_element_by_id("id_username").send_keys('bob')
		self.driver.find_element_by_id("id_password").send_keys('bob')
 		self.driver.find_element_by_css_selector("select#id_type_of_user > option[value='Artist']").click()
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		prof = self.driver.find_element_by_link_text('Profile')
		prof.click()
		logout = self.driver.find_element_by_link_text('Logout')
		logout.click()
		assert self.driver.current_url == "http://127.0.0.1:8000/logoutsuccess/"

	

	def tearDown(self):
		#self.selenium.stop()
		self.driver.quit()



#######################################
#RUN TEST FOR LISTING LINK ON HOMEPAGE#
#######################################


if __name__ == '__main__':
	unittest.main()
