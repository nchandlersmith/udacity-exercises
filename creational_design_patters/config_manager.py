"""
ConfigManager module for managing application configuration.
"""


class ConfigManager:
    """
    A ConfigManager class that implements the Singleton pattern.
    Ensures only one instance of the configuration manager exists.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance
