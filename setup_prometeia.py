from setuptools import find_packages
from setup import __version__, __description__, __license__, __author__, __email__
from promebuilder import gen_metadata, setup
from promebuilder.utils import VERSIONFILE

with open(VERSIONFILE, 'w') as verfile:
    vv = __version__.split('.')
    while len(vv) < 3:
        vv.append('0')
    verfile.write('.'.join(vv))

METADATA = gen_metadata(
    name='django-mongoengine',
    description=__description__,
    url='https://github.com/prometeia/django-mongoengine',
    email="pytho_support@prometeia.com",
    keywords="mongodb mongoengine django odm",
    package_data={'django-mongoengine': ['*.*']}
)
METADATA.update(dict(
    license=__license__,
    author=__author__,
    author_email=__email__,
    packages=find_packages(exclude=('doc', 'docs', 'tests')),
    include_package_data=True,
))


if __name__ == '__main__':
    setup(METADATA)
