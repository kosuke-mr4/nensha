import unittest
from src.utils import validate_image_format, validate_compression_ratio

class TestUtils(unittest.TestCase):
    def test_validate_image_format(self):
        validate_image_format('jpeg')
        validate_image_format('jpg')
        validate_image_format('JPG')
        validate_image_format('png')
        validate_image_format('PNG')
        validate_image_format('gif')
        validate_image_format('GIF')
        validate_image_format('bmp')
        validate_image_format('BMP')
        validate_image_format('webp')
        validate_image_format('WEBP')
        validate_image_format('heic')
        validate_image_format('HEIC')
        validate_image_format('heif')
        validate_image_format('HEIF')
        
        with self.assertRaises(ValueError):
            validate_image_format('invalid')

    def test_validate_compression_ratio(self):
        validate_compression_ratio(50)
        validate_compression_ratio(0)
        validate_compression_ratio(100)
        with self.assertRaises(ValueError):
            validate_compression_ratio(-10)
        with self.assertRaises(ValueError):
            validate_compression_ratio(150)

if __name__ == '__main__':
    unittest.main()