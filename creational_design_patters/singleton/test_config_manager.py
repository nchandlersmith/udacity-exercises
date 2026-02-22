import pytest
from creational_design_patters.singleton.config_manager import ConfigManager


class TestConfigManager:
    def test_config_manager_singleton(self):
        config1 = ConfigManager()
        config2 = ConfigManager()
        assert config1 is config2

    def test_config_manager_modify_attribute(self):
        config = ConfigManager()
        config.set("key", "test_value")
        assert config._config["key"] == "test_value"

    def test_config_manager_access_attribute(self):
        config = ConfigManager()
        config._config["key"] = "other_value"
        assert config.get("key") == "other_value"

    def test_config_manager_get_nonexistent_key(self):
        config = ConfigManager()
        assert config.get("nonexistent_key") is None
        
    def test_config_manager_data_access_consistency(self):
        config1 = ConfigManager()
        config2 = ConfigManager()
        config1.set("shared_key", "shared_value")
        assert config2.get("shared_key") == "shared_value"
