from distutils.core import setup

setup(name='HL API Project',
      version='1.0',
      description='Sample testing project',
      packages=['api_project'],
      install_requires=['pytest',
                        'selenium',
                        'allure-pytest',
                        'requests'
                        ]
      )