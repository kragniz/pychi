#!/usr/bin/env python
import urllib2, threading
    
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
        true = False
        for b in self._booleans:
            if b:
                true = b
        return true
        
        
class CheckUrl(threading.Thread):
    def __init__(self, url, results, timeout=1, verbose=False):
        threading.Thread.__init__(self, name='CheckUrl')
        self.results = results
        self.url = url
        self.timeout = timeout
        self.verbose = verbose
        
    def _checkUrl(self, url):
        try:
            urllib2.urlopen(url, None, self.timeout)
            if self.verbose:
                print 'got', url
            return True
        except Exception, e:
            if self.verbose:
                print 'failed', url, 'because', e
            return False
        
    def run(self):
        self.results.addValue(self._checkUrl(self.url))
