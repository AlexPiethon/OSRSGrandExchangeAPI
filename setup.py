from distutils.core import setup

setup(
    # Application name:
    name="OSRSGrandExchangeAPI",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Zakk Lefkowits",
    author_email="zakk@zakk.io",

    # Packages
    packages=["OSRSGrandExchangeAPI"],
    package_data = {"OSRSGrandExchangeAPI": ['items.json']},

    # Details
    url="https://github.com/zakkl13/OSRSGrandExchangeAPI",

    #
    license="LICENSE.txt",
    description="Oldschool Runescape API for ",

    # long_description=open("README.txt").read(),

)
