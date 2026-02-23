from socket import EuropeanPlug, USPlug, EuropeanSocket, USPlugAdapter
import pytest


class TestSocket:
    def test_european_plug(self):
        plug = EuropeanPlug()
        assert plug.connect() == 220

    def test_us_plug(self):
        plug = USPlug()
        assert plug.connect() == 110

    def test_socket_with_european_plug(self):
        socket = EuropeanSocket()
        plug = EuropeanPlug()
        assert socket.plug_in(plug) == "success"

    def test_socket_with_us_plug(self):
        socket = EuropeanSocket()
        plug = USPlug()
        assert socket.plug_in(plug) == "incompatible"

    def test_voltage_adapter(self):
        socket = EuropeanSocket()
        plug = USPlug()
        adapter = USPlugAdapter(plug)
        assert socket.plug_in(adapter) == "success"
