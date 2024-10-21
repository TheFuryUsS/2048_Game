from setuptools import setup, find_packages

setup(
    name='2048_Game',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    description='Implementación del juego 2048 en Python con TDD',
    author='Xavi',
    author_email='ivax132001@example.com',
    url='https://github.com/TheFuryUsS/2048_Game',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
