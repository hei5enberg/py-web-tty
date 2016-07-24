#!/usr/bin/python
# py-web-tty

import tornado.ioloop
import tornado.web
import tornado.httpserver
# from config import Config
import os

class DeviceHandler(tornado.web.RequestHandler):

    def get(self):
        # if not self.current_user:
        #     self.redirect("/login")
        self.render("devicesett.html", antenna_power="30", card_repeat_time=4)

    def post(self):
        # if not self.current_user:
        #     self.redirect("/login")
        #     return
        self.redirect("/device")

class Myapp(tornado.web.Application):

    def __init__(self):
        template_path=os.path.join(os.path.dirname(__file__), "templates")
        static_path=os.path.join(os.path.dirname(__file__), "static")
        handlers = [
            (r"/", DeviceHandler),
            (r"/device", DeviceHandler),
        ]
        tornado.web.Application.__init__(
            self, handlers, template_path=template_path, static_path=static_path, cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Myapp())
    http_server.listen(8880)
    tornado.ioloop.IOLoop.instance().start()
