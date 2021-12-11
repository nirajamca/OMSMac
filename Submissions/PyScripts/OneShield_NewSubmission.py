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
print("OneShield_NewSubmission script")

try:
    class FL02(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF, OneShieldFunctions as OSF
        import AccessorRepository as AR

        uInsuredOrg = myData['Option1']
        uUnderwriter = myData['Option2']
        uChangeState = myData['Option3']
        uRangeState = myData['Option4']

        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir
        mySRAFile = 'CaptureRangeAllowed.txt'

        def test_FL02_01_NSOverView(self):
            try:
                uEffDate = date.today().strftime("%m/%d/%Y")

                # Go to New Submission menu item
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathMenuNewSubmission))).click()
                time.sleep(3)

                # Verify if the Overview tab is opened
                self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathtabNSOverview).text, "Overview")


                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathtxtNSOInsured))).send_keys(self.uInsuredOrg)
                time.sleep(2)

                self.myDriver.find_element_by_xpath(self.AR.xPathtxtNSOInsured).send_keys(Keys.DOWN)
                time.sleep(2)

                self.myDriver.find_element_by_xpath(self.AR.xPathtxtNSOInsured).send_keys(Keys.RETURN)
                time.sleep(2)

                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathddNSOProgram))).click()
                time.sleep(2)

                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathddNSOProgramOption))).click()
                time.sleep(2)

                # Enter Proposed Effective Date
                self.myDriver.find_element(By.ID, self.AR.idtxtNSOEffDate).send_keys(uEffDate)
                time.sleep(2)

                # Underwriter
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddNSUnderwriter, self.uUnderwriter)

            except Exception as e11:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'LaunchOneSheld'))
                self.fail(e11)

        def test_FL02_02_ChangeRiskStateIfRequired(self):
            try:
                # If ChangeState flag is set to Yes, update the Risk State
                if self.uChangeState == 'Yes':
                    self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idtxtNSRiskState, self.uRangeState)

            except Exception as e22:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'ChangeRiskStateIfRequired'))
                self.fail(e22)


        def test_FL02_03_SaveNewSubmission(self):
            try:
                # Click Next to save UW Questions
                self.myDriver.find_element(By.ID, self.AR.idbtnOneShieldNext).click()
                time.sleep(2)

                # Verify if the record has been successfully created
                # assert self.myDriver.find_element(By.ID, "ctl00__MainContent_ucMessages_lblInfoMsg").text == "Record has been saved"

                self.myDriver.find_element_by_xpath('//*[@id="ctl00__MainContent_mnuDataTabsLevel3"]/ul/li[1]/a/span').click()
                time.sleep(3)

                print(self.myDriver.find_element(By.ID, 'ctl00__MainContent_lbSummaryText').text)

                # Save the Risk State/Territory
                uRangeState = self.myDriver.find_element(By.ID, self.AR.idtxtNSRiskState).text


                f1 = open(self.mySRAFile, "w+")
                f1.write(self.OSF.fncGetStateRangeAllowed(uRangeState))
                f1.close()
            except Exception as e23:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'SaveNewSubmission'))
                self.fail(e23)

except Exception as e1:
    print('OneShield_NewSubmission script did not run successfully')
    print(e1)

