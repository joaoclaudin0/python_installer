from urllib.request import urlretrieve as down
import os,sys
import platform
print(os.getlogin())


#Percent Download
def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))

if platform.architecture()[0].replace("bit",'') == "64":
    iso  = "your_download_link_x64"
    name = 'Executable_here.exe'
else:
    iso  = "your_download_link_x64"
    name = 'Executable_here.exe'

down(iso,f'C:\\Users\\{os.getlogin()}\\Downloads\\{name}',reporthook)
os.system(f"start C:\\Users\\{os.getlogin()}\\Downloads\\{name}")