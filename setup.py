from setuptools import setup, find_packages, setuptools

classifiers = [
  'Developement Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='abhiprime',
  version='6.0.0',
  description='A program to check if the given number is a prime number or not',
  long_description_content_type='text/markdown',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Abhishek Singh',
  author_email='abhisheksingh@ggits.org',
  License='MIT',
  classifier=classifiers,
  keywords='primenumber',
  packages=setuptools.find_packages(),
  install_requires=['']
)
