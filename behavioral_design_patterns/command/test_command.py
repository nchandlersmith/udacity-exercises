from command import LightOnCommand, LightOffCommand, FanOnCommand, FanOffCommand, Light, Fan, RemoteControl


class TestCommand:
    def test_light_on_turns_light_on(self):
        command = LightOnCommand()
        result = command.execute()
        assert result == "light turned on"

    def test_light_off_turns_light_off(self):
        command = LightOffCommand()
        result = command.execute()
        assert result == "light turned off"

    def test_fan_on_turns_fan_on(self):
        command = FanOnCommand()
        result = command.execute()
        assert result == "fan turned on"

    def test_fan_off_turns_fan_off(self):
        command = FanOffCommand()
        result = command.execute()
        assert result == "fan turned off"

    def test_light_receiver_turns_on_light(self):
        receiver = Light()
        result = receiver.turn_on()
        assert result == "light turned on"

    def test_light_receiver_turns_off_light(self):
        receiver = Light()
        result = receiver.turn_off()
        assert result == "light turned off"

    def test_fan_receiver_turns_on_fan(self):
        receiver = Fan()
        result = receiver.turn_on()
        assert result == "fan turned on"

    def test_fan_receiver_turns_off_fan(self):
        receiver = Fan()
        result = receiver.turn_off()
        assert result == "fan turned off"

    def test_remote_control_turns_on_light(self):
        remote = RemoteControl()
        result = remote.execute(Light().turn_on)
        assert isinstance(result, str)
        assert result.strip() != ""
