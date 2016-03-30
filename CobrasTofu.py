__author__ = 'marvin'

import re


class VariableNameObfuscator:

    variable_declaration = re.compile("^[\s]*[a-zA-Z_][a-zA-Z0-9_]*[\s]*=[\s]*")

    def __init__(self):
        pass

    def replace_names(self, obfuscatee_file):
        return self._replace_names_iterable(obfuscatee_file.readlines())

    def _replace_names_iterable(self, obfuscatee_iterable):
        varname_set = set()
        obfuscated = ""
        for line in obfuscatee_iterable:
            if self.variable_declaration.match(line):
                varname_set.add(re.compile("^[\s]*" + line[:line.index('=')].strip() + "[\s]+"))
                subd = re.sub(self.variable_declaration, "VAR=", line)
            for varname in varname_set:
                if re.match(varname, line):
                    line = re.sub(varname, self._generate_varname(), line)
            obfuscated += line

        return obfuscated

    def _generate_varname(self):
        return "varvarvarvar"

    # TODO
    def add_junk(self):
        pass

    # TODO think of more obfuscations
    # TODO monetize monetize monetize