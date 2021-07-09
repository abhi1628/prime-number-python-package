from setuptools import setup, find_packages

classifiers = [
  'Developement Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='abhiprime',
  version='1.1.2',
  description='A program to check if the given number is a prime number or not',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Abhishek Singh',
  author_email='abhisheksingh@ggits.org',
  License='MIT',
  classifier=classifiers,
  keywords='primenumber',
  packages=find_packages(),
  install_requires=['']
)
