from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='react_context',
    packages=find_packages(include=['react_context']),
    version='0.4.0',
    description='An API to pass data in the sub-function inspired by React Context',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alessandro Pagiaro',
    author_email='alessandropagiaro@gmail.com',
    url='https://github.com/alessandro308/react_context',
    license='MIT',
    install_requires=[],
    readme="README.md",
    tests_require=['pytest==7.2.0'],
    test_suite='tests',
)