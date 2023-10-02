import sys

from add import add_package;
from modify import modify_package

if len(sys.argv) == 1:
    # Add package operation
    add_package()
elif sys.argv[1] == "modify":
    # Modify package operation
    modify_package()