from distutils.core import setup
import os

setup(
    name='pythonpy',
    version='0.2.5',
    description='Take advantage of your python skills from the command line',
    scripts=['py', 'extras/pycompleter', 'bin/wpy'],
    data_files=[
            ('/etc/bash_completion.d', ['extras/pycompletion.sh']),
        ],
    license='MIT',
    url='https://github.com/Russell91/pythonpy',
    long_description='',
)
