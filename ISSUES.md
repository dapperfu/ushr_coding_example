# Issues

## [redacted] module not installed.

Following the conda instructions doesn't add the ```[redacted]``` module to Python:

    $ python -c 'import [redacted]'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named '[redacted]'

**Fix**:

Create ```setup.py``` for the [redacted] module.

Install the module with pip:

    pip install modules/python/[redacted]/

Install the module for development:

    pip install --editable modules/python/[redacted]/

```[redacted]``` module can now be imported in the conda environment.

    $ python
    Python 3.6.6 |Anaconda, Inc.| (default, Jun 28 2018, 17:14:51)
    [GCC 7.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import [redacted]
    >>>


## PEP8 Violations:

>  We adhere to pep8, except we use a max line width of 120 characters and do not use E123 or E124.

    $ pycodestyle --statistics --max-line-length=120 --ignore=E123,E124 modules/python/[redacted]/
    [redacted]
    22      E265 block comment should start with '# '
    1       E501 line too long (170 > 120 characters)

    $ pycodestyle --statistics --max-line-length=120 --ignore=E123,E124 examples/coordinate_systems/
    [redacted]
    3       E128 continuation line under-indented for visual indent
    28      E231 missing whitespace after ','
    3       E261 at least two spaces before inline comment
    2       E265 block comment should start with '# '
    6       E501 line too long (265 > 120 characters)
    2       W291 trailing whitespace

**Optional**:

Add [```pycodestyle```](http://pycodestyle.pycqa.org/en/latest/intro.html#configuration) configuration section to ```setup.cfg``` so that you can just call ```pycodestyle```:

    [pycodestyle]
    ignore = E123,E124
    max_line_length = 120

## numpy docstring issues:

>  We use [numpydoc docstrings](<https://numpydoc.readthedocs.io/en/latest/> "numpydoc docstrings").

    $ pydocstyle --convention=numpy modules/python/[redacted]/
            D100: Missing docstring in public module
            D400: First line should end with a period (not 'n')
            D412: No blank lines allowed between a section header and its content ('Parameters')
            D412: No blank lines allowed between a section header and its content ('Returns')
            D205: 1 blank line required between summary line and description (found 0)
            D400: First line should end with a period (not 'n')
            D412: No blank lines allowed between a section header and its content ('Notes')
            D412: No blank lines allowed between a section header and its content ('Parameters')
            D412: No blank lines allowed between a section header and its content ('Returns')
            D205: 1 blank line required between summary line and description (found 0)
            D400: First line should end with a period (not 's')
            D412: No blank lines allowed between a section header and its content ('Parameters')
            D412: No blank lines allowed between a section header and its content ('Returns')
            D200: One-line docstring should fit on one line with quotes (found 3)
            D100: Missing docstring in public module
            D205: 1 blank line required between summary line and description (found 0)
            D400: First line should end with a period (not 's')
            D412: No blank lines allowed between a section header and its content ('Parameters')
            D412: No blank lines allowed between a section header and its content ('Returns')
            D100: Missing docstring in public module
            D200: One-line docstring should fit on one line with quotes (found 3)
            D100: Missing docstring in public module
            D103: Missing docstring in public function
            D100: Missing docstring in public module
            D205: 1 blank line required between summary line and description (found 0)
            D400: First line should end with a period (not 's')
            D202: No blank lines allowed after function docstring (found 1)


    $ pydocstyle --convention=numpy examples/[redacted]/
            D205: 1 blank line required between summary line and description (found 0)
            D400: First line should end with a period (not 'x')

**Fix:**

Correct all issues until ```pydocstyle``` reports no errors.

## ```cython``` required for some modules:

Two modules require ```cython```. ```pip``` throws this 'warning' in red when ever ```pip``` is run.

    mkl-random 1.0.1 requires cython, which is not installed.
    mkl-fft 1.0.4 requires cython, which is not installed.

**Fix**:

Add ```cython``` to ```requirements.yaml```.

## AttributeError: module '[redacted]' has no attribute '[redacted]'

```[redacted]``` function is misspelled in ```[redacted]```

**Fix**:

[Assume that it is supposed to be **transform**]

1. Fix spelling to ```[redacted]``` in ```[redacted]```
2. Correct all calls to ```[redacted]``` in ```[redacted]```




```
    $ find . -name "*.py" | xargs  grep tranform
    ./modules/python/[redacted]/coord/homogeneous.py:def tranform(X, M):
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    out = h.tranform(i, np.identity(4))
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    out = h.tranform(i, np.identity(4))
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    out = h.tranform(i, np.identity(4))
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    out = h.tranform(i, np.identity(4))
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    out = h.tranform(i, np.identity(4))
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    out = h.tranform(i, np.identity(4))
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    ox, oy, oz = h.tranform((x, y, z), np.identity(4))
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    ox, oy, oz = h.tranform((x, y, z), np.identity(4))
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    ox, oy, oz = h.tranform((x, y, z), np.identity(4))
    ./modules/python/[redacted]/coord/unittests/test_homogeneous.py:    ox, oy, oz = h.tranform((x, y, z), np.identity(4))
```

## pytest failures

### Error 1:


    =============================================== FAILURES ===============================================
    ______________________________________________ test_toLLA ______________________________________________

        def test_toLLA():
    >       assert np.allclose(ecef.toLLA(list(unpacked_ecef)), packed_lla)
    E       assert False
    E        +  where False = <function allclose at 0x7fa6e2ecb378>(array([[-84.340086,  42.825226, 281.6     ],\n       [-84.400486,  42.685745, 258.8     ]]), array([[ 42.825226, -84.340086, 281.6     ],\n       [ 42.685745, -84.400486, 258.8     ]]))
    E        +    where <function allclose at 0x7fa6e2ecb378> = np.allclose
    E        +    and   array([[-84.340086,  42.825226, 281.6     ],\n       [-84.400486,  42.685745, 258.8     ]]) = <function toLLA at 0x7fa6e3f38d08>([[462088.79153139, 458198.17060913], [-4662537.62772459, -4673474.62537624], [4313473.17203725, 4302080.14183838]])
    E        +      where <function toLLA at 0x7fa6e3f38d08> = ecef.toLLA
    E        +      and   [[462088.79153139, 458198.17060913], [-4662537.62772459, -4673474.62537624], [4313473.17203725, 4302080.14183838]] = list(([462088.79153139, 458198.17060913], [-4662537.62772459, -4673474.62537624], [4313473.17203725, 4302080.14183838]))

    modules/python/[redacted]/[redacted]/coord/unittests/test_ecef.py:24: AssertionError


**Fix:**

Swap first & second columns of ```packed_lla.```

### Error 2:

See debug/test_ecef_error.pdf for more details.

    =============================================== FAILURES ===============================================
    _____________________________ test_create_local_model_matrix_real_z_value ______________________________

        def test_create_local_model_matrix_real_z_value():
            out = np.array([[9.27364962e-01, -1.07851592e-02, 8.47464301e-02, 3.00000000e+01],
                            [-7.20749970e-03, 9.13925013e-01, 1.69492860e-01, 4.00000000e+01],
                            [-9.12949962e-02, -1.81706487e-01, 8.47464301e-01, 2.00000000e+01],
                            [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
            M = h.create_local_model_matrix(heading_vector=[.1, 4, .7], up_vector=[.3, .6, 3.], origin=[30, 40, 20])
    >       assert np.allclose(M, out)
    E       assert False
    E        +  where False = <function allclose at 0x7fa6e2ecb378>(array([[ 2.85079893e+00,  2.46182982e-02,  2.72545455e-01,\n         3.00000000e+01],\n       [-2.21564684e-02,  9.84731...18e+00,\n         2.00000000e+01],\n       [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,\n         1.00000000e+00]]), array([[ 9.27364962e-01, -1.07851592e-02,  8.47464301e-02,\n         3.00000000e+01],\n       [-7.20749970e-03,  9.13925...01e-01,\n         2.00000000e+01],\n       [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,\n         1.00000000e+00]]))
    E        +    where <function allclose at 0x7fa6e2ecb378> = np.allclose

    modules/python/[redacted]/[redacted]/coord/unittests/test_homogeneous.py:61: AssertionError
    ================================= 2 failed, 20 passed in 0.27 seconds ==================================

**Fix:**

1. Normalize up_vector.
2. Correctly re-calculate Y vector.

See debug/test_homogeneous_error.pdf for more details.
