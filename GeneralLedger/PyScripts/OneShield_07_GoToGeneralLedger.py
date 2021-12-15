from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, timedelta
import xlrd
import locale
import time
import unittest
import HtmlTestRunner

print("OneShield Go To General Ledger Tab")
try:
    class FL07(unittest.TestCase):
        from CommonFunctions import BasicFunctions as BF
        import AccessorRepository as AR

        myDriver = myDriver
        ScreenShotsDir = ScreenShotsDir

        def test_FL07_01_GoToAnalyticReports(self):
            try:
                # Go to Analytic Reports Menu item in the left Panel
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathlnkAnalyticReports))).click()
                time.sleep(3)

                # Verify if the Reports section available
                self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathSectionHeaderARReports).text, "Reports")

            except Exception as e71:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'GoToAnalyticReports'))
                self.fail(e71)

        def test_FL07_02_ExpandGeneralReportsSection(self):
            try:
                # Click General link to expand General Reports tree
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathlnkARGeneral))).click()
                time.sleep(3)

                # Verify if the Reports section available
                self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathlnkARGLTransactionReport).text, "GL transaction report")

            except Exception as e72:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'ExpandGeneralReportsSection'))
                self.fail(e72)

        def test_FL07_03_LaunchGLTransactionReportPage(self):
            try:
                # Before launching new window create a handle to the current window
                main_window_handle = None
                while not main_window_handle:
                    main_window_handle = self.myDriver.current_window_handle

                # Click GL Transaction Report link
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathlnkARGLTransactionReport))).click()
                time.sleep(3)

                glreport_window_handle = None

                while not glreport_window_handle:
                    for handle in self.myDriver.window_handles:
                        if handle != main_window_handle:
                            glreport_window_handle = handle
                            break
                self.myDriver.switch_to_window(glreport_window_handle)
                time.sleep(2)

                # Verify if the Reports section available
                self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathHeaderARGLTransactionReport).text, "GL transaction report")

                # Create GL Report
                # Get today's date in the required format
                uTrToDate = date.today().strftime("%m/%d/%Y")

                uTrFromDate = date.today() + timedelta(-10)
                uTrFromDate = uTrFromDate.strftime("%m/%d/%Y")

                # Enter transaction from date
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathtxtARGLTransactionDateFrom))).clear()
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathtxtARGLTransactionDateFrom))).send_keys(uTrFromDate)
                time.sleep(3)

                # Enter transaction to date
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathtxtARGLTrasactionDateTo))).clear()
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathtxtARGLTrasactionDateTo))).send_keys(uTrToDate)
                time.sleep(3)

                # Select report type as Excel
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathrdoARGLReportFormatExcel))).click()
                time.sleep(1)

                # Click Run Report
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathbtnARGLRunReport))).click()
                time.sleep(3)

                # Verify if the report is generated successfully
                self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathlblARGLReportGenerated).text, 'Report has been generated, click on the View link to open it')
                self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathlnkARGLView).text, 'View')

                uHREF = WebDriverWait(self.myDriver, 10).until(EC.visibility_of_element_located((By.XPATH, self.AR.xPathlnkARGLView))).get_attribute('href')

                # Click View to download the General Ledger Report in Excel Format
                WebDriverWait(self.myDriver, 10).until(EC.element_to_be_clickable((By.XPATH, self.AR.xPathlnkARGLView))).click()
                time.sleep(3)

                print(uHREF)

                uGLTrReport = uHREF.split('=')[2]
                uGLTrReportLocal = 'C:\\Users\\niraj\\Downloads\\' + uGLTrReport

                # Create workbook object and capture the active sheet
                wb = xlrd.open_workbook(uGLTrReportLocal)

                # Designate the actual sheetname
                sheet = wb.sheet_by_name('Sheet1')
                locale.setlocale(locale.LC_ALL, 'English_United States.1252')

                # Get Final Adjustment Premium
                # uFinalPremium = sheet.cell(rowx=34, colx=1).value
                print(sheet.cell(rowx=5, colx=6).value)

                # self.myDriver.close()
                #
                # # switch the handle back to main window
                # self.myDriver.switch_to_window(main_window_handle)

            except Exception as e73:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'LaunchGLTransactionReportPage'))
                self.fail(e73)

except Exception as e7:
    print('OneShield Go To General Ledger script did not run successfully')
    print(e7)

