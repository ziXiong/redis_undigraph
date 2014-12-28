#!/usr/bin/env python
# Copyright (c) 2007 Qtrac Ltd. All rights reserved.
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from setuptools import setup

setup(name='redis_undigraph',
      version='1.0',
      author="ziXiong",
      author_email="quezixiong@qq.com",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['redis_undigraph', 'test'],
      platforms=["Any"],
      license="BSD",
      keywords='redis graph database',
      description="Python graph database implemented on top of Redis.",
      )
