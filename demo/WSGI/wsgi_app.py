# wsgi 应用规范：参数固定为两个
# 1.environ：含有服务器环境变量的字典
# 2.start_response：可调用对象，该对象使用HTTP状态码和会返回给客户端的HTTP头；
# 有了wsgi 我们关心的就是如何从 environ 中拿到请求信息，然后构造 HTML ，通过 start_response() 发送 Header，最后返回Body
#
# Content-Type，内容类型，一般是指网页中存在的 Content-Type，用于定义网络文件的类型和网页的编码，
# 决定浏览器将以什么形式、什么编码读取这个文件，这就是经常看到一些 Asp 网页点击的结果却是下载到的一个文件或一张图片的原因。
def application(environ, start_response):
    start_response('200 OK', [("Content-Type", 'text/html')])
    return [b'<h1>hello wsgi!</h>']
