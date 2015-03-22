from setuptools import setup

setup(name='whatype',
      version='0.1',
      description='Python independent file type identification library',
      url='http://github.com/omriher/whatype',
      author='Omri Herscovici',
      author_email='omriher@gmail.com',
      license='GPLv3.0',
      packages=['whatype'],
	  package_data={
			'whatype': ['README.txt', 'magics.csv'],
		},
      zip_safe=False)