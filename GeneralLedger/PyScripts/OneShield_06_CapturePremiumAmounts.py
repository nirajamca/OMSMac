from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, timedelta
import time
import unittest
import HtmlTestRunner


print("OneShield Capture Premium Amounts")
try:
    class FL06(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF, OneShieldFunctions as OSF
        import AccessorRepository as AR

        uPolicyNumber = myData['Option1']
        uFilename = 'GLBaseFile.xlsx'
        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir

        def test_FL06_01_CaptureCommissionReceived(self):
            try:
                uLimitOfLiability = self.myDriver.find_element_by_xpath(self.AR.xPathtxtPLimitOfLiability).text
                uSurplusLinesStateTax = self.myDriver.find_element_by_xpath(self.AR.xPathtxtPSurplusLinesStateTax).text
                uStampingFee = self.myDriver.find_element_by_xpath(self.AR.xPathtxtPStampingFee).text
                uOtherStateFee = self.myDriver.find_element_by_xpath(self.AR.xPathtxtPOtherStateFee).text
                uProcessingFee = self.myDriver.find_element_by_xpath(self.AR.xPathtxtPProcessingFee).text

                # Add Premium Amounts to GL Base file for calculations
                self.OSF.fncAddDataToGLBaseFile(self.uFilename, 'Limit Of Liability', uLimitOfLiability)
                self.OSF.fncAddDataToGLBaseFile(self.uFilename, 'Surplus Lines State Tax', uSurplusLinesStateTax)
                self.OSF.fncAddDataToGLBaseFile(self.uFilename, 'Stamping Fee', uStampingFee)
                self.OSF.fncAddDataToGLBaseFile(self.uFilename, 'Other State Fee', uOtherStateFee)
                self.OSF.fncAddDataToGLBaseFile(self.uFilename, 'Processing Fee', uProcessingFee)

            except Exception as e61:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'CapturePremiumAmounts'))
                self.fail(e61)


except Exception as e6:
    print('OneShield Capture Premium Amounts script did not run successfully')
    print(e6)

