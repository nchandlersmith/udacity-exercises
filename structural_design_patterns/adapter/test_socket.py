from socket import USPlug, EuropeanSocket, ToEuropeanSocketAdapter
import pytest


class TestSocket:

    def test_us_plug(self):
        plug = USPlug()
        assert plug.connect() == 110

    def test_socket_with_us_plug(self):
        socket = EuropeanSocket()
        plug = USPlug()
        assert socket.plug_in(plug) == "incompatible"

    def test_voltage_adapter(self):
        socket = EuropeanSocket()
        adapter = ToEuropeanSocketAdapter(USPlug())
        assert socket.plug_in(adapter) == "success"
