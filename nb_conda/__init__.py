# flake8: noqa
from .handlers import load_jupyter_server_extension
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

def _jupyter_nbextension_paths():
    return [dict(section="notebook",
                 src="static",
                 dest="nb_conda",
                 require="nb_conda/main"),
            dict(section="tree",
                 src="static",
                 dest="nb_conda",
                 require="nb_conda/tree")]


def _jupyter_server_extension_paths():
    return [dict(module="nb_conda")]

