import setuptools

def readme():
    try:
        with open("README.md") as f:
            return f.read()
    except IOError:
        return ""


setuptools.setup(
    name="psgtray",
    version="6.0",
    author="PySimpleGUI",
    install_requires=["PySimpleGUI","pystray<=0.18.0","pillow"],
    python_requires=">=3.6",
    description="A System Tray Icon that works with the PySimpleGUI tkinter port.  Uses pystray to supply the system tray.  Works well under Windows.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="GUI UI PySimpleGUI tkinter systemtray pystray",
    url="https://github.com/PySimpleGUI/psgtray",
    packages=setuptools.find_packages(),
    license='GNU Lesser General Public License v3 (LGPLv3)',
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Framework :: PySimpleGUI",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: User Interfaces",
    ),
    package_data={"":
                      ["*", "*.*"]
                  },
    entry_points={"gui_scripts": [
        "psgtray=psgtray.psgtray:main"
    ], },
)

