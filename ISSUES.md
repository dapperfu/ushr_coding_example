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



## pytest failures

### Error 1:

	[redacted]

**Fix:**

Swap first & second columns.

### Error 2:

	[redacted]

**Fix:**

1. Normalize up_vector.
2. Correctly re-calculate Y vector.
