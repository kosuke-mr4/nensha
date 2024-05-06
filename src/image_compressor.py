import logging
from pathlib import Path
from PIL import Image, ImageSequence
from pillow_heif import register_heif_opener
from src.utils import validate_compression_ratio , get_file_size_in_mb

register_heif_opener()

logger = logging.getLogger(__name__)

def compress_image(image_path: Path, compression_ratio: int) -> Path:
    validate_compression_ratio(compression_ratio)

    try:
        original_size = get_file_size_in_mb(image_path)
        compressed_path = image_path.with_stem(f"{image_path.stem}_compressed")
        with Image.open(image_path) as img:
            if "heic" in img.format.lower():
                img = next(ImageSequence.Iterator(img))
            img.save(compressed_path, optimize=True, quality=compression_ratio)
        compressed_size = get_file_size_in_mb(compressed_path)
        size_reduction = original_size - compressed_size
        logger.info(f"Image compressed successfully: {compressed_path}")
        logger.info(f"Original size: {original_size:.2f} MB")
        logger.info(f"Compressed size: {compressed_size:.2f} MB")
        logger.info(f"Size reduction: {size_reduction:.2f} MB")
        return compressed_path
    except FileNotFoundError as e:
        logger.error(f"Image file not found: {image_path}")
        raise e
    except Exception as e:
        logger.error(f"Error occurred while compressing image: {str(e)}")
        raise e