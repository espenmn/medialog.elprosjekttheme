from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='medialog.elprosjekttheme',
      version=version,
      description="A theme for Plone 4",
      long_description=open("README.txt").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
                   "Framework :: Plone",
                   "Programming Language :: Python",
                   ],
      keywords='Plone 4 theme',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='http://github.com/espenmn/medialog.elprosjekttheme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
                        'setuptools',
                        'medialog.subskins',
                        'medialog.portlet.placeholder',
                        # -*- Extra requirements: -*-
                        ],
      entry_points="""
          # -*- Entry points: -*-
          
          [z3c.autoinclude.plugin]
          target = plone
          """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
