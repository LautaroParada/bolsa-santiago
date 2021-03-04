import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.3'
PACKAGE_NAME = 'bolsa_stgo'
AUTHOR = 'Lautaro Parada Opazo'
AUTHOR_EMAIL = 'lautaro.parada.opazo@gmail.com'
URL = 'https://github.com/LautaroParada/bolsa-santiago'

LICENSE = 'MIT License'
DESCRIPTION = 'SDK de la API de la bolsa de Santiago.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = []

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )