#opens URL and saves the file as html

import urllib.request
u = urllib.request.urlopen('https://docs.python.org/3/howto/urllib2.html')
localFile = open('file.html', 'wb')
localFile.write(u.read())
localFile.close()
