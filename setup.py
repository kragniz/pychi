#!/usr/bin/env python
# -*- coding: utf-8 -*-
# see http://docs.python.org/distutils/

from distutils.core import setup
import libpychi
setup(name = libpychi.data.NAME,
      version = libpychi.data.VERSION,
      description = libpychi.data.DESCRIPTION,
      author = 'Louis Taylor',
      author_email = 'kragniz@gmail.com',
      license = 'GPL v3 or later',
      packages = ['libpychi'],
      scripts = ['pychi', 'pychi-applet'],
      data_files=[(libpychi.data.ICON_DIR,
                 ['icons/internet-connected.svg',
                  'icons/internet-disconnected.svg'])]
      )
