class Internet(object):
    def __init__(self):
        commonHosts = ('http://www.google.com',
                       'http://www.gnome.org',
                       'http://www.debian.org')
    
    def _checkHost(self, host):
        pass
    
    def connected(self):
        return False
    
if __name__ == '__main__':
    net = Internet()
    if net.connected():
        print('we are connected to the internet!')
