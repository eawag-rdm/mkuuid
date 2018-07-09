from setuptools import setup

setup(
    name='mkuuid',
    version='1.0',
    author='Harald von Waldow',
    author_email='harald.vonwaldow@eawag.ch',
    packages=['mkuuid'],
    url='https://github.com/eawag-rdm/mkuuid.git',
    license='GNU Affero General Public License',
    description='Create a file with name "uuid-<uuid> in specified directory',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        ],
    entry_points={
        'console_scripts': ['mkuuid=mkuuid.mkuuid:main_gui']
    }
)
