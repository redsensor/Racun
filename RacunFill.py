#Importing required libs

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import contextlib

# Set up webdriver

class RacunFill(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://biser-test.herokuapp.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_racun1(self):
        driver = self.driver
# Login into Biser

        driver.get(self.base_url + "/users/sign_in")
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys("freakrage@yandex.ru")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("qwerty")
        driver.find_element_by_name("commit").click()
        time.sleep(3)
		
# Opening form and filling with sample data

        counter = 0
        while (counter < 6): #if you have errors when running script try to reduce this amount and run script few times, you can also create as more forms as you want
            time.sleep(1)
            driver.get(self.base_url + "/output_invoices/new")
            driver.find_element_by_id("partner_name").clear()
            text = driver.find_element_by_id("partner_name").send_keys("TopTal")
            driver.find_element_by_xpath("//input[@id='partner_name']").click()
            driver.find_element_by_id("partner_name").send_keys(Keys.DOWN)
            time.sleep(2)
            driver.find_element_by_id("partner_name").send_keys(Keys.DOWN)
            time.sleep(2)			
            driver.find_element_by_id("partner_name").send_keys(Keys.ENTER)
            time.sleep(2)
            #driver.find_element_by_id("output_invoice_city").clear()
            driver.find_element_by_id("output_invoice_city").send_keys("San Francisco")
            driver.find_element_by_id("output_invoice_items__description").clear()
            driver.find_element_by_id("output_invoice_items__description").send_keys("PC delivery")
            driver.find_element_by_id("output_invoice_items__quantity").clear()
            driver.find_element_by_id("output_invoice_items__quantity").send_keys("5,00")
            driver.find_element_by_id("output_invoice_items__price").clear()
            driver.find_element_by_id("output_invoice_items__price").send_keys("9.999,00")
            Select(driver.find_element_by_id("output_invoice_items__discount_type")).select_by_visible_text("$")
            driver.find_element_by_css_selector("option[value=\"amount\"]").click()
            driver.find_element_by_id("output_invoice_items__discount").clear()
            driver.find_element_by_id("output_invoice_items__discount").send_keys("5,00")
            Select(driver.find_element_by_id("output_invoice_items__tax_rate")).select_by_visible_text("0 %")
            driver.find_element_by_css_selector("option[value=\"0\"]").click()
            driver.find_element_by_css_selector("td.plus_sign > img").click()
            driver.find_element_by_xpath("(//input[@id='output_invoice_items__description'])[2]").clear()
            driver.find_element_by_xpath("(//input[@id='output_invoice_items__description'])[2]").send_keys("Flash delivery")
            driver.find_element_by_xpath("(//input[@id='output_invoice_items__quantity'])[2]").clear()
            driver.find_element_by_xpath("(//input[@id='output_invoice_items__quantity'])[2]").send_keys("15,00")
            driver.find_element_by_xpath("(//input[@id='output_invoice_items__price'])[2]").clear()
            driver.find_element_by_xpath("(//input[@id='output_invoice_items__price'])[2]").send_keys("200,00")
            driver.find_element_by_xpath("(//input[@id='output_invoice_items__discount'])[2]").clear()
            driver.find_element_by_xpath("(//input[@id='output_invoice_items__discount'])[2]").send_keys("8,00")
            ''' Select(driver.find_element_by_xpath("(//select[@id='output_invoice_items__discount_type'])[2]")).select_by_visible_text("$")
	        driver.find_element_by_xpath("(//option[@value='amount'])[2]").click()
	        Select(driver.find_element_by_xpath("(//select[@id='output_invoice_items__tax_rate'])[2]")).select_by_visible_text("5 %")
	        driver.find_element_by_xpath("(//option[@value='5'])[2]").click()
	        '''
            driver.find_element_by_name("commit").click()
            driver.find_element_by_link_text(u"Povratak na račune").click()
            counter = counter + 1
        print ("\n Seven Racuns filled! \n")
		
#Asserting data
        driver = self.driver

	#Checking page title
	
        try:	
            assert 'Biser' in driver.title
            print ('PASS(1)')
        except:
            print ('FAIL(1)')
            #name_of_exception = type(exception).__name__

	#Checking if partner name is correct
	
        try:	
            assert 'Toptal' in driver.find_element_by_partial_link_text('Toptal')
            print ('PASS(2)')
        except:
            print ('FAIL(2)')
            #name_of_exception = type(exception).__name__
			
	#Checking if amount is correct
	
        try:	
            assert "9,99 kn" in driver.find_elements_by_class_name('money_cell')
            print ('PASS(3)')
        except:
            print ('FAIL(3)')
            #name_of_exception = type(exception).__name__
			
        time.sleep(30) #remove this if you want webdriver to be closed immediately
        driver.close()
        ''' You can uncomment this and try if it works for you
        assert '21.10.2014.' in driver.find_elements_by_xpath("//td[4]")
        assert '28.10.2014.' in driver.find_elements_by_xpath("//td[5]")
        assert 'Toptal' in driver.find_element_by_partial_link_text('Toptal')
        assert "9,99 kn" in driver.find_elements_by_class_name('money_cell')
        assert 'Toptal' in driver.find_element_by_partial_link_text('Toptal')
        '''
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
