import tornado.web
import tornado.ioloop
import os.path

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),'templates'),
    static_path = os.path.join(os.path.dirname(__file__),'static'),
    debug=True
)


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler)
    ],**settings)


if __name__ == '__main__':
    print("Server is running at 9000")
    app = make_app()
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()