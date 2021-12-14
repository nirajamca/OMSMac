from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, timedelta
import time
import unittest
import HtmlTestRunner


print("OneShield Capture Commission Received")
try:
    class FL04(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF, OneShieldFunctions as OSF
        import AccessorRepository as AR

        uPolicyNumber = myData['Option1']
        uFilename = 'GLBaseFile.xlsx'
        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir

        def test_FL04_01_CaptureCommissionReceived(self):
            try:
                uCommissionPercentage = self.myDriver.find_element_by_xpath(self.AR.xPathtxtPDisabledCommission).get_attribute("value")

                # Add Commission Percentage to GL Base file for calculations
                self.OSF.fncAddDataToGLBaseFile(self.uFilename, 'Commission Percentage', uCommissionPercentage )

            except Exception as e41:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'CaptureCommissionReceived'))
                self.fail(e41)


except Exception as e4:
    print('OneShield Capture Commission Received script did not run successfully')
    print(e4)

