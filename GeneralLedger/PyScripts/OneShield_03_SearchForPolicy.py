from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, timedelta
import time
import unittest
import HtmlTestRunner

print("OneShield Search for Policy Number")
try:
    class FL03(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF
        import AccessorRepository as AR

        uPolicyNumber = myData['Option1']
        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir

        def test_FL03_01_SearchForPolicy(self):
            try:
                # Enter Policy Number
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idtxtPPolicyNumber))).send_keys(self.uPolicyNumber)

                # Click Run Serach
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathbtnPRunSearch))).click()
                time.sleep(3)

                # Verify if the Policy is opened
                self.assertIn(self.uPolicyNumber, self.myDriver.find_element_by_xpath(self.AR.xPathlblPSummaryText).text)
                self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathtxtPDisabledPolicyNumber).get_attribute("value"), self.uPolicyNumber)

                print(self.myDriver.find_element_by_xpath('//*[@id="ctl00__MainContent_ucDataCtrl__dc_received_commission"]').get_attribute("value"))

            except Exception as e31:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'SearchForPolicy'))
                self.fail(e31)


except Exception as e3:
    print('OneShield Search for Policy script did not run successfully')
    print(e3)

