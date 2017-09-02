import urllib2
import os

httpsPrefix = "https://storage.googleapis.com/"
gsPrefix = "gs://"

def download_gs_to_file(url, fileName):
    download_http_to_file(url.replace(gsPrefix, httpsPrefix), fileName)

def download_http_to_file(url, fileName):
    path=os.path.dirname(fileName)
    if not os.path.exists(path):
        os.makedirs(path)
    response = urllib2.urlopen(url)
    CHUNK = 16 * 1024
    with open(fileName, 'wb') as f:
        while True:
            chunk = response.read(CHUNK)
            if not chunk:
                break
            f.write(chunk)
    print ('download ......ok')
