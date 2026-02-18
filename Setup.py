from setuptools import setup , find_packages
from typing import List

def Requirements()->List[str]:
    with open("Requirements.txt") as file:
        return file.read().splitlines()

setup(
    name="Stress Level",
    version="0.1.0",
    author="Omkar Kamate",
    author_email="omkarkamate2004@gmail.com",
    packages=find_packages(),
    install_requires=Requirements()
)
