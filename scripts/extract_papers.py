# Downloads all files from http://www.the-blockchain.com/blockchain-news-research-library/ and creates a library.yml file in _data.
# Be careful as this erases resets all data and files for the library!
# Sometimes filenames have some weird characters in them or it's simply difficult to decode them correctly
# I used some nasty workarounds for those, but I think it all works alright. The Digix paper includes a zero width space, which I manually removed.
# Author: Leon Weber

import sys
import urllib
import urllib2
from lxml import html
import os
import glob
from pyquery import PyQuery
from hurry.filesize import size

reload(sys)
sys.setdefaultencoding("utf-8")

fileYml = '../_data/library.yml'
fileDir = '../assets/pdf/library/'
url = 'http://www.the-blockchain.com/docs/'
listUrl = url + 'index.php'
site = html.fromstring(urllib.urlopen(listUrl).read())
pq = PyQuery(site)

def download_file(url):
    file_name = url.split('/')[-1]
    file_name = file_name.replace(u'\u200b', '')
    url = url.replace(u'\u200b', '%E2%80%8B')
    url = url.replace(' ', '%20')
    url = url.replace("'", '%E2%80%99')
    u = urllib2.urlopen(url)
    f = open(fileDir + file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,
    f.close()
    return file_size

if not os.path.exists(fileDir):
    os.makedirs(fileDir)
else:
	files = glob.glob(fileDir + "*")
	for f in files:
		os.remove(f)

rows = pq('td.thumbtext')

with open(fileYml, 'w') as f:
    for row in rows:
        filename = row.find('h2').find('a').attrib['href']
        filesize = download_file(url + filename.replace(u'\u2019', "'"))
        filedate = row.find('p').text.strip()

        print "\nFilesize: " + size(filesize)
        print "Filedate: " + filedate.encode('utf-8')
        print "\n"

        f.write('- title: ' + filename.replace('.pdf', '').replace(u'\u200b', '') + '\n')
        f.write('  date: ' + filedate + '\n')
        f.write('  size: ' + size(filesize) + '\n')
        f.write('  file: ' + filename.replace(u'\u200b', '') + '\n')
        f.write('  desc:\n')
        f.write('  authors:\n')
        f.write('  organization:\n')
