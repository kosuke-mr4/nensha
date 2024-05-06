from setuptools import setup, find_packages

setup(
    name='nensha',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nensha=src.main:cli',
        ],
    },
    install_requires=[
        'Pillow',
        'Click',
    ],
)