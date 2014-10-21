# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Eraser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://biser-test.herokuapp.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_eraser(self):
        driver = self.driver
        driver.get(self.base_url + "/users/sign_in")
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("freakrage@yandex.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("qwerty")
        driver.find_element_by_name("commit").click()
        time.sleep(3)
        
        counter = 0
        while (counter < 999):
            time.sleep(2)
            driver.get(self.base_url + "/output_invoices")
            driver.find_element_by_css_selector("li.separated > a.icon-link").click()
            self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Jeste li sigurni da želite obrisati račun br\. 2014-0015[\s\S]$")
            counter = counter + 1
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
