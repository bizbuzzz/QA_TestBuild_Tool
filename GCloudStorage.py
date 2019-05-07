
import argparse
import datetime
import pprint
from google.cloud import storage
import os
import ntpath
import json

import firebase_admin
from firebase_admin import credentials, firestore, storage


def json_file(urls, jfolders):
    with open('BizPhotosInputData.json', 'r+') as jsonfile:
        data = json.load(jsonfile)
        for obj in data['7l9teHCEPxeJaGWjM4fEo3ugaar2']:
            if obj['Section'] == jfolders:
                if obj['Image'] == ["image1","image2"]:
                    del obj['Image']
                    obj['Image'] = [] + [urls]
                else:
                    obj['Image'] += [urls]
        jsonfile.seek(0)
        json.dump(data, jsonfile, indent=4)
        jsonfile.truncate()


def upload(file):
    b_filename = ntpath.basename(file)
    folder = os.path.dirname(file).replace("RawBizPhotos/", "")
    jfolder = os.path.basename(folder)
    print(folder)
    print(b_filename)
    blob = bucket.blob('AppStaging/liveDatabase/India/v1_0/users/'+folder+'/'+b_filename)
    outfile = file
    # storages = storage.ref('AppStaging/iveDatabase/India/v1_0/users/'+'7l9teHCEPxeJaGWjM4fEo3ugaar2')
    # storages.put(file)
    with open(outfile, 'rb') as my_file:
        blob.upload_from_file(my_file, content_type='image/jpg')
    publiurl = blob.public_url
    json_file(publiurl, jfolder)


def filelist(source):
    global matches, dirnames
    matches = []
    dirnames = []
    for root, dirname, filenames in os.walk(source):
        for filename in filenames:
            if filename.endswith(('.jpge','.jpg')):
                matches.append(os.path.join(root, filename))
                dirnames.append(dirname)
    return matches, dirnames


def main():
    path = os.getcwd()
    filelist("RawBizPhotos")
    for objects in matches:
        upload(objects)


if __name__ == '__main__':
    cred = credentials.Certificate('bizbuzzztestbed-8ba40-firebase-adminsdk.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'bizbuzzztestbed-8ba40.appspot.com'
    })
    db = firestore.client()
    bucket = storage.bucket()
    main()