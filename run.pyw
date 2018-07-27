from src.graphics import GraphicController
from src.object_controller import ObjectController

VERSION = "DEV.1.0"


class App(object):
    objects = None
    graphics = None
    version = VERSION

    def __init__(self):
        self.objects = ObjectController(self)
        self.graphics = GraphicController(self)


if __name__ == "__main__":
    app = App()
