from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, timedelta
import time
import unittest
import HtmlTestRunner

print("OneShield_Login script")
try:
    class FL01(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF
        import AccessorRepository as AR

        uURL = myData['url']
        uClientID = myData['clientID']
        uLoginID = myData['LoginID']
        uPassword = myData['Password']
        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir

        def test_FL01_01_Launch_OneShield(self):
            try:
                # Launch URL for OneShield
                self.myDriver.get(self.uURL)
                self.myDriver.implicitly_wait(2)

                # Verify if the OneShield Login Page is displayed with logo
                self.myDriver.find_element_by_xpath(self.AR.xPathimgOSLoginLogo)

            except Exception as e11:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'LaunchOneSheld'))
                self.fail(e11)

        def test_FL01_02_Login_OneShield(self):
            try:
                # Enter Client id
                self.myDriver.find_element_by_xpath(self.AR.xPathlblOSClientID)
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idtxtOSClientID))).send_keys(self.uClientID)

                # Enter Login id
                self.myDriver.find_element_by_xpath(self.AR.xPathlblOSLoginID)
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idtxtOSLoginID))).send_keys(self.uLoginID)

                # Enter Password
                self.myDriver.find_element_by_xpath(self.AR.xPathlblOSPassword)
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idtxtOSPassword))).send_keys(self.uPassword)

                try:
                    # Check the checkbox for Logout all other active sessions
                    WebDriverWait(self.myDriver, 1).until(EC.element_to_be_clickable((By.ID, self.AR.idchkOSLogoutOtherSessions))).click()
                except Exception as e111:
                    x = 1

                # Click Login
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idbtnOSLogin))).click()
                time.sleep(3)

                # Verify if Home page is displayed
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathMenuOSHome)))

            except Exception as e12:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'LoginOneSheld'))
                self.fail(e12)
except Exception as e1:
    print('OneShield_Login Script did not run successfully')
    print(e1)

