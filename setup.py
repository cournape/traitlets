from distutils.core import setup

from traitlets import __version__

if __name__ == "__main__":
    setup(name="traitlets",
          author="David Cournapeau",
          author_email="David Cournapeau",
          maintainer="David Cournapeau",
          maintainer_email="David Cournapeau",
          packages=["traitlets",
                    "traitlets.tests",
                    ],
          version=__version__,
          licent="BSD",
    )
