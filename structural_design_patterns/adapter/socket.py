"""The example for the course is rather silly,so I decided to implement a more realistic example."""


class Plug:
    def __init__(self, voltage):
        self._voltage = voltage

    @property
    def voltage(self):
        return self._voltage

    def connect(self):
        return self._voltage


class USPlug(Plug):
    def __init__(self):
        super().__init__(110)


class ToEuropeanSocketAdapter(Plug):
    def __init__(self, plug: USPlug):
        super().__init__(220)
        self._us_plug = plug
        
    def connect(self):
        return self._us_plug.connect() * 2
        


class EuropeanSocket():
    """A socket that only accepts plugs with 220V. 
    This is the target interface that we want to build to."""

    def plug_in(self, plug: Plug):
        if plug.connect() == 220:
            return "success"
        return "incompatible"
