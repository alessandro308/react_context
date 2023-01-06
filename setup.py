from setuptools import find_packages, setup

setup(
    name='react_context',
    packages=find_packages(include=['react_context']),
    version='0.3.0',
    description='An API to pass data in the sub-function inspired by React Context',
    author='Alessandro Pagiaro',
    author_email='alessandropagiaro@gmail.com',
    url='https://github.com/alessandro308/react_context',
    license='MIT',
    install_requires=[],
    readme="README.md",
    tests_require=['pytest==7.2.0'],
    test_suite='tests',
)