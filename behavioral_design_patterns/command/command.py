from abc import ABC, abstractmethod
import time


class Light():

    def turn_on(self):
        return "light turned on"

    def turn_off(self):
        return "light turned off"


class Fan():

    def turn_on(self):
        return "fan turned on"

    def turn_off(self):
        return "fan turned off"


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):

    def __init__(self):
        self._light = Light()

    def execute(self):
        return self._light.turn_on()


class LightOffCommand(Command):

    def __init__(self):
        self._light = Light()

    def execute(self):
        return self._light.turn_off()


class FanOnCommand(Command):

    def __init__(self):
        self._fan = Fan()

    def execute(self):
        return self._fan.turn_on()


class FanOffCommand(Command):

    def __init__(self):
        self._fan = Fan()

    def execute(self):
        return self._fan.turn_off()


class RemoteControl():

    def execute(self, receiver_function):
        return receiver_function()


if "__main__" == __name__:
    remote = RemoteControl()
    print(remote.execute(LightOnCommand().execute))
    time.sleep(1)
    print()
    print(remote.execute(LightOffCommand().execute))
    print()
    time.sleep(2)
    print()
    print(remote.execute(FanOnCommand().execute))
    print()
    time.sleep(1)
    print(remote.execute(FanOffCommand().execute))
