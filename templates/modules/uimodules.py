import os

import tornado.web
from constants import *


class SideBar(tornado.web.UIModule):
    def embedded_css(self):
        return self.render_string(
            os.path.join(SIDEBAR_LOCATION, "sidebar-module.css"),
            height="15%"
        )

    def embedded_javascript(self):
        return self.render_string(
            os.path.join(SIDEBAR_LOCATION, "sidebar-module.js")
        )

    def render(self):
        return self.render_string(
            os.path.join(SIDEBAR_LOCATION, "sidebar-module.html")
        )

