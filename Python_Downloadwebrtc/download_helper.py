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


if __name__ == "__main__":
    f = open("./grep_download_error.log")
    line = f.readline()
    while line:
        #print line,
        line = f.readline()
        if not line:
            break
        arr = line.split()
        url = arr[5]
        addr = arr[7]
        fulladdr = "WebRTC_BuildScripts2/webrtc-build-scripts/android/webrtc/" + addr[0:-1]
        print(url)
        print(fulladdr)
        download_gs_to_file(url, fulladdr)
    f.close()
    print ('This is main of module "hello.py"')
    #download_gs_to_file('gs://chromium-android-tools/play-services/10.2.0/31843001b7ce94fbdf71f2a9db76b28548a795fa', '/tmp/tangpeng/f1')
