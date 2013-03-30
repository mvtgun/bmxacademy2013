import os
import sys

from settings import PROJECT_ROOT, normpath

sys.path.append(PROJECT_ROOT)

# BEGIN activacte virtualenv
try:
    activate_path = normpath(PROJECT_ROOT, 'env/bin/activate_this.py')
    execfile(activate_path, dict(__file__=activate_path))
except IOError:
    print "E: virtualenv must be installed to PROJECT_ROOT/env"
# END activacte virtualenv


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()