import urllib2, threading, time
class Internet(object):
    def __init__(self):
        self.commonHosts = ('http://www.google.com',
                            'http://www.gnome.org',
                            'http://www.desdfsdfbian.org',
                            )
        self.results = Booleans()
        
    def connected(self):
        if self.results:
            print 'hello'
            self.results.clear()
            
        for url in self.commonHosts:
            CheckUrl(url, self.results).start()
            
        while len(self.results) != len(self.commonHosts):
            time.sleep(0.01)
            
        return self.results.true()
    
    
class Booleans(object):
    def __init__(self):
        self._booleans = []
        
    def addValue(self, b):
        self._booleans += [b]
        
    def clear(self):
        self._booleans = []
        
    def __len__(self):
        return len(self._booleans)
    
    def __eq__(self, other):
        return (self._booleans == other)
    
    def true(self):
        '''Return True if at least one value is True'''
        true = True
        for b in self._booleans:
            true = (true or b)
        return true
        
        
class CheckUrl(threading.Thread):
    def __init__(self, url, results):
        threading.Thread.__init__(self, name='CheckUrl')
        self.results = results
        self.url = url
        
    def _checkUrl(self, url):
        try:
            urllib2.urlopen(url)
            return True
        except:
            return False
        
    def run(self):
        self.results.addValue(self._checkUrl(self.url))
            
if __name__ == '__main__':
    net = Internet()
    if net.connected():
        print('We are connected to the internet!')
    else:
        print('Oh noes! No interwebs!')
