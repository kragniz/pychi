import urllib2
class Internet(object):
    def __init__(self):
        self.commonHosts = ('http://www.google.com',
                            'http://www.gnome.org',
                            'http://www.debian.org')
    
    def _checkHost(self, url):
        try:
            urllib2.urlopen(url)
            return True
        except:
            return False
    
    def connected(self):
        isConnected = True
        for url in self.commonHosts:
            isConnected = (self._checkHost(url) and isConnected)
        return isConnected
    
if __name__ == '__main__':
    net = Internet()
    if net.connected():
        print('We are connected to the internet!')
    else:
        print('Oh noes! No interwebs!')
