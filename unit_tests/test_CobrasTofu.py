import unittest
from CobrasTofu import VariableNameObfuscator

class test_CobrasTofu(unittest.TestCase):

    # TODO this could be more succinct
    input = """__author__ = 'marvin'

    import re

    class CobrasTofu:

        def __init__(self):
            pass

        def replace_names(self, obfuscatee):
            rgx = re.compile(".*=.*")
            for line in obfuscatee:
                if rgx.match(line):
                    print line

            print "\n\n"
            return obfuscatee

        # TODO
        def add_junk(self):
            pass

        # TODO think of more obfuscations
        # TODO monetize monetize monetize

    f = open('test_input')
    print CobrasTofu().replace_names(f.read())"""

    expected_output = """varvarvarvar= \'marvin\'    import re    class CobrasTofu:        def __init__(self):            pass        def replace_names(self, obfuscatee):varvarvarvar= re.compile(".*=.*")            for line in obfuscatee:                if rgx.match(line):                    print line            print ""            return obfuscatee        # TODO        def add_junk(self):            pass        # TODO think of more obfuscations        # TODO monetize monetize monetizevarvarvarvar= open(\'test_input\')    print CobrasTofu().replace_names(f.read())"""

    def test_replace_names_iterable(self):
        cobrasTofu_testobject = VariableNameObfuscator()

        #self.assertEqual(cobrasTofu_testobject._replace_names_iterable(self.input),
        #                 self.expected_output)

        self.assertEqual(self.expected_output,
                         cobrasTofu_testobject._replace_names_iterable(iter(self.input.splitlines())))