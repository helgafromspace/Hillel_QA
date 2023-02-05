from distutils.core import setup

setup(name='HL Web Project',
      version='1.0',
      description='Sample testing project',
      packages=['web_project'],
      install_requires=['pytest',
                        'selenium',
                        'webdriver-manager'
                        ]
      )