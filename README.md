[![GitHub](https://img.shields.io/github/license/axi0m/violent_python?color=bright-green&style=flat-square)](https://github.com/axi0m/violent_python/blob/master/LICENSE.md)
![GitHub last commit](https://img.shields.io/github/last-commit/axi0m/violent_python?style=flat-square)
![Maintenance](https://img.shields.io/maintenance/yes/2020?style=flat-square)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/axi0m/violent_python.svg?logo=lgtm&logoWidth=18&style=flat-square)](https://lgtm.com/projects/g/axi0m/violent_python/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/axi0m/violent_python.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/axi0m/violent_python/context:python)
[![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Updates](https://pyup.io/repos/github/axi0m/violent_python/shield.svg)](https://pyup.io/repos/github/axi0m/violent_python/)
[![Python 3](https://pyup.io/repos/github/axi0m/violent_python/python-3-shield.svg)](https://pyup.io/repos/github/axi0m/violent_python/)

# Violent Python

Selection of various scripts from TJ O'Connor's Violent Python by Syngress. The scripts tend to be targeted at specific security related needs, including:

1. Dictionary attack based zip file cracker
2. Rudimentary vulnerability scanner
3. Offline Linux password cracker (dictionary based)
4. SSH Botnet

## Getting Started

Please don't use this repo for anything legitimate. You're free to copy the code, clone it, and modify it (see license)
but I'd rather you buy TJ O'Connor's book and do the exercises/projects yourself.

However, if you decide you want to use the code, you're welcome to do so, and you're even welcome to submit PR's and issues, just do not expect a ton of support as this is just side project work I use to learn and improve my security and Python skills.

### Prerequisites

- Python 3.6+
- git
- pipenv (if you want to use the pip lock file)

### Using/Installing

Please don't. I expect much of this not to work.

Ensure you have the required components.
Navigate to your preferred clone directory (/usr/local/src/ or /opt/ in Linux or wherever you want in Windows)

```bash
git clone https://github.com/axi0m/violent_python.git
```

```bash
pipenv install
python <filename>.py
```

## Testing

```bash
pipenv install --dev
python -m pytest
```

### Testing Coverage

```bash
pipenv install --dev
python -m pytest --cov
```

## Coding Style

[Black](https://github.com/psf/black) and [PEP8](https://www.python.org/dev/peps/pep-0008/)

## Deployment

I do not recommend you use this code on a live system, this was created purely to host my code as I learned more about Python

## Built With

- [Pipenv](https://pipenv.readthedocs.io/en/latest/) - Package management and virtual environment handling
- [VSCode](https://code.visualstudio.com/) - IDE from Microsoft

## Contributing

This isn't a repo maintained for necessariliy contributing and improving the content. I am sharing this just to host
an external copy of the effort as I go through TJ's book.

If you want to contribute, I recommend you fork it and do with it what you will.

## Versioning

No specific versioning system/format defined/selected.

## Author(s)

axi0m

## License

This project is licensed under MIT license - see the [LICENSE.md](https://github.com/axi0m/violent_python/blob/master/LICENSE.md) file for details.

## Acknowledgements

1. Syngress for publishing the book Violent Python
2. TJ O'Connor for writing the book and doing the hard work of coming up with all the examples and sharing his years of
knowledge with his readers.
