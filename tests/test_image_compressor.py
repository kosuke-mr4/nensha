import unittest
from pathlib import Path
from src.image_compressor import compress_image
from src.image_converter import convert_image
from src.utils import validate_image_format

class TestImageCompressor(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = Path('tests/test_data')
        self.input_file = self.test_data_dir / 'input.jpg'
        self.output_file = self.test_data_dir / 'compressed.jpg'

    def tearDown(self):
        if self.output_file.exists():
            self.output_file.unlink()

    def test_compress_image(self):
        compress_image(self.input_file, 50)
        self.assertTrue(self.input_file.stat().st_size > self.input_file.stat().st_size)

    def test_invalid_compression_ratio(self):
        with self.assertRaises(ValueError):
            compress_image(self.input_file, 150)
            
    def test_convert_image_invalid_input(self):
        with self.assertRaises(FileNotFoundError):
            convert_image(Path('nonexistent.jpg'), self.output_file, 'png')

    def test_convert_image_invalid_output(self):
        with self.assertRaises(ValueError):
            convert_image(self.input_file, Path('/invalid/path/output.png'), 'png')

    def test_validate_image_format_valid(self):
        validate_image_format('jpg')
        validate_image_format('PNG')
        validate_image_format('GiF')

    def test_validate_image_format_invalid(self):
        with self.assertRaises(ValueError):
            validate_image_format('invalid')

if __name__ == '__main__':
    unittest.main()