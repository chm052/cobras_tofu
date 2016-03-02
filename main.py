__author__ = 'marvin'

import re

class CobrasTofu:

    variable_declaration = re.compile("^[\s]*[a-zA-Z_][a-zA-Z0-9_]*[\s]*=[\s]*")

    def __init__(self):
        pass

    def replace_names(self, obfuscatee):
        varname_set = set()
        obfuscated = ""
        for line in obfuscatee.readlines():
            if self.variable_declaration.match(line):
                #print "line: " + line
                varname_set.add(re.compile("^[\s]*" + line[:line.index('=')].strip() + "[\s]+"))
                subd = re.sub(self.variable_declaration, "VAR=", line)
                #print subd
            for varname in varname_set:
                if re.match(varname, line):
                    line = re.sub(varname, self._generate_varname(), line) + "\n"
            obfuscated += line

        return obfuscated

    def _generate_varname(self):
        return "varvarvarvar"

    # TODO
    def add_junk(self):
        pass

    # TODO think of more obfuscations
    # TODO monetize monetize monetize

f = open('test_input')
print CobrasTofu().replace_names(f)
