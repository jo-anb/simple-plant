"""Constants for simple_plant_extended."""

from logging import Logger, getLogger

from homeassistant.const import Platform

STORAGE_KEY = "simple_plant_extended_data"

LOGGER: Logger = getLogger(__package__)

DOMAIN = "simple_plant_extended"

STORAGE_DIR = "simple_plant_extended"

MANUFACTURER = "Simple Plant Extended"

HEALTH_OPTIONS = [
    "notset",
    "poor",
    "fair",
    "good",
    "verygood",
    "excellent",
]

FEED_OPTIONS = [
    "liquid",
    "sticks",
    "pebbles",
]

ENABLED_OPTIONS = [
    "notset",
    "on",
    "off",
]

ILLUMINATION_OPTIONS = [
    "notset",
    "sunny",
    "partly_sunny",
    "shade",
]

IMAGES_MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".bmp": "image/bmp",
    ".webp": "image/webp",
    ".tiff": "image/tiff",
    ".svg": "image/svg+xml",
}


PLATFORMS: list[Platform] = [
    Platform.BUTTON,
    Platform.BINARY_SENSOR,
    Platform.DATE,
    Platform.IMAGE,
    Platform.NUMBER,
    Platform.SELECT,
    Platform.SENSOR,
]
