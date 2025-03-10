# `pyhf` Tutorial

**The tutorial is based off of [`pyhf` `v0.7.6`](https://pypi.org/project/pyhf/0.7.6/)**

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyhf/pyhf-tutorial/main?urlpath=lab)
[![JupyterLite](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://pyhf.github.io/pyhf-tutorial/live/lab/index.html?path=jupyterlite.ipynb)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4670321.svg)](https://doi.org/10.5281/zenodo.4670321)

[![Deploy Jupyter Book](https://github.com/pyhf/pyhf-tutorial/actions/workflows/deploy-jupyter-book.yml/badge.svg)](https://pyhf.github.io/pyhf-tutorial/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pyhf/pyhf-tutorial/main.svg)](https://results.pre-commit.ci/latest/github/pyhf/pyhf-tutorial/main)

## Setup

### Using `pixi` (recommended)

On any `x86` Linux machine or any macOS machine first install [`pixi`](https://pixi.sh/) and then from the top level of the repository run

```
pixi install --environment book
```

### Using a manually controlled virtual environment

In a Python virtual environment run the following

```
python -m pip install --require-hashes --requirement book/requirements.lock
```

## Build

To build the book after setup simply run

### Using `pixi`

```
pixi run build
```

### Local virtual environment

```
make build
```

## Build lock file

To build a `uv pip compile` lock file for local use `nox`

```
nox
```

To build a lock file for deployment use Docker to avoid differences between operating systems with

```
bash lock.sh
```

or

```
nox --session docker
```

## Past tutorials

* [Computational HEP Traineeship Summer School 2023](https://indico.cern.ch/event/1293313/) (2023-07-26)
* [DANCE/CoDaS Workshop 2022](https://indico.cern.ch/event/1151329/) (2022-07-22)
* [PyHEP Topical Meeting April 2021](https://indico.cern.ch/event/985425/) (2021-04-07)
   - [![Zendo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4670322.svg)](https://doi.org/10.5281/zenodo.4670322)
* [LHC Reinterpretation Forum Workshop 2021](https://indico.cern.ch/event/982553/contributions/4219487/) (2021-02-18)
   - [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4549428.svg)](https://doi.org/10.5281/zenodo.4549428)
* [ATLAS Exotics + SUSY Workshop 2020](https://indico.cern.ch/event/898965/sessions/355806/) (2020-09-25)
* [PyHEP 2020](https://indico.cern.ch/event/882824/contributions/3931292/) (2020-07-16)
   - [![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4152916.svg)](https://doi.org/10.5281/zenodo.4152916)
