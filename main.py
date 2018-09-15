import tornado.ioloop
import tornado.web


class HomeScreenHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("HomeScreen.html")



def make_app():
    return tornado.web.Application([
        (r"/", HomeScreenHandler),

    ], template_path="templates/"
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
