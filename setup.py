
from setuptools import setup, find_packages

setup(
    name='educational_alife',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'rake-nltk',
        'nltk',
        'scikit-learn'
    ],
    author='Narges Shahhoseini',
    author_email='n.shahhoseini@ut.ac.ir',
    description='An artificial life ecosystem for educational content evolution.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Narges-Shah/educational_alife',  # optional, if you publish it
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
