import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fnet_improved",
    version="0.0.1",
    author="YBI",
    author_email="yeun0908@gmail.com",
    description="an improved FNet forked from Hugging Face transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hoeny-Be/fnet-improved",
    project_urls={
        "Bug Tracker": "https://github.com/Hoeny-Be/fnet-improved/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)