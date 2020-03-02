import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piccolo-cipher",
    version="0.0.0",
    author="Adithya Pokala",
    author_email="adithya@visualdev.in",
    description="Piccolo: An Ultra-Lightweight Blockcipher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adipokala/piccolo-cipher",
    packages=[
        "piccolo_cipher"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)