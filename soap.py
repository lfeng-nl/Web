## 基于python2 ，选择包 spyne
## 参考文档：http://spyne.io/docs/2.10/manual/02_helloworld.html
## 参考文档：https://blog.csdn.net/fengqingting2/article/details/50501866
## 参考文档：https://github.com/arskom/spyne/tree/master/examples
from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.protocol.soap import Soap11 

class HelloWorldService(ServiceBase):
    @srpc(String, UnsignedInteger, _returns=Iterable(String))
    def say_hello(name, times):
        for i in xrange(times):
            yield 'Hello, %s' % name

if __name__ == "__main__":
    #//logging.basicConfig(level=logging.DEBUG)
    #logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    app = Application([HelloWorldService], 'spyne.examples.hello.http',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )
    wsgi_app = WsgiApplication(app)
    server = make_server('127.0.0.1', 7789, wsgi_app)

    print "listening to http://127.0.0.1:7789"
    print "wsdl is at: http://localhost:7789/?wsdl"

    server.serve_forever()