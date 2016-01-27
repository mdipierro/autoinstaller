# Created by Massimo Di Pierro (http://experts4solutions.com) @2016 BSDv3 License

import sys, imp
from ez_setup import use_setuptools
use_setuptools()
from setuptools.command.easy_install import main

class SmartImporter(object):
    tried_modules=set()
    domain_modules = set()
 
    def find_module(self, fullname, path=None):
        if fullname in self.domain_modules:
            return self
        if fullname in self.tried_modules:
            return None
        else:
            self.tried_modules.add(fullname)
            try:
                main([fullname])
                return self
            except:
                return None

    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.modules[fullname]
        mod = imp.new_module(fullname)
        mod.__loader__ = self
        sys.modules[fullname] = mod
        if fullname not in self.domain_modules:
            self.domain_modules.add(fullname)
        return mod 
 
sys.meta_path = [SmartImporter()]

