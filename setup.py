from setuptools import setup


setup(name='iban',
      version='0.0.1',
      packages=['iban'],
      description='Server to provide IBAN related services',
      author='Sai Sameer Guttha',
      author_email='saisameer.gutha@gmail.com',
      install_requires=open('requirements.txt').read().splitlines())
