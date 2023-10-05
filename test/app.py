# Google OAuth 2.0 and OAuth consent screen

# authetication to google api services
# create oauth client secret file

# https://console.cloud.google.com/

# pip install pydrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1mT1alkWJ-akPnPyB9T7vtumNutwqRK0S'

file_list = drive.ListFile({'q': "'%s' in parents and trashed=false"%(folder)}).GetList()

took = False
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
  
  file_id = file1['id']
  print(file_id)
  print("---")
  
