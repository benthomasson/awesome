"""
Load up the django settings in a normal python shell if available.  
This will give access to the django models and the database if
started from the root of a django application.

Copy this to your ~/.pythonrc file.
"""

try:
     from django.core.management import setup_environ
     import settings
     setup_environ(settings)
except:
    pass

