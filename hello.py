# Step 1: Settngs Configuration
# import sys
#
# from django.conf import settings
#
# settings.configure(
#     DEBUG=true,
#     SECRET_KEY='thisisabadkeybutitwilldo',
#     ROOT_URLCONF=sys.modules[__name__],
# )
#

# Step 2: URL Configuration

# import sys
#
# from django.conf import settings 
# from django.conf.urls import patterns
# 
# settings.configure(
#     DEBUG=True,
#     SECRET_KEY='thisisabadkeybutitwilldo',
#     ROOT_URLCONF=sys.modules[__name__],
# )
# 
# urlpatterns = patterns('',
#     (r'^hello-world/$', index),
# )

# Step 3 View Configuration
# import sys
#
# from django.conf import settings 
# from django.conf.urls import patterns
# from django.http import HttpResponse
#
# settings.configure(
#     DEBUG=True,
#     SECRET_KEY='thisisabadkeybutitwilldo',
#     ROOT_URLCONF=sys.modules[__name__],
# )
#
# def index(request):
#     return HttpResponse('Hello, World')
#
# urlpatterns = patterns('',
#     (r'^hello-world/$', index),
# )


#Step 4: Enable command line support

import sys

from django.conf import settings 
from django.conf.urls import patterns
from django.http import HttpResponse
from django.core.management import execute_from_command_line

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisabadkeybutitwilldo',
    ROOT_URLCONF=sys.modules[__name__],
)

def index(request):
    return HttpResponse('Hello, World')

urlpatterns = patterns('',
    (r'^hello-world/$', index),
)

if __name__ == "__main__":
    execute_from_command_line(sys.argv)

