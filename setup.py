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
        'django-json-field==0.5.8',
    ],
    zip_safe=False,
    dependency_links=[
        'https://github.com/matllubos/django-json-field/tarball/0.5.8#egg=django-json-field-0.5.8',
        'https://github.com/asgeirrr/django-security/tarball/FixPython3RelatedSudsBugs'
        '#egg=django-security-FixPython3RelatedSudsBugs',
    ]
)
