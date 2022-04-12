from setuptools import find_packages, setup

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Generic release markers:
#   X.Y.0   # For first release after an increment in Y
#   X.Y.Z   # For bugfix releases
version = '0.1.5'

with open('requirements.txt') as f:
    requirements = [
        line.split('#', 1)[0].strip() for line in f.read().splitlines()
        if not line.strip().startswith('#')
    ]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jsonabler",
    version=version,
    author="webfucktory",
    author_email="root@webfucktory.com",
    description="Make your classes Jsonable",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/webfucktory/python-jsonabler",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.8',
    install_requires=requirements,
)
