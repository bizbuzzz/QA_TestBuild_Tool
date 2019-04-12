#!/usr/bin/env python3



#Please place this file inside required project

import fileinput
import os
import urllib.request
import shutil

Path = os.getcwd()
count = 0
URL = 'https://console.firebase.google.com/m/mobilesdk/projects/599768896409/clients/android%3Acom.bizbuzzz.app/artifacts/2?param=%5B%22getArtifactRequest%22%2Cnull%2C%22android%3Acom.bizbuzzz.app%22%2C%222%22%2C%22599768896409%22%5D&authuser=2'
for pfile in os.walk(Path):
    for i in pfile[2]:
        if i == 'AndroidManifest.xml':
            with fileinput.FileInput(pfile[0]+"\\AndroidManifest.xml", inplace=True) as file:
                for line in file:
                    if "For production Build" in line:
                        print(line, end='')
                    else:
                        print(line.replace("\"AIzaSyAfjRvAYEoosdOioNz_VJli7UrYSbpvlic\"", "\"AIzaSyBTa01FnkrkCjybY0ViNBP2sUUaqwY9yQw\""), end='')
            print("FoundFile at:"+pfile[0]+"\\AndroidManifest.xml")
        elif i == 'BizBuzzzConstants.java':
            with fileinput.FileInput(pfile[0]+'\\BizBuzzzConstants.java', inplace=True) as file:
                for line in file:
                    if "For production Build" in line:
                        print(line, end='')
                    else:
                        print(line.replace("\"liveDatabase/liveDatabase\"", "\"qa_5july\""), end='')
            print("FoundFile at:"+pfile[0]+"\\BizBuzzzConstants.java")
        elif i == 'logback.xml':
            with fileinput.FileInput(pfile[0]+'\\logback.xml', inplace=True) as file:
                for line in file:
                    if "For production Build" in line:
                        print(line, end='')
                    else:
                        print(line.replace("\"ERROR\"",
                                       "\"DEBUG\""), end='')
            print("FoundFile at:"+pfile[0]+"\\logback.xml")
        # elif pfile == 'proguard-rules.pro':
        #     with fileinput.FileInput('proguard-rules.pro', inplace=True) as file:
        #         for line in file:
        #             print(line.replace("\"AIzaSyDg0n-_93lzmSCiDx0DG8gUlRa0pZD5JwM\"",
        #                                "\"AIzaSyBTa01FnkrkCjybY0ViNBP2sUUaqwY9yQw\""), end='')
        elif i == 'remote_config_defaults.xml':
            with fileinput.FileInput(pfile[0]+'\\remote_config_defaults.xml', inplace=True) as file:
                for line in file:
                    if "dev" in line:
                        print(line, end='')
                    else:
                        print(line.replace("e5krp",
                                       "qmkk3"), end='')
            print("FoundFile at:"+pfile[0]+"\\remote_config_defaults.xml")
        elif i == 'RestHelper.java':
            with fileinput.FileInput(pfile[0]+'\\RestHelper.java', inplace=True) as file:
                for line in file:
                    if "For production Build" in line:
                        print(line, end='')
                    else:
                        print(line.replace("\"https://qaserver-dot-bizbuzzzdevbed-4e5c6.appspot.com\"",
                                        "\"https://qaserver-dot-bizbuzzztestbed-8ba40.appspot.com\""), end='')
            print("FoundFile at:"+pfile[0]+"\\RestHelper.java")
        #elif i == 'google-services.json':
         #   with urllib.request.urlopen(URL) as response,open(pfile[0]+"\\google-services.json", 'wb') as out_file:
          #      shutil.copyfileobj(response, out_file)
           # print("FoundFile at:"+pfile[0]+"\\google-services.json")
        else:
            count=count+1


input('Task Completed!')

