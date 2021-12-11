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
import os

print('OneShield_Quotations Script')
try:
    class FL07(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF, OneShieldFunctions as OSF
        import AccessorRepository as AR

        uQCarrier = myData['Option1']
        uQDescription = myData['Option2']
        uQBrokerCommission = myData['Option3']
        uQInstallmentPlan = myData['Option4']
        uRSRFactor = myData['Option5']
        uRSRFactorApplied = myData['Option6']
        uNRSRFactor = myData['Option7']
        uNRSRFactorApplied = myData['Option8']

        uComplexityofRisk = myData['Option9']
        uRevenueSource = myData['Option10']
        uCvrgEnhancementsRestrictions = myData['Option11']
        uPrimaryCoverageTerms = myData['Option12']

        uAppScheduleRating = myData['Option13']
        uMktPricingAdjFactor = myData['Option14']

        uExtendedReportingPeriod = myData['Option15']
        uExtendedReportingPeriodFactor = myData['Option16']

        uRunoffPolicies = myData['Option17']
        uRunoffPoliciesFactor = myData['Option18']

        uIDLCoverage = myData['Option19']
        uSideACoverage = myData['Option20']
        uFurtherAdjustment = myData['Option21']

        uRejectTerrorismCoverage = myData['Option22']
        uTerrorismDiscount = myData['Option23']

        uLOLLimit = myData['Option24']
        uLOLDedRet = myData['Option25']

        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir
        mySRAFile = 'CaptureRangeAllowed.txt'
        uRangeState = ''

        def test_FL07_01_GoToQuotations(self):
            try:
                # Go to Quotations Tab
                self.myDriver.find_element(By.CSS_SELECTOR, "#ctl00__MainContent_mnuDataTabs > .rmRootGroup > .rmItem:nth-child(6) .rmText").click()
                time.sleep(3)

            except Exception as e71:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'GoToQuotations'))
                self.fail(e71)

        def test_FL07_02_AddOrganization(self):
            try:
                try:
                    # print(self.myDriver.find_element(By.ID, 'ctl00MainContent_uc_QuoteWrapper_QuoteListControl_radgvHeaders_ctl00').text)
                    self.assertIn('Excess Follow form', self.myDriver.find_element(By.ID, 'ctl00MainContent_uc_QuoteWrapper_QuoteListControl_radgvHeaders_ctl00').text, 'Is this printing')

                    print('Select the existing record, do not create new one')

                except Exception as e721:
                    print('no record found')

                    # Click Add button to add an Organization
                    WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idbtnQuotationsAddOrg))).click()
                    time.sleep(3)


                    # Select Carrier
                    self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddQCarrier, self.uQCarrier)

                    # Add Description
                    self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQCarrierDesc, self.uQDescription)

                    # Broker Commission
                    self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQBrokerCommission, self.uQBrokerCommission)

                    # Select Installment plan type
                    self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddQInstallmentPlan, self.uQInstallmentPlan)

                    # Click Save to add the ord record
                    WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idbtnQuotationsSave))).click()
                    time.sleep(2)

                    WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.myDriver.find_element(By.ID, 'ctl00MainContent_uc_QuoteWrapper_QuoteListControl_radgvHeaders_ctl00__0')))).click()
                    time.sleep(2)

            except Exception as e72:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'AddOrganization'))
                # self.fail(e72)

        def test_FL07_03_SelectQuote(self):
            try:
                # Select the already existing or a newly created Quote
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00MainContent_uc_QuoteWrapper_QuoteListControl_radgvHeaders_ctl00__0"]/td[2]'))).click()
                time.sleep(2)
            except Exception as e73:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'SelectQuote'))
                self.fail(e73)

        def test_FL07_04_EnterRangeStateElements(self):
            try:
                # Open the file that has Range State indicator, created during either New Submission creation
                # or Select an existing Submission

                # Open file in read only mode
                f1 = open(self.mySRAFile, "r")

                # Read the file and assign value to uRangeState, close and remove the file
                self.uRangeState = f1.read()
                f1.close()
                os.remove(self.mySRAFile)

                # uRangeState can be either Yes or No based on data from State List of
                # Range states vs Non Range states.xlsx file
                if self.uRangeState == 'Yes':
                    # If its a range state, enter values in Range State Risk Factor and
                    # Range State Risk Factor Applied
                    self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddlQRangeStateRiskFactor, self.uRSRFactor)
                    self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQRangeStateRiskFactorApplied, self.uRSRFactorApplied)

                elif self.uRangeState == 'No':
                    # If its not a range state, enter values in Non-Range State Risk Factor and
                    # Non-Range State Risk Factor Applied
                    self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddlQNonRangeStateRiskFactor, self.uNRSRFactor)
                    self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQNonRangeStateRiskFactorApplied, self.uNRSRFactorApplied)

            except Exception as e74:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'EnterRangeStateElements'))
                self.fail(e74)

        def test_FL07_05_AddScheduleRating(self):
            try:

                # Category		                            CW (x CA & NY)	CA	        NY	        GA
                # i.    Complexity of Risk		            +/- 25%	        +/- 15%     +/- 10%	    +/- 25%
                # ii.   Revenue Source		                +/- 25%	        +/- 15%	    +/- 10%	    +/- 25%
                # iii.  Coverage Enhancements/Restrictions	+/- 25%	        +/- 15%	    +/- 10%	    N/A
                # iv.   Primary Coverage Terms		        +/- 25%	        +/- 15%	    +/- 10%	    +/- 25%

                # Complexity of Risk
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQComplexityofRisk, self.uComplexityofRisk)

                # Revenue Source
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQRevenueSource, self.uRevenueSource)

                # Coverage Enhancements/Restrictions
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQCvrgEnhancementsRestrictions, self.uCvrgEnhancementsRestrictions)

                # Primary Coverage Terms
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQPrimaryCoverageTerms, self.uPrimaryCoverageTerms)

                # Applied Schedule Rating
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQAppScheduleRating, self.uAppScheduleRating)

                # Market Pricing Adjustment Factor (60% - 85%)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQMktPricingAdjFactor, self.uMktPricingAdjFactor)

                # Extended Reporting Period and factor applied (Non-admitted)
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddQExtendedReportingPeriod, self.uExtendedReportingPeriod)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQExtendedReportingPeriodFactor, self.uExtendedReportingPeriodFactor)

                # Run off Policies and factor applied (Non-admitted)
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddQRunoffPolicies, self.uRunoffPolicies)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQRunoffPoliciesFactor, self.uRunoffPoliciesFactor)

                # Independent Directors Liability
                if self.uIDLCoverage != "":
                    self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQIDLCoverage, self.uIDLCoverage)

                # Side A Coverage
                if self.uSideACoverage != "":
                    self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQSideACoverage, self.uSideACoverage)

                # Further percentage adjustment to Average Score of Risk
                if self.uFurtherAdjustment != "":
                    self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQFurtherAdjustment, self.uFurtherAdjustment)

                # Reject Terrorism Coverage
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddQRejectTerrorismCoverage, self.uRejectTerrorismCoverage)
                if self.uRejectTerrorismCoverage == 'Yes':
                    self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQTerrorismDiscount, self.uTerrorismDiscount)

            except Exception as e75:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'AddScheduleRating'))
                self.fail(e75)

        def test_FL07_06_EnterCoverage(self):
            try:
                # Coverage table
                # Limit of Liability
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idchkQCoverageLimitofLiabilty))).click()

                # Limit
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQCoverageLOLLimit, self.uLOLLimit)

                # Deductible/Retention
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtQCoverageLOLDedRet, self.uLOLDedRet)


            except Exception as e76:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'EnterCoverage'))
                self.fail(e76)


        def test_FL07_07_SaveandPrice(self):
            try:
                # # Save and Price
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.ID, self.AR.idbtnQSaveandPrice))).click()
                time.sleep(1)

                # Verify if the record has been successfully created
                assert self.myDriver.find_element(By.ID, "ctl00__MainContent_ucMessages_lblInfoMsg").text == "Quotation has been saved !!"

                uHREF = WebDriverWait(self.myDriver, 10).until(EC.visibility_of_element_located((By.XPATH, self.AR.xPathlnkQRaterFile))).get_attribute('href')

                WebDriverWait(self.myDriver, 10).until(EC.visibility_of_element_located((By.XPATH, self.AR.xPathlnkQRaterFile))).click()
                time.sleep(5)

                print("Premium from Rater file: ", self.BF.fncGetFinalPremiumFromRater(uHREF))
                print("Premium from Quotation page: ", self.myDriver.find_element(By.ID, self.AR.idlblQPremium).text)

                assert self.myDriver.find_element(By.ID, self.AR.idlblQPremium).text == self.BF.fncGetFinalPremiumFromRater(uHREF)




            except Exception as e77:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'SaveandPrice'))
                self.fail(e77)


except Exception as e7:
    print('OneShield_Quotations Script did not run successfully')
    print(e7)

