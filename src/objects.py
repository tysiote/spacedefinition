class SpaceObject(object):
    raw_params = {}
    mass = 0
    radius = 0
    parent = None
    children = []
    color = ''

    def __init__(self, params):
        self.raw_params = params
