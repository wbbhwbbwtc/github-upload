"""
EECS 485 project 1 static site generator.

Andrew DeOrio <awdeorio@umich.edu>
"""

from setuptools import setup

setup(
    name='insta485generator',
    version='0.1.0',
    packages=['insta485generator'],
    include_package_data=True,
    install_requires=[
        'bs4==0.0.1',
        'click==7.1.2',
        'html5validator==0.3.3',
        'jinja2==2.11.2',
        'pycodestyle==2.6.0',
        'pydocstyle==5.0.2',
        'pylint==2.5.3',
        'pytest==5.4.3',
        'requests==2.24.0',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'insta485generator = insta485generator.__main__:main'
        ]
    },
)
