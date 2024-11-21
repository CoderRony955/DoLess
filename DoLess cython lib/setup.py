from setuptools import setup, Extension
from Cython.Build import cythonize


extentions = [
    Extension(
        name="DoLess",
        sources=["DoLess.pyx"],
        language="c",
    )
]

setup(
    name="DoLess",
    ext_modules=cythonize(extentions),
    zip_safe=False

)
