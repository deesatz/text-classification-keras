from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 3 - Alpha'
]

version = '0.0.0'

setup(name='tex_cla',
      version=version,
      description='Text Classification Library for Keras',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Raghavendra Kotikalapudi, Johannes Filter',
      author_email='ragha@outlook.com, hi@jfilter.de',
      url='https://github.com/jfilter/text-classification-keras',
      license='MIT',
      install_requires=['keras==2.2.*', 'six==1.10.*',
                        'scikit-learn==0.19.*', 'joblib==0.12.*',
                        'jsonpickle==0.9.*', 'numpy==1.5.*'],
      extras_require={'full': ['spacy==2.0.*', 'deep-plots==0.1.*']},
      include_package_data=True,
      classifiers=classifiers,
      packages=find_packages())
