# ft_package

A simple Python package that provides list manipulation utilities.

## Installation

You can install the package using pip:

```bash
pip install hatchling build
python -m build
```

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

# Count occurrences of an element in a list
print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
