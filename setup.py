from setuptools import setup, find_packages

setup(
    name='py-fhe',
    description='Python implementations of CKKS and BFV cryptosystems',
    author='Elvis',
    author_email='erabelli@mit.edu',
    license='MIT',
    install_requires=[
        'sympy',
        'pytest',
    ],
    packages=['bfv', 'ckks', 'tests', 'util']
)