import notfound
import setuptools


with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sphinx-notfound-page',
    version=notfound.version,
    author='Manuel Kaufmann',
    author_email='humitos@gmail.com',
    description='Sphinx extension to build a 404 page with absolute URLs',
    url='https://github.com/rtfd/sphinx-notfound-page',
    license='MIT',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
