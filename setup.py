from setuptools import setup, find_packages

setup(
    name='municipality-lookup',
    version='0.1.0',
    author='Andrea Iannazzo',
    author_email='andrea.iannazzo@gmail.com',
    description='Fuzzy and exact lookup tool for Italian municipalities',
    long_description = open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/andrjan1/municipality-lookup',
    packages=find_packages(),
    install_requires=['pandas'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.7',
)
