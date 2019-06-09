#!/usr/bin/env python3


class Version():
    def __init__(self, major, minor=0, patch=0):
        if isinstance(major, str):
            resu_tuple = convert_string_to_version_component_numbers(major)
            self.major = resu_tuple[0]
            self.minor = resu_tuple[1]
            self.patch = resu_tuple[2]
        elif isinstance(major, int):
            self.major = major
            self.minor = minor
            self.patch = patch
        elif isinstance(major, tuple):
            self.major = major[0]
            if len(major) >= 2:
                self.minor = major[1]
                if len(major) == 3:
                    self.patch = major[2]
                else:
                    self.patch = 0


    def __repr__(self):
        return_string = "Version(%s, %s, %s)" % (self.major, self. minor,
                                                 self.patch)
        return return_string


    def __str__(self):
        return_string = "%s.%s.%s" % (self.major, self. minor, self.patch)
        return return_string


    def __lt__(self, other):
        # "rich comparison" instance methods
        tup1 = (self.major, self.minor, self. patch)
        tup2 = (other.major, other.minor, other. patch)
        if compare_versions(tup1, tup2) == -1:
            return True
        else:
            return False


    def __le__(self, other):
        # "rich comparison" instance methods
        tup1 = (self.major, self.minor, self. patch)
        tup2 = (other.major, other.minor, other. patch)
        if compare_versions(tup1, tup2) == 1:
            return False
        else:
            return True


    def __eq__(self, other):
        # "rich comparison" instance methods
        tup1 = (self.major, self.minor, self. patch)
        tup2 = (other.major, other.minor, other. patch)
        if compare_versions(tup1, tup2) == 0:
            return True
        else:
            return False


    def __ne__(self, other):
        # "rich comparison" instance methods
        tup1 = (self.major, self.minor, self. patch)
        tup2 = (other.major, other.minor, other. patch)
        if compare_versions(tup1, tup2) == 0:
            return False
        else:
            return True


    def __gt__(self, other):
        # "rich comparison" instance methods
        tup1 = (self.major, self.minor, self. patch)
        tup2 = (other.major, other.minor, other. patch)
        if compare_versions(tup1, tup2) == 1:
            return True
        else:
            return False


    def __ge__(self, other):
        # "rich comparison" instance methods
        tup1 = (self.major, self.minor, self. patch)
        tup2 = (other.major, other.minor, other. patch)
        if compare_versions(tup1, tup2) == -1:
            return False
        else:
            return True




def convert_string_to_version_component_numbers(s):
    """
    Convert a Semantic Versioning Component Number String to a Tuple
    Input:
        - s: a string of numbers (1 to 3 components as major, minor and path)
    Output:
        - resu_tuple: the tuple (major, minor, patch), replace the missing
            component with 0
    """
    components = s.split(".")
    resu_tuple = ()
    for component in components:
        resu_tuple += (int(component),)
    while len(resu_tuple) < 3:
        resu_tuple += (0,)
    return resu_tuple


def compare_versions(this, other):
    """
    Compare Versions
    Input:
        -this: the tuple (major, minor, patch) - original
        -other: the tuple (major, minor, patch) - compare material
    Output:
        - 1: if this > other
        - -1: if this < other
        - 0 : if this = other
        (prioritize from major to minor then patch)
    """
    for index in range(3):
        if this[index] > other[index]:
            return 1
        elif this[index] < other[index]:
            return -1
        else:
            continue
    return 0

def main():
    resu_tuple = convert_string_to_version_component_numbers("4")
    compare_versions((4,2,2),(3,3,2))
    print(Version("2.4.5") < Version("1.2.8"))

if __name__ == '__main__':
    main()
