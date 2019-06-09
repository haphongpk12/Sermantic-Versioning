#!/usr/bin/env python3


def convert_string_to_version_component_numbers(s):
    """
    Waypoint 1: Convert a Semantic Versioning Component Number String
                to a Tuple
        - If only 1-component number is given,
        the function returns minor and patch equal to 0.
    @param: s -> a string representation of
                 a semantic versioning 3-component number (at least 1)
    @return: a tuple composed of 3 integers (major, minor, patch)
    """
    # Check error if input is not string of version
    if not isinstance(s, str):
        raise ValueError("Please input string of version, not another type")
    # Split the string with "." into a list
    str_split = s.split(".")
    # Check if element is not number or not positive
    if all(not x.isnumeric() for x in str_split):
        raise ValueError("Please input version string with positive number")
    # Change all str type number to int
    for i in range(len(str_split)):
        str_split[i] = int(str_split[i])
    # Return final tuple with major, minor, path
    return tuple(str_split[:len(str_split)] + \
        [0 for _ in range(3 - len(str_split))])


def compare_versions(this, other):
    """
    Waypoint 2: Compare Versions
    @param: this, other -> both tuples composed of
            3 integers (major, minor, patch)
    @return:
        1 if this is above other;
        0 if this equals other;
        -1 if this is below other.
    """
    # Check if input is not tuple
    if not isinstance(this, tuple) or not isinstance(other, tuple):
        raise ValueError("Please input tuple of version, not another type")
    # Check if element in tuple is not positive
    if all(x < 0 for x in this):
        raise ValueError("Please input version string with \
            positive number in first tuple")
    elif all(y < 0 for y in other):
        raise ValueError("Please input version string with \
            positive number in second tuple")
    # Return result with given criteria
    return 1 if this > other else 0 if this == other else -1


class Version:
    """
    Waypoint 3: Write a Class Version
    - Class Version which class construction, also known
        as initialization method, accepts:
        + A string representation of a semantic versioning
        + From 1 to 3 integers representing, in that particular order
        3-component number (at least 1);
            major, minor, and patch;
        + A tuple from 1 to 3 integers representing, in that particular order
            major, minor, and patch: (major[, minor[, patch]]).
    - If minor and patch are not specified, their default value is 0.
    """
    def __init__(self, major, minor: int=0, patch: int=0):
        # Check for the case with 3 integers input
        if all(isinstance(x, int) for x in (major, minor, patch)):
            self.major = major
            self.minor = minor
            self.patch = patch
        # Check with string of version input
        elif isinstance(major, str):
            self.major, self.minor, self.patch = \
                convert_string_to_version_component_numbers(major)
        # Check with tuple of version input
        elif isinstance(major, tuple):
            # Change tuple to list to plus zero number, after return to tuple
            self.major, self.minor, self.patch = \
                tuple(list(major)[:len(major)] + \
                    [0 for _ in range(3 - len(major))])
        # Get final tuple with major, minor, path
        self.final_tup = (self.major, self.minor, self.patch)

    def __repr__(self):
        """
        Waypoint 4: Compute "Official" String Representations
        - Write the instance method __repr__ to compute
        the “official” string representation of a Version object
        @return: a string that yields an object with the same value
                as when we pass it to the Python built-in eval, i.e.,
                a string representation of a valid Python expression
                that could be used to recreate an object with the same value.
        """
        return "Version(%s, %s, %s)" % (self.major, self.minor, self.patch)

    def __str__(self):
        """
        Waypoint 5: Compute "Informal" String Representation
        - Write the instance method __str__ to compute the "informal" or
        nicely printable string representation of a Version object.
        """
        return "%s.%s.%s" % (self.major, self.minor, self.patch)

    """
    Waypoint 6: Compare Version Instances
    - Write the "rich comparison" instance methods
    to allow comparing two Version instances.
    """
    def __lt__(self, other):
        """
        Compare less than "<"
        """
        # Using compare_versions function to compare with other Version
        return compare_versions(self.final_tup, other.final_tup) == -1

    def __eq__(self, other):
        """
        Compare equal "=="
        """
        # Using compare_versions function to compare with other Version
        return compare_versions(self.final_tup, other.final_tup) == 0

    def __gt__(self, other):
        """
        Compare great than ">"
        """
        # Using compare_versions function to compare with other Version
        return compare_versions(self.final_tup, other.final_tup) == 1


def main():
    """
    Main function: This function will execute many other function
    """
    version_after_convert = convert_string_to_version_component_numbers("1.2.3")
    compare_this_other = compare_versions((4, 2, 1), (2, 3, 4))
    version = Version(1, 3)
    print(version_after_convert)
    print(version.final_tup)
    print(Version("1.2.8") < Version("2.4.5"))


if __name__ == "__main__":
    main()
