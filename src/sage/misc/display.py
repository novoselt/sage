"""
Generic display mechanism for Sage.
"""
#*****************************************************************************
#       Copyright (C) 2014 Jason Grout <jason-sage@creativetrax.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

def register(kind, function):
    old_func = _HANDLERS.get(kind, None)
    _HANDLERS[kind]=function
    return old_func

def is_registered(kind):
    return _HANDLERS.get(kind, None) is not None

def run_handler(kind, *args, **kwds):
    f = _HANDLERS.get(kind, None)
    if f is not None:
        return f(*args, **kwds)

def display_html(s):
    return run_handler('html', s)

def display_jmol(path):
    return run_handler('jmol', path)

def display_canvas3d(path):
    return run_handler('canvas3d', path)

def display_image(path):
    return run_handler('image', path)

def image_link(path):
    return run_handler('image_link', path)

def display_file(path, mimetype=None):
    return run_handler('file', path, mimetype)

def _default_file(path, mimetype=None):
    if mimetype is None:
        print path
    else:
        print "%s (%s)"%(path, mimetype)

_HANDLERS = {'file': _default_file}

def _notebook_html(s):
    print "<html>%s</html>"%s

def _notebook_image_link(s):
    return '<img src="cell://%s">'%s

def _notebook_image(s):
    display_html(image_link(s))
