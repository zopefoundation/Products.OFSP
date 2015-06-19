##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import setup, find_packages

setup(name='Products.OFSP',
      version = '2.13.3.dev0',
      url='http://pypi.python.org/pypi/Products.OFSP',
      license='ZPL 2.1',
      description="General Zope 2 help screens.",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=open('README.txt').read() + '\n' +
                       open('CHANGES.txt').read(),
      packages=find_packages('src'),
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      install_requires=[
        'setuptools',
        'ExtensionClass < 4.0dev',
        'AccessControl',
        'Persistence',
        'Zope2 >= 2.13.0a1',
      ],
      include_package_data=True,
      zip_safe=False,
      )
