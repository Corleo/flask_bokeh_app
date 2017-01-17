from tornado.ioloop import IOLoop

from bokeh.application import Application
from bokeh.application.handlers import ScriptHandler, FunctionHandler
from bokeh.server.server import Server

from bokeh_scripts.slider_func import _slider_func

def _bokeh_init():
    io_loop = IOLoop.current()

    server = Server(
        {
            '/_func':    Application(FunctionHandler(_slider_func)),
            '/_sliders': Application(ScriptHandler(filename='bokeh_scripts/sliders.py')),
            '/_fourier': Application(ScriptHandler(filename='bokeh_scripts/fourier_animated.py'))
        },
        io_loop=io_loop,
        allow_websocket_origin=["localhost:8080"]
    )
    server.start()
    io_loop.start()


if __name__ == '__main__':
    _bokeh_init()
