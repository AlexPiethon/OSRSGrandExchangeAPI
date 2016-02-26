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

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/zakkl13/OSRSGrandExchangeAPI",

    #
    # license="LICENSE.txt",
    description="Oldschool Runescape API for ",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "requests",
        "json",
    ],
)
