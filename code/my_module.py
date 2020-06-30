#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: insert date (e.g. 2020/12/25)
@author: your name, username or email (e.g. name.surname@tecnalia.com)

Short description of the aims of the script.
"""
from logging import getLogger
from configparser import ConfigParser
from typing import Iterable, Tuple


class MyClass:
    def __init__(self, logger=None):
        # set logger
        self.logger = logger or getLogger('__main__')
        # parse config.ini file
        config = ConfigParser(allow_no_value=True)
        config.read('config.ini')

    # example of instance method
    def my_instance_method(self, arg1: Iterable, arg2: Tuple) -> None:
        """Short description of the method.

        :param arg1:
        :param arg2:
        :return:
        :raise:
        """
        self.logger.info('Start process.')

        # insert your code here.

        return None

    # example of class method
    @classmethod
    def my_classmethod(cls, arg1, arg2):
        """Short description of the method.

        :param arg1:
        :param arg2:
        :return:
        :raise:
        """

        # insert your code here.

        return None

    # example of static method
    @staticmethod
    def my_staticmethod(arg1, arg2):
        """Short description of the method.

        :param arg1:
        :param arg2:
        :return:
        :raise:
        """

        # insert your code here.

        return None
