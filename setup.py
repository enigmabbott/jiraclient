try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='jiraclient',
      version=verstr,
      description='A REST client for Atlassian JIRA',
      url='https://github.com/enigmabbott/jiraclient',
      author='Scott Abbott',
      license='GPL',
      packages=['jiraclient'],
      scripts=['bin/jiraclient'],
      install_requires=[
          "restkit",
          "PyYAML"
      ],
     )

