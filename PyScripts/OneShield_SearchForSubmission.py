from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import date, time, timedelta
import time
import unittest
import HtmlTestRunner

print('OneShield_SearchForSubmission script')

try:
    class FL03(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF, OneShieldFunctions as OSF
        import AccessorRepository as AR

        uSubmission = myData['Option2']
        uChangeState = myData['Option3']
        uRangeState = myData['Option4']

        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir
        mySRAFile = 'CaptureRangeAllowed.txt'

        def test_FL03_01_SearchForSubmissions(self):
            try:
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathMenuSubmissions))).click()
                time.sleep(3)

                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idtxtSubmissionSearchSubNumber))).send_keys(self.uSubmission)
                time.sleep(3)

                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathbtnSubmissionsRunSearch))).click()
                time.sleep(5)

            except Exception as e31:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'SearchForSubmissions'))
                self.fail(e31)

        def test_FL03_02_ChangeRiskStateIfRequired(self):
            try:
                # print(self.uRangeState)
                # If ChangeState flag is set to Yes, update the Risk State
                if self.uChangeState == 'Yes':
                    self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idtxtNSRiskState, self.uRangeState)

                    # Click Next to save UW Questions
                    self.myDriver.find_element(By.ID, self.AR.idbtnOneShieldNext).click()
                    time.sleep(2)

                else:
                    # Save the Risk State/Territory
                    self.uRangeState = self.myDriver.find_element(By.ID, self.AR.idtxtNSRiskState).text

                print(self.myDriver.find_element(By.ID, 'ctl00__MainContent_lbSummaryText').text)

                if(self.uRangeState is None):
                    self.uRangeState = 'New York'

                # print(self.uRangeState)

                f1 = open(self.mySRAFile, "w+")
                f1.write(self.OSF.fncGetStateRangeAllowed(self.uRangeState))
                f1.close()

            except Exception as e32:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'ChangeRiskStateIfRequired'))
                self.fail(e32)



except Exception as e1:
    print('OneShield_SearchForSubmission did not run successfully')
    print(e1)

