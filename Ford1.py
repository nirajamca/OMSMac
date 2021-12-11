# Specify the location of test data file and the sheet name to read from
testDataLoc = "TestData.xlsx"
testDataSheet = "Ford1"

# Specify the location for adding screenshots on errors
ScreenShotsDir = 'C:\ScreenShots'

exec(open("SmokeTest.py").read())
