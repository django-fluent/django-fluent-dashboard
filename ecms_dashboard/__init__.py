VERSION = (0, 1, 0)

# Do some sane version checking
import admin_tools

if tuple(admin_tools.VERSION.split('.')) < (0,4,0):
    raise ImportError("At least Django admin_tools 0.4.0 is required to run this application")
