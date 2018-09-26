from subprocess import check_call

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

setup(
    name='grow-ext-shortcodes',
    version='1.0.0',
    license='Apache License 2.0',
    author='Jung von Matt/tech GmbH',
    author_email='nextalster-developer@jvm.de',
    include_package_data=False,
    packages=[
        'shortcodes',
    ],
    install_requires=[
        'bbcode'
    ],
)
