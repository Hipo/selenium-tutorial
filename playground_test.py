# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest, time, re


class IletisimTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://timvroom.com"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_iletisim(self):
		driver = self.driver
		driver.get(self.base_url + "/selenium/playground/")
		title = driver.title
		# Step 1
		driver.find_element_by_id("answer1").send_keys(title)
		# Step 2
		driver.find_element_by_id("name").send_keys("Kilgore Trout")
		# Step 3
		Select(driver.find_element_by_id("occupation")).select_by_visible_text("Science Fiction Author")
		# Step 4
		count = len(driver.find_elements_by_class_name("bluebox"))
		driver.find_element_by_id("answer4").send_keys(count)
		

		raw_input("")
		self.assertEqual(u"Merhaba", driver.find_element_by_class_name("welcome").text)

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True

	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException, e: return False
		return True

	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()
