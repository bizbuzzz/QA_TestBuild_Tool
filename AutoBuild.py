import sys
import subprocess
from subprocess import Popen , PIPE
from tkinter import filedialog
import os
import fnmatch
from shutil import copyfile

paths = os.getcwd()
jks=''
apk=''
apkpath = ''
global jkspath

storePassword = 'B$Uwqtp9zr~zTeSt'
keyAlias = 'Testbedkey'
keyPassword = 'B$Uwqtp9zr~zTeSt'
# folder_name = filedialog.askdirectory()

with open('LOGGER.log', 'wb') as f:
    process = subprocess.Popen([r"gradlew","assembleRelease"], stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    for line in iter(process.stdout.readline, b''):
        sys.stdout.write(str(line)+"\n")
        f.write(line)

    for root, dirs, files in os.walk(paths):
        for file in files:
            if file == "app-release-unsigned.apk":
                apk = os.path.join(root, file)
                apkpath = root
                print(file + " Found at " + root)
                if not os.path.isdir('Testfile'):
                    os.mkdir(paths + '\\Testfile')
                    copyfile(apk, paths + '\\Testfile\\app-release-unsigned.apk')
            elif fnmatch.fnmatch(file, "testbed-release-keystore"):
                print(file+" Found at "+root)
                jks = os.path.join(root, file)
                jkspath = root
                apks = paths + '\\Testfile\\app-release-unsigned.apk'
                jarsign = 'jarsigner -verbose -keystore ' + jks + ' -storepass ' + storePassword + ' -keypass ' + keyPassword + ' ' + apks + ' ' + keyAlias
                folders = os.path.basename(paths)
                signedapk = folders.replace('bizBuzzzNewUXUI-','')
                zipalign = r'zipalign -v 4 ' + apks + ' ' + paths+'\\Testfile\\'+signedapk+'.apk'

    print("========================================JARSIGN===========================================")
    process1 = subprocess.Popen(jarsign, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, shell=True)
    for line in iter(process1.stdout.readline, b''):
        sys.stdout.write(str(line) + "\n")
        f.write(line)

    print("========================================Zipalign===========================================")
    process2 = subprocess.Popen(zipalign, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    for line in iter(process2.stdout.readline, b''):
        sys.stdout.write(str(line) + "\n")
        f.write(line)
    print("===============Thank--YOU=================")
    print("Find Your Files in Test Folder")







