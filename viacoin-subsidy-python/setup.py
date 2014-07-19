from distutils.core import setup, Extension

viacoin_module = Extension('viacoin_subsidy', sources = ['viacoin_subsidy.cpp'])

setup (name = 'viacoin_subsidy',
       version = '1.0',
       description = 'Subsidy function for Viacoin',
       ext_modules = [viacoin_module])
