from twisted.web.server import Site  #For listening server port to the HTTP protocol implementation
from twisted.web.static import File  #For a static resource
from twisted.internet import reactor #reactor drives the whole process

resource = File('./tmp') #nstance of the File resource
site_factory = Site(resource) #create an instance of the Site
reactor.listenTCP(8880, site_factory) #run factory to a TCP port
print 'Server running on port 8880 and ip 0.0.0.0'
reactor.run() #start server

