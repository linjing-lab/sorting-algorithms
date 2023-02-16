import os
import sys

from setuptools import setup

if sys.version_info < (3, 7, 0):
    raise OSError(f'sortingx requires Python >=3.7, but yours is {sys.version}')

if (3, 7, 0) <= sys.version_info < (3, 8, 0):
    # https://github.com/pypa/setuptools/issues/926#issuecomment-294369342
    try:
        import fastentrypoints
    except ImportError:
        try:
            import pkg_resources
            from setuptools.command import easy_install

            easy_install.main(['fastentrypoints'])
            pkg_resources.require('fastentrypoints')
        except:
            pass

try:
    pkg_name = 'sortingx'
    libinfo_py = os.path.join(pkg_name, '__init__.py')
    libinfo_content = open(libinfo_py, 'r', encoding='utf-8').readlines()
    version_line = [l.strip() for l in libinfo_content if l.startswith('__version__')][0]
    exec(version_line) # gives __version
except FileNotFoundError:
    __version__ = '0.0.0'

try:
    with open('README.md', 'r', encoding='utf-8') as fp:
        _long_description = fp.read()
except FileNotFoundError:
    _long_description = ''

setup(
    name=pkg_name,
    packages=['sortingx',],
    version=__version__,
    description='The powerful package designed for sorting.',
    author='林景',
    author_email='linjing010729@163.com',
    license='Apache 2.0',
    url='https://github.com/linjing-lab/sorting-algorithms',
    download_url='https://github.com/linjing-lab/sorting-algorithms/tags',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    setup_requires=['setuptools>=18.0', 'wheel'],
    project_urls={
        'Source': 'https://github.com/linjing-lab/sorting-algorithms/tree/main/sortingx',
        'Tracker': 'https://github.com/linjing-lab/sorting-algorithms/issues',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'typing_extensions>=3.10.0.2'
    ]
    # extras_require = []
)