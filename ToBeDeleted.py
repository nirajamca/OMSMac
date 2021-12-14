# import xlrd
#
# wb = xlrd.open_workbook("C:\\Users\\niraj\\PycharmProjects\\Falcon\\TestData.xlsx")
#
# sheet = wb.sheet_by_name('Test1')
#
# print(sheet.cell(rowx=3, colx=32).value)

# from CommonFunctions import BasicFunctions as BF
#
# print(BF.fncGetValues('TestData.xlsx', 'Test1', 'PyScripts\OneShield_UWQuestions.py'))



# sheets = read_excel('State List of Range states vs Non Range states.xlsx', sheet_name=['Sheet1'])

# import openpyxl
# loc = 'State List of Range states vs Non Range states.xlsx'
# wb = openpyxl.load_workbook(loc)
# sheet = wb['Sheet1']
#
# uState = 'Massachusetts'
from CommonFunctions import BasicFunctions as BF

# uHREF = 'https://qa2.oms.oneshield.com/blob?fn=qnaconskff31293701.xlsm'

# def fncGetFinalPremiumFromRater(uHREF):
#     import xlrd
#     import locale
#
#     uRaterFile = uHREF.split('=')[1]
#     uRaterFileLocal = 'C:\\Users\\niraj\\Downloads\\' + uRaterFile
#
#     # Create workbook object and capture the active sheet
#     wb = xlrd.open_workbook(uRaterFileLocal)
#
#     # Designate the actual sheetname
#     sheet = wb.sheet_by_name('XS Final Premium Calculation')
#
#     uFinalPremium = sheet.cell(rowx=34, colx=1).value
#
#     locale.setlocale( locale.LC_ALL, 'English_United States.1252' )
#
#     return locale.currency( uFinalPremium, grouping = True )




import CommonFunctions.OneShieldFunctions as OSF
# fncCheckIfFileExists('GLBaseFile.xlsx')
# OSF.fncAddDataToGLBaseFile('GLBaseFile.xlsx','Commission', '50.00')
OSF.fncAddDataToGLBaseFile('GLBaseFile.xlsx','ProcessingFee', '250.00')
