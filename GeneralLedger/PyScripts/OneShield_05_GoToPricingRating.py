from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, timedelta
import time
import unittest
import HtmlTestRunner

print("OneShield Go To Pricing/Rating")
try:
    class FL05(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF
        import AccessorRepository as AR

        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir

        def test_FL05_01_GoToPolicies(self):
            try:
                # Go To Pricing/Rating tab
                self.myDriver.find_element(By.CSS_SELECTOR, "#ctl00__MainContent_mnuDataTabs > .rmRootGroup > .rmItem:nth-child(8) .rmText").click()
                time.sleep(3)

                # Verify if the Search Policy page is opened
                # self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathlblPPolicyNumber).text, "Policy Number")


            except Exception as e51:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'GoToPricingRating'))
                self.fail(e51)


except Exception as e5:
    print('OneShield Go To Pricing/Rating script did not run successfully')
    print(e5)

