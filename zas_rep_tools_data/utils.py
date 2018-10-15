#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Utilities 
# Author:
# c(Student) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import inspect, os

#path_to_zas_rep_tools_data = inspect.getfile(inspect.currentframe()) # script filename (usually with path)
path_to_zas_rep_tools_data = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory