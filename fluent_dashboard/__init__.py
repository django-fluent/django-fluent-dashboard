# following PEP 386
__version__ = "0.4"

# Do some sane version checking
import admin_tools

if tuple(admin_tools.VERSION.split('.')) < (0,5,1):
    raise ImportError("At least Django admin_tools 0.5.1 is required to run this application")
