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

print('OneShield_UWQuestions Script')
try:
    class FL04(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF, OneShieldFunctions as OSF
        import AccessorRepository as AR

        uMarketCap = myData['Option1']
        uTotalAssets = myData['Option2']
        uAnnualRevenues = myData['Option3']
        uOrgCategory = myData['Option4']
        uTicker = myData['Option5']
        uFinCondition = myData['Option6']
        uNoOperations = myData['Option7']
        uAcqHistory = myData['Option8']
        uMgtQuality = myData['Option9']
        uLtgHistory = myData['Option10']
        uTimeInBusiness = myData['Option11']
        uClsBusiness = myData['Option12']

        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir

        def test_FL04_01_GoToUWQuestions(self):
            try:
                # Go to UW Questions Tab
                self.myDriver.find_element(By.CSS_SELECTOR, "#ctl00__MainContent_mnuDataTabs > .rmRootGroup > .rmItem:nth-child(2) .rmText").click()
                time.sleep(3)

            except Exception as e41:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'GoToUWQuestions'))
                self.fail(e41)

        def test_FL04_02_AddPolicyInformation(self):
            try:

                # Market Cap
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtUWQMarketCap, self.uMarketCap)


                # Total Assets
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtUWQTotalAssets, self.uTotalAssets)

                # Annual Revenues
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtUWQAnnualRevenues, self.uAnnualRevenues)

                # Organization Category
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddUWQOrgCategory, self.uOrgCategory)

                # Ticker Symbol
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtUWQTicker, self.uTicker)

            except Exception as e42:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'AddPolicyInformation'))
                self.fail(e42)

        def test_FL04_03_AddUnderlyingInsuranceRiskFactors(self):
            try:
                # Financial Condition
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddUWQFinCondition, self.uFinCondition)

                # Nature of Operations
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddUWQNoOperations, self.uNoOperations)

                # Acquisition History
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddUWQAcqHistory, self.uAcqHistory)

                # Management Quality
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddUWQMgtQuality, self.uMgtQuality)

                # Litigation History
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddUWQLtgHistory, self.uLtgHistory)

                # Time in Business
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddUWQTimeInBusiness, self.uTimeInBusiness)

                # Class of Business
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddUWQClsBusiness, self.uClsBusiness)

            except Exception as e43:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'AddUnderlyingInsuranceRiskFactors'))
                self.fail(e43)

        def test_FL04_04_SaveUWQuestions(self):
            try:
                # Click Next to save UW Questions
                self.myDriver.find_element(By.ID, self.AR.idbtnOneShieldNext).click()
                time.sleep(2)

                # Verify if the record has been successfully created
                assert self.myDriver.find_element(By.ID, "ctl00__MainContent_ucMessages_lblInfoMsg").text == "Record has been saved"

            except Exception as e44:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'SaveUWQuestions'))
                self.fail(e44)

except Exception as e4:
    print('OneShield_UWQuestions Script did not run successfully')
    print(e4)

