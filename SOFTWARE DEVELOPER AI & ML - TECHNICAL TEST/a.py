'''ORMUCO'S SOFTWARE DEVELOPER AI & ML - TECHNICAL TEST, Question B

This is a software library that accepts 2 version string as input and returns
whether one is greater than, equal, or less than the other. As an example:
“1.2” is greater than “1.1”. Some test cases are provided.
'''

class Version(version_string):
    !!!! make these attributes private, so We do not allow this to be modified directly, only by the setter methods, to make sure that the version_number and subversion_number stays consistent with the version string
    self.version_string
    self.version_number
    self.subversion_number

    constructor with the version_string
    constructor with the version numbers

    def set_version(self, new_version_string):
        self.version_string = new_version_string
        self.version_number, self.subversion_number = new_version_string.split('.')

    def increment_version(self):
        !!!! might need a type cast to int to be able to implement, or keep the value in int in the class definition
        # first set the new version number
        self.version_number += 1
        # then uses the new incremented version number to build the new version_string
        self.version_string = "{}.0".format(self.version_number)

    def increment_subversion(self):
        # first set the new subversion number
        self.subversion_number += 1
        # then uses the new incremented subversion number to build the new version_string
        self.version_string = "{}.{}".format(self.version_number, self.subversion_number)


    def is_greater_than(self, other_version):
        if (self.version_number > other_version.version_number):
            return True
        elif (self.version_number == other_version.version_number):
            if (self.subversion_number > other_version.subversion_number):
                return True
        return False

    def is_equal_to(self, other_version):
        if (
            self.version_number == other_version.version_number
            and self.subversion_number == other_version.subversion_number
        ):
            return True
        return False

    def is_less_than(self, other_version):
        if (self.version_number < other_version.version_number):
            return True
        elif (self.version_number == other_version.version_number):
            if (self.subversion_number < other_version.subversion_number):
                return True
        return False

    def compare_version_to(self, other_version):
        if self.is_greater_than(other_version):
            return("“{}” is greater than “{}”".format(self.version_string, other_version.version_string))
        if self.is_less_than(other_version):
            return("“{}” is less than “{}”".format(self.version_string, other_version.version_string))
        if self.is_equal_to(other_version):
            return("“{}” is equal to “{}”".format(self.version_string, other_version.version_string))
        return ("Error")

def compare_version_strings(version_string_A, version_string_B):
    version_A = Version(version_string_A)
    version_B = Version(version_string_B)
    if version_A.is_greater_than(version_B):
        return("“{}” is greater than “{}”".format(version_A.version_string, version_B.version_string))
    if version_A.is_less_than(version_B):
        return("“{}” is less than “{}”".format(version_A.version_string, version_B.version_string))
    if version_A.is_equal_to(version_B):
        return("“{}” is equal to “{}”".format(version_A.version_string, version_B.version_string))
    return ("Error")
        

if __name__ == "__main__":
    # read the first version string
    version_string_A = input()
    # read the second version string
    version_string_B = input()

    # instantiate the version A object with the string contructor
    version_A = Version(version_string_A)

    # instantiate the version A object with the numbers constructor
    version_number_B, subversion_number_B = version_string_B.split('.')
    version_B = Version(version_number_B, subversion_number_B)

    print(version_A.compare_version_to(version_B))


def test_case_1():
    version_a = Version("0.3")
    version_b = Version(0, 2)
    assert version_a.is_greater_than(version_b) == True
    assert version_a.is_less_than(version_b) == False
    assert version_a.is_equal_to(version_b) == False

def test_case_2():
    # "1.2" is equal to "1.2"
    version_a = Version("1.2")
    version_b = Version(1, 2)
    assert version_a.is_greater_than(version_b) == False
    assert version_a.is_less_than(version_b) == False
    assert version_a.is_equal_to(version_b) == True

def test_case_3():
    # "0.130" is greater than "0.99"
    version_a = Version("0.130")
    version_b = Version(0, 99)
    assert version_a.is_greater_than(version_b) == True
    assert version_a.is_less_than(version_b) == False
    assert version_a.is_equal_to(version_b) == False

def test_case_4():
    # "0.13" is less than "0.99"
    version_a = Version("0.13")
    version_b = Version(0, 99)
    assert version_a.is_greater_than(version_b) == False
    assert version_a.is_less_than(version_b) == True
    assert version_a.is_equal_to(version_b) == False

def test_case_5():
    # "0.9999999" is less than "1.0"
    version_a = Version("0.9999999")
    version_b = Version(1, 0)
    assert version_a.is_greater_than(version_b) == False
    assert version_a.is_less_than(version_b) == True
    assert version_a.is_equal_to(version_b) == False

def test_case_6():
    # "0.9999999" is less than "1.0"
    version_a = Version("0.9999999")
    version_b = Version(1, 0)
    assert version_a.is_greater_than(version_b) == False
    assert version_a.is_less_than(version_b) == True
    assert version_a.is_equal_to(version_b) == False

def test_case_7():
    # "99999.999999" is less than "100000.0"
    version_a = Version("99999.999999")
    version_b = Version(100000, 0)
    assert version_a.is_greater_than(version_b) == False
    assert version_a.is_less_than(version_b) == True
    assert version_a.is_equal_to(version_b) == False

def test_case_8():
    # "9999.12" is greather than "9999.2"
    version_a = Version("9999.12")
    version_b = Version(9999, 2)
    assert version_a.is_greater_than(version_b) == True
    assert version_a.is_less_than(version_b) == False
    assert version_a.is_equal_to(version_b) == False

def test_case_9():
    # "0.20" is greater than "0.3"
    version_a = Version("0.20")
    version_b = Version(0, 3)
    assert version_a.is_greater_than(version_b) == True
    assert version_a.is_less_than(version_b) == False
    assert version_a.is_equal_to(version_b) == False

def test_case_10():
    # "0.1" is equal to "0.1"
    version_a = Version("0.1")
    version_b = Version(0, 1)
    assert version_a.is_greater_than(version_b) == False
    assert version_a.is_less_than(version_b) == False
    assert version_a.is_equal_to(version_b) == True
