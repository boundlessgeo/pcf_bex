import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="pcf_bex",
    version="0.1",
    author="",
    author_email="",
    description="pcf_bex, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="pcf_bex geonode django",
    url='https://github.com/boundlessgeo/pcf_bex',
    packages=['pcf_bex',],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'geoshape-geonode==1.4',
        'geoshape==1.7.11',
        'gunicorn==19.4.5',
        'whitenoise==2.0.6'
    ],
    dependency_links=[
        "git+ssh://github.com/boundlessgeo/rogue_geonode.git#egg=geoshape-1.7.11"
    ]
)
