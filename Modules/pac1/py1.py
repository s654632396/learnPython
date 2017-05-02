# -*- coding : utf-8 -*-

from mod1 import test
from mod2 import test as test2
test()
test2()
import os
print os.path.isdir('/home/haruharu/')
print os.path.isfile('/home/software/nginx')

# import something   #ImportError: No module named something

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python' : 2.7})
