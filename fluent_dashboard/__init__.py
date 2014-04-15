# following PEP 386
__version__ = "0.3.6"

# Do some sane version checking
import admin_tools

# admin-tools 0.4.0 is the base API.
# admin-tools 0.4.1 fixes static files support for Django 1.3.
if tuple(admin_tools.VERSION.split('.')) < (0,4,0):
    raise ImportError("At least Django admin_tools 0.4.0 is required to run this application")
