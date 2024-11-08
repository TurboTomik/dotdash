from setuptools import setup, find_packages

setup(
    name="dotdash",
    version="0.1.0",
    author="Tomik",
    author_email="maxiwrayt@gmail.com",
    description="This project provides a tool for encoding and decoding Morse code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TurboTomik/dotdash",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
