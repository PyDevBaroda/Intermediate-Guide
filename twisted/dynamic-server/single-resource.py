from twisted.internet import reactor
from twisted.web.server import Site #For listening server port to the HTTP protocol implementation
from twisted.web.resource import Resource #For representing a page
import time

class ClockPage(Resource):
    isLeaf = True #if it is true then ClockPage will not have any child resource
    def render_GET(self, request): #Using GET method to bind to request
        return "<html><body>%s</body></html>" % (time.ctime(),)

resource = ClockPage()  #resourse object is defined
factory = Site(resource) #create an instance of the Site
reactor.listenTCP(8881, factory) #bind it to a port
print 'Server running on port 8881 and ip 0.0.0.0'
reactor.run() #start server
