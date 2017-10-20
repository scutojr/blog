#!/usr/bin/env python

import pudb


class Meta(type):
    def __new__(cls, name, *parents, **dct):
        #pudb.set_trace()
        print '@@@@@@@@@@@@@@@@@@@@@'
        print cls
        print name
        hehe = super(Meta, cls).__new__(cls, name, parents, dct)
        print '@@@@@@@@@@@@@@@@@@@@@'
        print hehe
        print '@@@@@@@@@@@@@@@@@@@@@'
        return hehe


class Test(object):
    __metaclass__ = Meta
    pass
