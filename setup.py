from distutils.core import setup
setup(
  name = 'orangetool',
  packages = ['orangetool'],
  version = '0.25',
  description = 'Some useful script for Orangepi/Raspberrypi boards',
  long_description="",
  author = 'Moduland Co',
  author_email = 'info@moduland.ir',
  url = 'https://github.com/Moduland/Orangetool',
  download_url = 'https://github.com/Moduland/Orangetool/tarball/v0.24',
  keywords = ['orangepi', 'raspberrypi', 'embedded-systems','python'],
  classifiers = [],
  install_requires=[
      'psutil',
	  'requests',
      ],
  license='MIT',
)
