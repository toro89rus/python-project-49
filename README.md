### Hexlet tests and linter status:
[![Actions Status](https://github.com/toro89rus/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/toro89rus/python-project-49/actions)

### CodeClimate maintainability Badge:
[![Maintainability](https://api.codeclimate.com/v1/badges/0eac92deb91a8a7b53a7/maintainability)](https://codeclimate.com/github/toro89rus/python-project-49/maintainability)

# Brain Games
Test your logic and mathematical skills in 5 different games.
- Brain - Calc: Find the result of an expression (use brain-calc to run)
- Brain - Even: Define if the number is even (use brain-even to run)
- Brain - GCD: Find the greatest common divisor of two numbers (use brain-gcd to run)
- Brain - Prime: Define if the number is prime (use brain-prime to run)
- Brain - Progression: Find the missing element in progression (use brain-calc to run)


## Requirements
- Python 3.09
- Poetry
- make
- pip

For Debian 12+ or Ubuntu 23 +:
- venv or pipx (read installation for details)

## How to install
```
git clone git@github.com:toro89rus/python-project-49.git
make build
make package-install
```

Due to limitations of using pip to install (including install --user) packages on Debian 12+ or Ubuntu 23+ (see [details](https://packaging.python.org/en/latest/specifications/externally-managed-environments/#externally-managed-environments)) there are two ways of installing Brain Games if you are are using one of these operation systems:
- using virtual enviroment. Make sure venv is [installed in your system](https://virtualenv.pypa.io/en/latest/installation.html). Don't forget to activate your venv before installation.

```
git clone git@github.com:toro89rus/python-project-49.git
make build
make package-install-venv
```

- if you don't know how to use venv, you can install Brain Games via pipx, which will automatically create a virtual environment for you and install Brain Games there. Make sure pipx is [installed in your system](https://pipx.pypa.io/stable/installation/)

```
git clone git@github.com:toro89rus/python-project-49.git
make build
make package-install-pipx
```

#How to uninstall
Use one of these commands according to the one you used for installation:

```
make package-uninstall
```

```
make package-uninstall-venv
```

```
make package-uninstall-pipx
```


### ASCIINEMA brain-even
[![asciicast](https://asciinema.org/a/ZcKBL4BOzL3Kf9uOdWLLiiFac.svg)](https://asciinema.org/a/ZcKBL4BOzL3Kf9uOdWLLiiFac)

### ASCIINEMA brain-calc
[![asciicast](https://asciinema.org/a/Jq4HjG82pacJBDS04WtxtYZEB.svg)](https://asciinema.org/a/Jq4HjG82pacJBDS04WtxtYZEB)

### ASCIINEMA brain-gcd
[![asciicast](https://asciinema.org/a/NMZqFUNJHmPrye2Fnbd0z2sLa.svg)](https://asciinema.org/a/NMZqFUNJHmPrye2Fnbd0z2sLa)

### ASCIINEMA brain-progression
[![asciicast](https://asciinema.org/a/tAVwpaYyOOUZwMO5FmSOufTqG.svg)](https://asciinema.org/a/tAVwpaYyOOUZwMO5FmSOufTqG)


### ASCIINEMA brain-progression brain-prime
[![asciicast](https://asciinema.org/a/3dp9MhVpqR2FBmSWaQv1EJ05S.svg)](https://asciinema.org/a/3dp9MhVpqR2FBmSWaQv1EJ05S)