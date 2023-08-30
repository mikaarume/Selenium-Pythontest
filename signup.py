import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestSignup(unittest.TestCase): 

    def setUp(self): 
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(options=options)
        # self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_signup(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("apaajaqa") # isi name
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("arumeningmika@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("1q2w3e4r5t") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()