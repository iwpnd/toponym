from setuptools import setup

packages = ["toponym"]

setup(
    name="toponym",
    version="0.3.3",
    description="build grammatical cases for words in slavic languages",
    url="http://github.com/iwpnd/toponym",
    author="Benjamin Ramser",
    author_email="ahoi@iwpnd.pw",
    license="MIT",
    include_package_data=True,
    install_requires=[],
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: Slavic",
        "Intended Audience :: Developers",
    ],
)
