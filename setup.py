from setuptools import setup, find_namespace_packages
import sys

setup(
    name='vpy',
    version='0.0.1',
    url='',
    license='MIT',
    maintainer='Ross Daly',
    maintainer_email='rdaly525@stanford.edu',
    description='verilog parser',
    packages=find_namespace_packages(include=['vpy',]),
    install_requires=[
        'ply',
    ],
    python_requires='>=3.8',
)
