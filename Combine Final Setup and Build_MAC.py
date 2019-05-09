
import sys
import subprocess
from subprocess import Popen , PIPE
from tkinter import filedialog
import os
import fnmatch
from shutil import copyfile

import fileinput
import urllib.request
import shutil
from shutil import copyfile


def generate_Signed_APK():
    paths = os.getcwd()
    jks = ''
    apk = ''
    apkpath = ''
    global jkspath

    storePassword = "\'B$Uwqtp9zr~zTeSt\'"
    keyAlias = "\'Testbedkey\'"
    keyPassword = "\'B$Uwqtp9zr~zTeSt\'"
    # folder_name = filedialog.askdirectory()

    with open('LOGGER.log', 'wb') as f:
        process = subprocess.Popen([r"./gradlew", "assembleRelease"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(process.stdout.readline, b''):  # replace '' with b'' for Python 3
            sys.stdout.write(str(line) + "\n")
            f.write(line)

        for root, dirs, files in os.walk(paths):
            for file in files:
                if file == "app-release-unsigned.apk":
                    apk = os.path.join(root, file)
                    apkpath = root
                    print(file + " Found at " + root)
                    if not os.path.isdir('Testfile'):
                        os.mkdir(paths + '/Testfile')
                        copyfile(apk, paths + '/Testfile/app-release-unsigned.apk')
                elif fnmatch.fnmatch(file, "testbed-release-keystore"):
                    print(file + " Found at " + root)
                    jks = os.path.join(root, file)
                    jkspath = root
                    apks = paths + '/Testfile/app-release-unsigned.apk'
                    jarsign = 'jarsigner -verbose -keystore ' + jks + ' -storepass ' + storePassword + ' -keypass ' + keyPassword + ' ' + apks + ' ' + keyAlias
                    folders = os.path.basename(paths)
                    signedapk = folders.replace('bizBuzzzNewUXUI-', '')
                    zipalign = r'zipalign -v 4 ' + apks + ' ' + paths + '/Testfile/' + signedapk + '.apk'

        print("========================================JARSIGN===========================================")
        process1 = subprocess.Popen(jarsign, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        for line in iter(process1.stdout.readline, b''):
            sys.stdout.write(str(line) + "\n")
            f.write(line)

        # Place zipalign in Android/SDk/build tools and set Path for it in ~/.bash_profile; Restart You Mac
        print("========================================Zipalign===========================================")
        process2 = subprocess.Popen(zipalign, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        for line in iter(process2.stdout.readline, b''):
            sys.stdout.write(str(line) + "\n")
            f.write(line)

    print('Task Completed! Signed APK is in Test Folder')


# !/usr/bin/env python3
# Please place this file inside required project

def setup_for_Build():
    Path = os.getcwd()
    count = 0
    URL = 'https://console.firebase.google.com/m/mobilesdk/projects/599768896409/clients/android%3Acom.bizbuzzz.app/artifacts/2?param=%5B%22getArtifactRequest%22%2Cnull%2C%22android%3Acom.bizbuzzz.app%22%2C%222%22%2C%22599768896409%22%5D&authuser=2'
    for pfile in os.walk(Path):
        for i in pfile[2]:
            if i == 'AndroidManifest.xml':
                with fileinput.FileInput(pfile[0] + "/AndroidManifest.xml", inplace=True) as file:
                    for line in file:
                        if "For production Build" in line:
                            print(line, end='')
                        else:
                            print(line.replace("\"AIzaSyAfjRvAYEoosdOioNz_VJli7UrYSbpvlic\"",
                                               "\"AIzaSyBTa01FnkrkCjybY0ViNBP2sUUaqwY9yQw\""), end='')
                print("FoundFile at:" + pfile[0] + "/AndroidManifest.xml")
            elif i == 'BizBuzzzConstants.java':
                with fileinput.FileInput(pfile[0] + '/BizBuzzzConstants.java', inplace=True) as file:
                    for line in file:
                        if "For production Build" in line:
                            print(line, end='')
                        else:
                            print(line.replace("\"liveDatabase/liveDatabase\"", "\"qa_5july\""), end='')
                print("FoundFile at:" + pfile[0] + "/BizBuzzzConstants.java")
            elif i == 'logback.xml':
                with fileinput.FileInput(pfile[0] + '/logback.xml', inplace=True) as file:
                    for line in file:
                        if "For production Build" in line:
                            print(line, end='')
                        elif "LICENSE" in line:
                            print(line, end='')
                        elif "Create" in line:
                            print(line, end='')
                        elif "ERROR" in line:
                            print(line.replace("\"ERROR\"", "\"DEBUG\""), end='')
                        elif "<!--" in line:
                            print(line.replace("<!--", " ").replace("-->", " "), end='')
                        else:
                            print(line, end='')
                print("FoundFile at:" + pfile[0] + "/logback.xml")
            # elif pfile == 'proguard-rules.pro':
            #     with fileinput.FileInput('proguard-rules.pro', inplace=True) as file:
            #         for line in file:
            #             print(line.replace("\"AIzaSyDg0n-_93lzmSCiDx0DG8gUlRa0pZD5JwM\"",
            #                                "\"AIzaSyBTa01FnkrkCjybY0ViNBP2sUUaqwY9yQw\""), end='')
            elif i == 'remote_config_defaults.xml':
                with fileinput.FileInput(pfile[0] + '/remote_config_defaults.xml', inplace=True) as file:
                    for line in file:
                        if "dev" in line:
                            print(line, end='')
                        else:
                            print(line.replace("e5krp",
                                               "qmkk3"), end='')
                print("FoundFile at:" + pfile[0] + "/remote_config_defaults.xml")
            elif i == 'RestHelper.java':
                with fileinput.FileInput(pfile[0] + '/RestHelper.java', inplace=True) as file:
                    for line in file:
                        if "For production Build" in line:
                            print(line, end='')
                        else:
                            print(line.replace("\"https://bizbuzzzdevbed-4e5c6.appspot.com\"",
                                               "\"https://qaserver-dot-bizbuzzztestbed-8ba40.appspot.com\""), end='')
                print("FoundFile at:" + pfile[0] + "/RestHelper.java")
            elif i == 'google-services.json':
                if "/app/" in pfile[0]:
                    copyfile(os.getcwd() + "/google-services.json", pfile[0] + "/google-services.json")
                    print("FoundFile at:" + pfile[0] + "/google-services.json")
            else:
                count = count + 1

    input('Setup for Build Task Completed!')
    main()


def main():
    print("==============================================================================================================================================================")
    inpu = input("Choose Your Option:\n1.)Setup_for_Build\n2.)Generate_Signed_APK\n")

    if inpu == '1':
        setup_for_Build()
    elif inpu == '2':
        generate_Signed_APK()
    else:
        print("Wrong Option")
        main()


if __name__ == '__main__':
    main()



