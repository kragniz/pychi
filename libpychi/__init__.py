import time
import data
from checkUrl import Booleans, CheckUrl

class Internet(object):
    def __init__(self, customHosts=None, timeout=1, verbose=False):
        self.commonHosts = ('http://www.google.com',
                            'http://www.gnome.org',
                            'http://www.debian.org',
                            'http://www.xkcd.com'
                            )
        if customHosts:
            self.commonHosts = customHosts
            
        self.results = Booleans()
        self.timeout = timeout
        self.verbose = verbose
        
    def connected(self):
        if self.results:
            self.results.clear()
            
        for url in self.commonHosts:
            CheckUrl(url, self.results, timeout=self.timeout, verbose=self.verbose).start()
            
        while len(self.results) != len(self.commonHosts):
            time.sleep(0.01)
            
        return self.results.true()
    
if __name__ == '__main__':
    '''self tests'''
    net = Internet()
    if net.connected():
        print('We are connected to the internet!')
    else:
        print('Oh noes! No interwebs!')
