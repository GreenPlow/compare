from setuptools import setup, find_packages

setup(
   name='compare',
   version='0.0',
   description='A useful module to compare files between directories and safely copy',
   packages=find_packages(where="src"),
   package_dir={"": "src"},
)
