import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def validate_image_format(fmt: str) -> None:
    supported_formats = ['jpeg', 'jpg', 'JPG', 'png', 'PNG', 'gif', 'GIF', 'bmp', 'BMP', 'webp', 'WEBP', 'heic', 'HEIC']
    if fmt not in supported_formats:
        logger.error(f"Unsupported image format: {fmt}")
        raise ValueError(f"Unsupported image format: {fmt}")

def validate_compression_ratio(ratio: int) -> None:
    if ratio < 0 or ratio > 100:
        logger.error(f"Invalid compression ratio: {ratio}")
        raise ValueError(f"Invalid compression ratio: {ratio}. Must be between 0 and 100.")

def get_file_size_in_mb(file_path: Path) -> float:
    return file_path.stat().st_size / (1024 * 1024)