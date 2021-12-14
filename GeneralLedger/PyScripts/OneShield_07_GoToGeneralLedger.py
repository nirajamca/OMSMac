from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, timedelta
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
                time.sleep(5)

                # Verify if the Reports section available
                self.assertEqual(self.myDriver.find_element_by_xpath(self.AR.xPathHeaderARGLTransactionReport).text, "GL transaction report")

                self.myDriver.close()

                # switch the handle back to main window
                self.myDriver.switch_to_window(main_window_handle)

            except Exception as e73:
                print(self.BF.fncCaptureScreenshot(self.myDriver, self.ScreenShotsDir, 'LaunchGLTransactionReportPage'))
                self.fail(e73)

except Exception as e7:
    print('OneShield Go To General Ledger script did not run successfully')
    print(e7)

