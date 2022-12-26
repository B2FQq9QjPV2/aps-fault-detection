from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."
def get_requiremetns()->List[str]:...


def get_requirements():
    pass

setup(
    name = 'sensor'
    version = "0.0.1"
    author = "ineuron_megha"
    author_email = "meghaw42@gmail.com"
    packages =  find_packages(),
    install_requires = get_requirements(),
)

from setuptools import find_packages,setup