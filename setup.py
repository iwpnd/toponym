from setuptools import setup

packages = ["toponym"]

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="toponym",
    version="0.4.1",
    description="build grammatical cases for words in slavic languages",
    url="http://github.com/iwpnd/toponym",
    author="Benjamin Ramser",
    author_email="ahoi@iwpnd.pw",
    license="MIT",
    include_package_data=True,
    install_requires=required,
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: Slavic",
        "Intended Audience :: Developers",
    ],
)
