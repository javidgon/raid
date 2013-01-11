import os
import sys
import glob

def get_file(filename):
    """
    Search project's files from site-packages.
    """
    python_bin = os.path.dirname(sys.executable)
    python_lib = os.path.join(python_bin, '..', 'lib/')
    python_version = glob.glob(os.path.join(python_lib + 'python*'))
    return os.path.join(python_version[0], 'site-packages/raid/%s' % filename)