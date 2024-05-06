import click
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.image_converter import convert_image
from src.image_compressor import compress_image
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), help='Output image file path')
@click.option('-t', '--target-format', help='Target image format (jpg, png, gif, bmp, webp)')
@click.option('-c', '--compression-ratio', type=int, default=50, help='Compression ratio (0-100)')
def cli(input_file, output, target_format, compression_ratio):
    try:
        input_path = Path(input_file)        
        if target_format:
            if not output:
                output_path = input_path.with_suffix(f'.{target_format}')
            else:
                output_path = Path(output)
            convert_image(input_path, output_path, target_format)
            input_path = output_path
        
        if compression_ratio:
            compressed_path = compress_image(input_path, compression_ratio)
            click.echo(f"Image compressed successfully: {compressed_path}")
        else:
            click.echo(f"Image processed successfully: {input_path}")
            
    except Exception as e:
        click.echo(f"Error: {str(e)}")

if __name__ == '__main__':
    cli()