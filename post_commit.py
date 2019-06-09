#!/usr/bin/env python3
from os.path import exists, isfile
from sermantic_versioning import Version


def increment_version():
    """
    Waypoint 7: Increment Version on Git Commit
    - When changes are committed to the Git repository,
    the script automatically increments the patch number
    of a semantic versioning 3-component number (at least 1)
    stored in a file VERSION located at the root folder of a Git repository.
    - If this file VERSION doesn't initially exist,
    the script creates it and stores the version 1.0.1
    (the script assumes that the initial version before the commit is 1.0.0).
    - You can install your script file, with the proper name,
    into the hooks folder of your Git repository to check whether
    it works successfully.
    """
    try:
        # Check if VERSION file existed
        if exists("VERSION"):
            # Check is it file?
            if isfile("VERSION"):
                with open("VERSION", 'r+') as f:
                    # Get content of file
                    content_file = f.read()
                    # Get version of a file
                    version = Version(content_file)
                    # Plus patch element to one
                    version.patch += 1
                    # Take cursor to head of file
                    f.seek(0)
                    # Cut size of file
                    f.truncate()
                    # Write version into file
                    f.write(str(version))
        # If file did not exist, create new file and write
        else:
            with open("VERSION", 'w+') as f:
                f.write('1.0.1')
    # Throw error
    except OSError:
        print("Throw error when access to VERSION")
    # Check error of user input
    except TypeError:
        print("%s is not a valid version input") % (content_file)


if __name__ == "__main__":
    increment_version()
