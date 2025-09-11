# Brain Games

## Hexlet tests and linter status

[![Actions Status](https://github.com/toro89rus/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/toro89rus/python-project-49/actions)

## CodeClimate maintainability Badge

[![Maintainability](https://api.codeclimate.com/v1/badges/0eac92deb91a8a7b53a7/maintainability)](https://codeclimate.com/github/toro89rus/python-project-49/maintainability)

## Description

Test your logic and mathematical skills in 5 different games.

- Brain - Calc: Find the result of an expression (use brain-calc to run)
- Brain - Even: Define if the number is even (use brain-even to run)
- Brain - GCD: Find the greatest common divisor of two numbers (use brain-gcd to run)
- Brain - Prime: Define if the number is prime (use brain-prime to run)
- Brain - Progression: Find the missing element in progression (use brain-calc to run)

## Requirements

for Docker usage:

- Docker

for local installation:

- Python 3.09
- uv
- make

## Docker Use

Make sure docker is [installed](https://docs.docker.com/engine/install/)

``` bash
docker run --rm -it toro89/brain_games:latest *game_name*
```

## How to install locally

Make sure uv is [installed](https://docs.astral.sh/uv/getting-started/installation/)

``` bash
git clone git@github.com:toro89rus/python-project-49.git
make build
make package-install
```

## How to uninstall

Use one of these commands according to the one you used for installation:

``` bash
make package-uninstall
```

### Brain-Even

[![asciicast](https://asciinema.org/a/CPOBdYlQhqucomlfZnK6woCf7.svg)](https://asciinema.org/a/CPOBdYlQhqucomlfZnK6woCf7)

### Brain-Calc

[![asciicast](https://asciinema.org/a/59E27Om0bXueNZVvgPRQnknQd.svg)](https://asciinema.org/a/59E27Om0bXueNZVvgPRQnknQd)

### Brain-GCD

[![asciicast](https://asciinema.org/a/kqu2RQAVpIU36a0Il3W38lWxx.svg)](https://asciinema.org/a/kqu2RQAVpIU36a0Il3W38lWxx)

### Brain-Progression

[![asciicast](https://asciinema.org/a/YZQCSKShHmorferGycLBnOa5m.svg)](https://asciinema.org/a/YZQCSKShHmorferGycLBnOa5m)

### Brain-Prime

[![asciicast](https://asciinema.org/a/szbC6XSRZrjQMnO8JjQiP7TUl.svg)](https://asciinema.org/a/szbC6XSRZrjQMnO8JjQiP7TUl)
