import tornado.web
import tornado.ioloop
import os.path
import scraper

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    
    def post(self):
        self.set_header("Content-Type", "text/plain")
        url = self.get_body_argument("url")
        print(url)
        scraper.download_image(url)
        self.redirect("/fetch")

class FetchHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("success.html")

    
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),'templates'),
    static_path = os.path.join(os.path.dirname(__file__),'static'),
    debug=True
)


def make_app():
    return tornado.web.Application(
    [
        (r'/', MainHandler),
        (r'/fetch', FetchHandler)
    ],**settings)


if __name__ == '__main__':
    print("Server is running at 9000")
    app = make_app()
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()
