from .base import *

DEBUG = False

ALLOWED_HOSTS = ['	http://ec2-54-213-252-3.us-west-2.compute.amazonaws.com'] 

try:
    from .local import *
except ImportError:
    pass
