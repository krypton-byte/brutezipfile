from concurrent.futures.thread import ThreadPoolExecutor
from zipfile import ZipFile
import sys
def extract():
    zip=ZipFile(input("*.zip : "))
    wordlist = open(input("wordlist : "), "rb").read().splitlines()
    length=len(wordlist)
    for i in enumerate(wordlist):
        try:
            zip.extractall(pwd=i[1])
            sys.stdout.write("\rPassword ditemukan : %s                  \n"%i[1].decode())
            break
        except:
            sys.stdout.write("\rCracking : %s%s  percobaan: %s"%(round(100/(length/(i[0]+1)),1), '%',i[0]+1))
        sys.stdout.flush()
    print('\n')
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(extract)