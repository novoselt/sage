"""
Pager for showing strings
"""

#############################################################################
#       Copyright (C) 2006 William Stein <wstein@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#
#                  http://www.gnu.org/licenses/
#############################################################################

# Currently we just use the IPython pager when not in embedded mode.
# If we want to use something else, we can just change this function.
# Any code in sage that uses a pager should use this pager.


def cat(x):
    print(x)

def pager():
    from sage.misc.misc import EMBEDDED_MODE
    if EMBEDDED_MODE:
        return cat
    else:
        import IPython.core.page
        return IPython.core.page.page
