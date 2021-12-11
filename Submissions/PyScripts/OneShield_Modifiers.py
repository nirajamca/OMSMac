from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import date, time, timedelta
import time
import unittest
import HtmlTestRunner

print('OneSubmission_Modifiers Script')

try:
    class FL05(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF, OneShieldFunctions as OSF
        import AccessorRepository as AR

        uCreditForSideA = myData['Option2']
        uCreditForIDL = myData['Option3']
        uNoOfOperations = myData['Option4']
        uNYOAppliedFactor = myData['Option5']
        uSNFMAActivity = myData['Option6']
        uSNFMAAppliedFactor = myData['Option7']
        uSECOffering = myData['Option8']
        uSECOfferingAppliedFactor = myData['Option9']
        uDOLitigation = myData['Option10']
        uDOLitigationAppliedFactor = myData['Option11']
        uOtherLitigation = myData['Option12']
        uOtherLitigationAppliedFactor = myData['Option13']
        uCoinsurance = myData['Option14']
        uCOSECClaims = myData['Option15']
        uCOSECClaimsAppliedFactor = myData['Option16']
        uIndustryRisk = myData['Option17']
        uIndustryRiskAppliedFactor = myData['Option18']
        uDiscovery = myData['Option19']
        uDiscoveryAppliedFactor = myData['Option20']
        uClaimLitigationHistory = myData['Option21']
        uCorpGovernanceProcedure = myData['Option22']
        uEarningConsistency = myData['Option23']
        uEffectedByRecession = myData['Option24']
        uEnvironmentalIssues = myData['Option25']
        uFinancialSolvency = myData['Option26']
        uInsiderTradingActivity = myData['Option27']
        uJointVentures = myData['Option28']
        uLaborRelations = myData['Option29']
        uLiquidity = myData['Option30']
        uMajorCustomers = myData['Option31']
        uManagementStability = myData['Option32']
        uManagementOwnership = myData['Option33']
        uOtherFinFactors = myData['Option34']
        uQualityExtBrdMembers = myData['Option35']
        uRegulatoryExposure = myData['Option36']
        uStabilityofWorkforce = myData['Option37']
        uStockMrktSensitivity = myData['Option38']
        uStockVolatility = myData['Option39']
        uTakeoverPotential = myData['Option40']
        uTerrorismRiskDiscount = myData['Option41']
        uTransactionEvent = myData['Option42']

        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir

        def test_FL05_01_GoToModifiers(self):
            try:
                xPathOSHeader = '//*[@id="ctl00__MainContent_ucDataCtrl_pnlDataControl"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/span'

                if self.myDriver.find_element(By.XPATH, xPathOSHeader).text == 'Coverage Modifiers':
                    y=1
                else:
                    # Go to Modifiers tab
                    self.myDriver.find_element(By.CSS_SELECTOR, "#ctl00__MainContent_mnuDataTabs > .rmRootGroup > .rmItem:nth-child(3) .rmText").click()
                    time.sleep(3)

            except Exception as e51:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'GoToModifiers'))
                self.fail(e51)

        def test_FL05_02_AddCoverageModifiers(self):
            try:
                # Credit for Side A Only with DIC Coverage
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMSideAOnly, self.uCreditForSideA)

                # Credit for IDL Only with DIC Coverage
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMIDEOnly, self.uCreditForIDL)

                # Number of Years in Operations and Applied Factor
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddMNumberOfYearsInOperation, self.uNoOfOperations)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMNumberOfYearsInOperationsFactors, self.uNYOAppliedFactor)

                # Significant M&A Activity / Level of M&A Concern and Applied Factor
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddMLevelOfMAConcern, self.uSNFMAActivity)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMLevelOfMAConcernFactor, self.uSNFMAAppliedFactor)

                # SEC Offering and Applied Factor
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddMSECOffering, self.uSECOffering)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMSECOfferingFactor, self.uSECOfferingAppliedFactor)

                # D&O Litigation and Applied Factor
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddMDOLitigation, self.uDOLitigation)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMDOLitigationFactor, self.uDOLitigationAppliedFactor)

                # Other Litigation and Applied Factor
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddMOtherLitigation, self.uOtherLitigation)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMOtherLitigationFactor, self.uOtherLitigationAppliedFactor)

                # Coinsurance
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMCoinsurance, self.uCoinsurance)

                 # Coinsurance re SEC Claims
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddMCOSECClaims, self.uCOSECClaims)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMCOSECClaimsFactor, self.uCOSECClaimsAppliedFactor)

                # Industry Risk/Level of Confidence in Industry and Applied Factor
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddMIndustryRisk, self.uIndustryRisk)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMIndustryRiskFactor, self.uIndustryRiskAppliedFactor)

                # # Discovery (Extended Reporting) and Applied Factor
                self.BF.fncSelectElementFromDropdown(self.myDriver, self.AR.idddMDiscovery, self.uDiscovery)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMDiscoveryFactor, self.uDiscoveryAppliedFactor)

            except Exception as e52:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'AddCoverageModifiers'))
                self.fail(e52)

        def test_FL05_03_AddOtherRiskFactors(self):
            try:

                # Claims litigation history (severity) (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMClaimLitigationHistory, self.uClaimLitigationHistory)

                # Earnings consistency (0.75-4.00)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMEarningConsistency, self.uEarningConsistency)

                # Environmental issues (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMEnvironmentalIssues, self.uEnvironmentalIssues)

                # Insider trading activity (1.00-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMInsiderTradingActivity, self.uInsiderTradingActivity)

                # Labor relations (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMLaborRelations, self.uLaborRelations)

                # Major customers (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMMajorCustomers, self.uMajorCustomers)

                # Management ownership (0.80-1.25)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMManagementOwnership, self.uManagementOwnership)

                # Quality of external board members (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMQualityExtBrdMembers, self.uQualityExtBrdMembers)

                # Stability of workforce (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMStabilityofWorkforce, self.uStabilityofWorkforce)

                # Stock volatility (0.75-2.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMStockVolatility, self.uStockVolatility)

                # Terrorism risk discount (0.90-1.00)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMTerrorismRiskDiscount, self.uTerrorismRiskDiscount)

                # Corporate governance procedures(0.75 - 1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMCorpGovernanceProcedure, self.uCorpGovernanceProcedure)

                # Effected by recession (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMEffectedByRecession, self.uEffectedByRecession)

                # Financial solvency (0.75-2.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMFinancialSolvency, self.uFinancialSolvency)

                # Joint ventures/Limited partnerships/Significant subsidiary operations (incl. SVPs) (1.00-2.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMJointVentures, self.uJointVentures)

                # Liquidity (0.75-2.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMLiquidity, self.uLiquidity)

                # Management experience or stability (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMManagementStability, self.uManagementStability)

                # Other financial factors (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMOtherFinFactors, self.uOtherFinFactors)

                # Regulatory exposure/experience (0.90-2.00)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMRegulatoryExposure, self.uRegulatoryExposure)

                # Stock market sensitiviy (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMStockMrktSensitivity, self.uStockMrktSensitivity)

                # Takeover potential (0.80-1.50)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMTakeoverPotential, self.uTakeoverPotential)

                # Transaction Event (e.g., bankruptcy, credit downgrade) (1.00-2.00)
                self.BF.fncEnterTextboxValue(self.myDriver, self.AR.idtxtMTransactionEvent, self.uTransactionEvent)

            except Exception as e53:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'AddOtherRiskFactors'))
                self.fail(e53)

        def test_FL05_04_SaveModifiers(self):
            try:
                # Click Next to save UW Questions
                self.myDriver.find_element(By.ID, self.AR.idbtnOneShieldNext).click()
                time.sleep(2)

                # Verify if the record has been successfully created
                assert self.myDriver.find_element(By.ID, "ctl00__MainContent_ucMessages_lblInfoMsg").text == "Record has been saved"

            except Exception as e54:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'SaveModifiers'))
                self.fail(e54)

except Exception as e5:
    print('OneShield_Modifiers Script did not run successfully')
    print(e5)

