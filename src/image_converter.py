import logging
from pathlib import Path
from PIL import Image, ImageSequence
from src.utils import validate_image_format

from pillow_heif import register_heif_opener

logger = logging.getLogger(__name__)

register_heif_opener()

def convert_image(input_path: Path, output_path: Path, target_format: str) -> None:
    validate_image_format(target_format)

    try:
        with Image.open(input_path) as img:
            if "heic" in img.format.lower():
                img = next(ImageSequence.Iterator(img))
            img.save(output_path, format=target_format)
            logger.info(f"Image converted successfully: {input_path} -> {output_path}")
    except FileNotFoundError as e:
        logger.error(f"Input file not found: {input_path}")
        raise e
    except Exception as e:
        logger.error(f"Error occurred while converting image: {str(e)}")
        raise e