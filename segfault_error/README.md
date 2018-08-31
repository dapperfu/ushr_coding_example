# License

Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

# Issue

Running ```[redacted].py``` produces a Segmentation fault.

    (venv) jed@m6700:$ python [redacted].py
    Segmentation fault (core dumped)

Test env to reproduce:

- Ubuntu 18.04 x64
- Both *conda3 distributions.
  - Miniconda3-latest-Linux-x86_64.sh
  - Anaconda3-5.2.0-Linux-x86_64.sh
- ```pip freeze```:
  - atomicwrites==1.1.5
  - attrs==18.1.0
  - autopep8==1.3.4
  - certifi==2018.8.13
  - cycler==0.10.0
  - Cython==0.28.5
  - GDAL==2.3.0
  - matplotlib==2.0.2
  - mkl-fft==1.0.4
  - mkl-random==1.0.1
  - more-itertools==4.2.0
  - numpy==1.15.0
  - pluggy==0.7.1
  - py==1.5.4
  - pycodestyle==2.4.0
  - pydocstyle==2.1.1
  - PyOpenGL==3.1.  -
  - pyparsing==2.2.0
  - pyproj==1.9.5.1
  - pytest==3.7.1
  - python-dateutil==2.7.3
  - pytz==2018.5
  - six==1.11.0
  - snowballstemmer==1.2.1
  - tornado==5.1

Issue appears to be a Qt5 in conda: https://github.com/matplotlib/matplotlib/issues/9294/

# Fixes

**Fix 1**:

Explicitly define the backend as TkAgg or WebAgg:

	import matplotlib as mpl
	mpl.use('TkAgg')  # or whatever other backend that you want

Working backends:

	TkAgg
	WebAgg

**Fix 2**:

Install PyQt5 with ```pip``` after activating the conda environment. ```PyQt5``` isn't a conda package so adding it to ```requirements.yaml``` produces this error:

    conda env create -f requirements.yaml
    Solving environment: failed

    ResolvePackageNotFound:
      - pyqt5

**Fix 3**:

Don't use conda and use a vanilla Python virtual environment.

    python3 -mvenv /tmp/venv
    source /tmp/venv/bin/activate
    pip install -U pip wheel setuptools matplotlib==2.0.2 numpy
    python [redacted].py
