from vector import vector, adjust_up


class sphere([['pos', 'color', 'trail_color'],
       ['axis', 'size', 'up'],
       ['visible', 'opacity','shininess', 'emissive',
        'make_trail', 'trail_type', 'interval',
        'retain', 'trail_color', 'trail_radius', 'texture', 'pickable'],
       ['red', 'green', 'blue','length', 'width', 'height', 'radius']]):
    def __init__(self, **args):
        args['_default_size'] = vector(2,2,2)
        args['_objName'] = "sphere"
        super(sphere, self).setup(args)
        self._sizing = False # no axis/size connection

    @property
    def radius(self):
        return self._size.y/2
    @radius.setter
    def radius(self,value):
        d = 2*value
        self.size = vector(d,d,d) # size will call addattr

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,value):
        if not isinstance(value, vector): raise TypeError('size must be a vector')
        self._size = value
        if not self._constructing:
            self.addattr('size') # changing a sphere size should not affect axis

    @property
    def axis(self):
        return self._axis
    @axis.setter
    def axis(self,value): # changing a sphere axis should not affect size
        self._save_oldaxis = adjust_up(self._axis, value, self._up, self._save_oldaxis) # this sets self._axis and self._up
        self._axis.value = value
        if not self._constructing:
            # must update both axis and up when either is changed
            self.addattr('axis')
            self.addattr('up')
