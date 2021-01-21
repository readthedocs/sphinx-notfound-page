import notfound
import setuptools


with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sphinx-notfound-page',
    version=notfound.__version__,
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    description='Sphinx extension to build a 404 page with absolute URLs',
    url='https://github.com/readthedocs/sphinx-notfound-page',
    license='MIT',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ],
    keywords='notfound 404 page sphinx',
    project_urls={
        'Documentation': 'https://sphinx-notfound-page.readthedocs.io/',
        'Source': 'https://github.com/readthedocs/sphinx-notfound-page',
        'Tracker': 'https://github.com/readthedocs/sphinx-notfound-page/issues',
    },
)
