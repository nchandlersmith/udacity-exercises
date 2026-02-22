import pytest
from creational_design_patters.config_manager import ConfigManager


class TestConfigManager:
    def test_config_manager_singleton(self):
        config1 = ConfigManager()
        config2 = ConfigManager()
        assert config1 is config2
