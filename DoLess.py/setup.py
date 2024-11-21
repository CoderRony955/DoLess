from setuptools import setup, find_packages

setup(
    name="DoLess",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author="raunak_sh",
    description="""DoLess is a Python library that provides a set of functions that can be used to perform various tasks in Python. The library is designed to be easy to use and provides a simple functions and class where you can use in your Python scripts to perform basic tasks in just calling functions and methods.""",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
