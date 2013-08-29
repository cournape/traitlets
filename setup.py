from distutils.core import setup

VERSION = "0.0.1.dev"

if __name__ == "__main__":
    fp = open("_version.py", "wt")
    try:
        fp.write("version = \"%s\"" % (VERSION,))
    finally:
        fp.close()

    setup(name="traitlets",
          author="David Cournapeau",
          author_email="David Cournapeau",
          install_requires=["six"],
          maintainer="David Cournapeau",
          maintainer_email="David Cournapeau",
          packages=["traitlets",
                    "traitlets.tests",
                    ],
          version=VERSION,
          license="BSD",
    )
