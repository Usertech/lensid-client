from setuptools import find_packages, setup

from lensid_client.version import get_version


setup(
    name="lensid-client",
    version=get_version(),
    description="A client library for Lens ID API",
    author='Lukas Rychtecky',
    author_email='lukas.rychtecky@gmail.com',
    url='https://github.com/LukasRychtecky/lensid-client',
    license='MIT',
    package_dir={'lensid-client': 'lensid_client'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'requests>=2.10.0',
    ],
    zip_safe=False
)
