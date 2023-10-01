from setuptools import setup

setup(
    name="mugit",
    version="1.0",
    packages=["mugit"],
    entry_points={"console_scripts": ["mugit = mugit.cli:main"]},
)
