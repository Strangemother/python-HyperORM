from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='hyperorm',
      version='0.1',
      description='Python API for HyperDex',
      long_description=readme(),
      test_suite='nose.collector',
	    tests_require=['nose'],
      keywords='hyperdex orm storage cloud',
      url='https://github.com/Strangemother/python-HyperORM',
      author='Strangemother',
      author_email='jay@strangemother.com',
      license='MIT',
      packages=['hyperorm'],
      install_requires=[],
      zip_safe=False)
