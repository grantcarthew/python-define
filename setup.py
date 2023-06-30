from setuptools import setup

setup(
    name='define',
    version='0.1.0',
    py_modules=['define'],
    install_requires=[
        'Click',
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'define = define:cli',
        ],
    },
)