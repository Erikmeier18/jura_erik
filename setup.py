import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read() 
setuptools.setup(
	name="rv_curve_jura_erik",
	version="0.1",
	author="Erik Meier",
	author_email="erikmeier18@gmail.com",
	description="Plot all RV curves that you want!",
	packages=setuptools.find_packages(),
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Erikmeier18/jura_erik/tree/main/rv_curve_jura",
	install_requires = ["numpy","matplotlib"],
	classifiers=["Programming Language :: Python :: 3"],
)
