import tornado.ioloop
import tornado.web

from templates.modules import uimodules


class HomeScreenHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("HomeScreen.html")


settings = {
    "ui_modules": uimodules,
    "template_path": "templates/",
    "debug": True
}


def make_app():
    return tornado.web.Application([
        (r"/", HomeScreenHandler),

    ], ** settings

    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    print("starting server")
    tornado.ioloop.IOLoop.current().start()
