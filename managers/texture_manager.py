
from typing import Dict
from pathlib import Path
import json
from loguru import logger
from pygame import Surface
import pygame

class TextureManager(object):

    # Class variables
    managers = {}
    
    # Class methonds
    @classmethod
    def create_manager(cls, name: str, configuration_path: str):
        
        mgr = cls(configuration_path)
        cls.managers[name] = mgr

        return mgr

    @classmethod
    def get_manager(cls, name: str):
        
        logger.debug(f"Looking for Texture manager: {name}")
        if name in cls.managers.keys():
            return cls.managers[name]
        else:
            raise ValueError(f"Texture Manager '{name}' not found!")
            
    def __init__(self, configuration_path: str):
        self.textures = {}
        self.configuration_path = Path(configuration_path)

        if not self.configuration_path.exists():
            raise ValueError(f"No sample manager configuration found at {self.configuration_path}")

        try:
            with open(self.configuration_path, "r") as f:
                configuration = json.load(f)
            assert len(configuration.keys()) > 0
        except Exception as e:
            raise ValueError(f"Invalid configuration in {self.configuration_path}: {e}")

        for name, path in configuration.items():
            self.textures[name] = pygame.image.load(str(path))

    def get_texture(self, name: str, convert_alpha: bool = True) -> Surface:

        if name not in self.textures.keys():
            raise ValueError(f"Sample {name} in not defined in configuration! Only {list(self.textures.keys())}")

        img = self.textures[name]
        if convert_alpha:
            img = img.convert_alpha()
        
        return img

    def get_mask(self, name: str) -> Surface:

        if name not in self.textures.keys():
            raise ValueError(f"Sample {name} in not defined in configuration! Only {list(self.textures.keys())}")

        img = pygame.mask.from_surface(self.textures[name], 50)
        return img
