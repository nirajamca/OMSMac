from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, timedelta
import time
import unittest
import HtmlTestRunner

print("OneShield Go To Policies Tab")
try:
    class FL02(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF
        import AccessorRepository as AR

        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir

        def test_FL02_01_GoToPolicies(self):
            try:
                # Go to Policies Menu item in the left Panel
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathlnkPolicies))).click()
                time.sleep(3)

                # Verify if the Search Policy page is opened
                self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathlblPPolicyNumber).text, "Policy Number")


            except Exception as e21:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'GoToPolicies'))
                self.fail(e21)


except Exception as e2:
    print('OneShield Go To Policies script did not run successfully')
    print(e2)

