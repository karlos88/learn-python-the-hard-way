try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex48',
    'author': 'ExampleAuthor',
    'url': 'http://www.example.com',
    'download_url': 'http://www.example.com',
    'author_email': 'example@example.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)