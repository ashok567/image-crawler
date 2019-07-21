import tornado.web
import tornado.ioloop
import os.path
import scraper

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    
class DataHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "application/json")
        url = self.get_body_argument("url")
        scraper.download_image(url)
        self.write({'response': "ok"})

    
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),'templates'),
    # static_path = os.path.join(os.path.dirname(__file__),'static'),
    debug=True
)


def make_app():
    return tornado.web.Application(
    [
        (r'/', MainHandler),
        (r'/data', DataHandler),
        (r'/(.*)', tornado.web.StaticFileHandler, {"path": ""}),
    ],**settings)


if __name__ == '__main__':
    print("Server is running at 9000")
    app = make_app()
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()
