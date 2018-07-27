from src.objects import SpaceObject


class ObjectController(object):
    objects = {}
    app = None
    next_id = 0

    def __init__(self, app):
        self.app = app

    def create_object(self, params):
        if "id" in params.keys():
            self.objects[params["id"]] = SpaceObject(params)
        else:
            self.objects[self.next_id] = SpaceObject(params)
            self.next_id += 1

    def get(self, as_list=False):
        if as_list:
            return [obj for obj in self.objects.values()]
        return self.objects
