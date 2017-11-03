from setuptools import setup, find_packages

#- fill in setup's long description from README.me
readme_file = open('README.md')
readme_text = readme_file.read()

setup(name='colorlog',
      version='0.0.1a1',
      description='Colored Console Logs',
      long_description=readme_text,
      author='James Light',
      author_email='j.gareth.light@gmail.com',
      url='https://github.com/jl2501/colorlog',
      install_requires=['kaleidoscope'],
      packages=find_packages(exclude=['notes', 'debug', 'test']),
      keywords=['Logging', 'Color'],
      classifiers=['Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Operating System :: OS Independent',
                   'Development Status :: 1 - Planning'])
