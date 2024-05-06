import unittest
from pathlib import Path
from src.image_converter import convert_image
from src.image_compressor import compress_image
from src.utils import validate_compression_ratio

class TestImageConverter(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = Path('tests/test_data')
        self.input_file = self.test_data_dir / 'input.jpg'
        self.output_file = self.test_data_dir / 'output.png'

    def tearDown(self):
        if self.output_file.exists():
            self.output_file.unlink()

    def test_convert_image(self):
        convert_image(self.input_file, self.output_file, 'png')
        self.assertTrue(self.output_file.exists())

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_image(self.input_file, self.output_file, 'invalid')
    
    def test_compress_image_invalid_input(self):
        with self.assertRaises(FileNotFoundError):
            compress_image(Path('nonexistent.jpg'), 50)

    def test_validate_compression_ratio_valid(self):
        validate_compression_ratio(0)
        validate_compression_ratio(50)
        validate_compression_ratio(100)

    def test_validate_compression_ratio_invalid(self):
        with self.assertRaises(ValueError):
            validate_compression_ratio(-10)
        with self.assertRaises(ValueError):
            validate_compression_ratio(150)

if __name__ == '__main__':
    unittest.main()