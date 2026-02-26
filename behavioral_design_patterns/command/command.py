from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def execute(self):
        return "light turned on"


class LightOffCommand(Command):
    def execute(self):
        return "light turned off"


class FanOnCommand(Command):
    def execute(self):
        return "fan turned on"


class FanOffCommand(Command):
    def execute(self):
        return "fan turned off"


class LightReceiver():

    def __init__(self):
        self._light_on_command = LightOnCommand()
        self._light_off_command = LightOffCommand()

    def turn_on(self):
        return self._light_on_command.execute()

    def turn_off(self):
        return self._light_off_command.execute()


class FanReceiver():

    def __init__(self):
        self._fan_on_command = FanOnCommand()
        self._fan_off_command = FanOffCommand()

    def turn_on(self):
        return self._fan_on_command.execute()

    def turn_off(self):
        return self._fan_off_command.execute()


class RemoteControl():

    def execute(self, receiver_function):
        return receiver_function()
