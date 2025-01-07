# `pyhf` Tutorial

## Welcome!

<p align="center">
<a href="https://github.com/scikit-hep/pyhf"><img src="https://raw.githubusercontent.com/scikit-hep/pyhf/main/docs/_static/img/pyhf-logo.svg" width="45%"></a>
</p>

Welcome to the `pyhf` tutorial!
We'll first point you towards our documentation website ([pyhf.readthedocs.io/](https://pyhf.readthedocs.io/)) and recommend that you visit it for much more detailed explanations and examples.
Let's dive right in.


We won't review the full pedagogy of `HistFactory`, so instead we'll point you to
the [`pyhf` talk at SciPy 2020](https://github.com/matthewfeickert/talk-SciPy-2020).

<!-- http://www.get-youtube-thumbnail.com/ -->
[![SciPy 2020 talk YouTube](https://i3.ytimg.com/vi/FrH9s3eB6fU/maxresdefault.jpg)](https://youtu.be/FrH9s3eB6fU)

Instead, let's move to looking at the `pyhf` API right away.

## Installation

### Make a Virtual Environment

::::{tab-set}

:::{tab-item} With pixi
```
$ pixi init
$ pixi shell
```
:::

:::{tab-item} With venv
```
$ python3 -m venv pyhf-tutorial
$ source pyhf-tutorial/bin/activate
(pyhf-tutorial) $ python -m pip install --upgrade pip
```
:::

:::{tab-item} With conda
```
$ conda create --name pyhf-tutorial --yes 'python=3.12'
$ conda activate pyhf-tutorial
```
:::

:::{tab-item} On EL9 LXPLUS/tier-3
First we need to set up the 'views' that [already have `pyhf` installed](https://lcginfo.cern.ch/pkg/pyhf/)

```
$ export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
$ . $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh
$ lsetup "views LCG_106 x86_64-el9-gcc13-opt"
```

Then we can install [`cvmfs-venv`](https://github.com/matthewfeickert/cvmfs-venv)

```
$ mkdir -p ~/.local/bin
$ export PATH=~/.local/bin:"${PATH}"
$ curl -sL https://raw.githubusercontent.com/matthewfeickert/cvmfs-venv/main/cvmfs-venv.sh -o ~/.local/bin/cvmfs-venv
$ chmod +x ~/.local/bin/cvmfs-venv
```

and use it to create a user controlled virtual environment

```
$ cvmfs-venv pyhf-tutorial
$ . pyhf-tutorial/bin/activate
(pyhf-tutorial) $ uv pip install --upgrade pip
```
:::

:::{tab-item} In your browser

As `pyhf` is pure Python it is possible to install and run a version of it directly in your browser using [Pyodide](https://pyodide.org/).
You can try out the live WebAssembly version of the user guide in [JupyterLite](https://jupyterlite.readthedocs.io/) now by visiting the [live view of the website](https://pyhf.github.io/pyhf-tutorial/live/lab/index.html?path=jupyterlite.ipynb).

Not all parts of this user guide are able to run in Pyodide, but the pure Python parts will work.

:::

::::

Once you have a virtual environment set up, you can use `source pyhf-tutorial/bin/activate` to get back into it again (or `pixi shell` for `pixi`). Note the prefix `(pyhf-tutorial) $` on your command line, which indicates that you're inside a virtual environment named 'pyhf-tutorial'.

### Getting pyhf

If you haven't already, make a new Python 3 virtual environment and then install `pyhf`

::::{tab-set}

:::{tab-item} pixi
from [conda-forge](https://anaconda.org/conda-forge/pyhf) with [`pixi`](https://pixi.sh/)

```
$ pixi add pyhf
```
:::

:::{tab-item} pip
from [PyPI](https://pypi.org/project/pyhf/) with `pip`

```
(pyhf-tutorial) $ python -m pip install pyhf
```
:::

:::{tab-item} conda
from [conda-forge](https://anaconda.org/conda-forge/pyhf) with [`conda`](https://docs.conda.io/)

```
(pyhf-tutorial) $ conda install --channel conda-forge pyhf
```
:::

::::

### Installation Extras

If you're installing from PyPI, you can also install with some of the "extras" that will be useful for doing typical HEP analysis workflows with `pyhf`.

::::{tab-set}

:::{tab-item} Read/Write XML+ROOT
```
(pyhf-tutorial) $ python -m pip install 'pyhf[xmlio]'
```

The 'xmlio' extra additionally installs [`uproot`](https://github.com/scikit-hep/uproot4) to read `ROOT` files.
:::

:::{tab-item} Use PyTorch and Tensorflow
```
(pyhf-tutorial) $ python -m pip install 'pyhf[torch,tensorflow]'
```

The 'torch' extra installs [`pytorch`](https://pytorch.org/) and the 'tensorflow' extra installs [`tensorflow`](https://www.tensorflow.org/).
:::

:::{tab-item} Using Minuit Optimization
```
(pyhf-tutorial) $ python -m pip install 'pyhf[minuit]'
```

The 'minuit' extra installs [`iminuit`](https://iminuit.readthedocs.io/).
:::

::::

See our [installation docs](https://pyhf.readthedocs.io/en/v0.7.6/installation.html) for more information about installation options.

### Dependencies for this tutorial

To get all the dependencies needed for this tutorial first clone the repository locally

```
(pyhf-tutorial) $ git clone https://github.com/pyhf/pyhf-tutorial.git
(pyhf-tutorial) $ cd pyhf-tutorial
```

#### Using `pixi`

then simply run

```
pixi install
```

or to also start running the example notebooks run

```
pixi run start
```

#### Using `pip`

then install from the included `requirements.txt` in the top level `binder/` directory of [the source repository](https://github.com/pyhf/pyhf-tutorial)

```
(pyhf-tutorial) $ python -m pip install --upgrade --requirement binder/requirements.txt
```

If you want to also get the dependencies to build and explore the Jupyter Book form of the tutorial you can install them with

```
(pyhf-tutorial) $ python -m pip install --upgrade --requirement book/requirements.txt
```

### Citation

`pyhf` `v0.6.0` and later makes it very easy to get the proper citation for the version of the library that you're using! Simply ask the CLI API to get the properly formatted BibTeX references.

```
(pyhf-tutorial) $ pyhf --citation
@software{pyhf,
  author = {Lukas Heinrich and Matthew Feickert and Giordon Stark},
  title = "{pyhf: v0.7.6}",
  version = {0.7.6},
  doi = {10.5281/zenodo.1169739},
  url = {https://doi.org/10.5281/zenodo.1169739},
  note = {https://github.com/scikit-hep/pyhf/releases/tag/v0.7.6}
}

@article{pyhf_joss,
  doi = {10.21105/joss.02823},
  url = {https://doi.org/10.21105/joss.02823},
  year = {2021},
  publisher = {The Open Journal},
  volume = {6},
  number = {58},
  pages = {2823},
  author = {Lukas Heinrich and Matthew Feickert and Giordon Stark and Kyle Cranmer},
  title = {pyhf: pure-Python implementation of HistFactory statistical models},
  journal = {Journal of Open Source Software}
}
```

Alternatively, [check the website](https://pyhf.readthedocs.io/en/v0.7.6/citations.html).

### Statistics References

For more information about some of the theoretical topics covered with `pyhf`, see Kyle Cranmer's [Statistics and Data Science](https://cranmer.github.io/stats-ds-book/intro.html) book.

### Questions and Further Information on `pyhf`

For more information on `pyhf` please check the [documentation website](https://pyhf.readthedocs.io/).
Additionally, if you have a question about the use of `pyhf` not covered in the documentation, please ask a question the `pyhf` [GitHub Discussions](https://github.com/scikit-hep/pyhf/discussions).
If you believe you have found a bug in `pyhf`, please report it in the [GitHub Issues](https://github.com/scikit-hep/pyhf/issues/new?template=Bug-Report.md&labels=bug&title=Bug+Report+:+Title+Here).
If you're interested in getting updates from the `pyhf` dev team and release announcements you can join the [`pyhf-announcements` mailing list](https://groups.google.com/group/pyhf-announcements/subscribe) (through Google Groups).
