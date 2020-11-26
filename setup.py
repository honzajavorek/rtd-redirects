from setuptools import setup


version = '1.0.1'
install_requires = [
    'requests',
    'lxml',
    'cssselect',
    'click',
    'pyaml'
]
tests_require = [
    'flake8'
]


setup(
    name='rtd-redirects',
    version=version,
    description='Manage redirects in the ReadTheDocs admin, programmatically',
    long_description=open('README.rst').read(),
    author='Honza Javorek',
    author_email='mail@honzajavorek.cz',
    url='https://github.com/honzajavorek/rtd-redirects',
    license=open('LICENSE').read(),
    py_modules=('rtd_redirects',),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            'rtd-redirects = rtd_redirects:main',
        ],
    },
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
        'Topic :: Internet',
    ),
    keywords='readthedocs documentation redirects sphinx mkdocs'
)
