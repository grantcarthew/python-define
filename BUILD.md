# Build Instructions

Update the version in the `pyproject.toml` file.

```bash
python -m build
python -m twine upload --repository pypi dist/*
```

_Note: Username is `__token__` and the password is the PyPi API Token_

Reference: https://packaging.python.org/en/latest/tutorials/packaging-projects/

