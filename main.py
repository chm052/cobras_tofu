__author__ = 'marvin'
from CobrasTofu import VariableNameObfuscator

f = open('test_input')
print VariableNameObfuscator().replace_names(f)
