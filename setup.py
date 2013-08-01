from distutils.core import setup

from traitlets import __version__

if __name__ == "__main__":
    setup(name="okonomiyaki",
          author="David Cournapeau",
          author_email="David Cournapeau",
          packages=["traitlets",
                    "traitlets.tests",
                    ],
          version=__version__
    )
