"""
Internal module for Django compatibility.
"""
import django

if django.VERSION >= (1, 7):
    def get_meta_model_name(opts):
        return opts.model_name
else:
    def get_meta_model_name(opts):
        return opts.module_name
