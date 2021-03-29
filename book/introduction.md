# [LHC Reinterpretation Forum Workshop 2021 `pyhf` Tutorial](https://indico.cern.ch/event/982553/contributions/4219487/)

## Welcome!

<p align="center">
<a href="https://github.com/scikit-hep/pyhf"><img src="https://raw.githubusercontent.com/scikit-hep/pyhf/master/docs/_static/img/pyhf-logo-small.png"></a>
</p>

Welcome to the `pyhf` tutorial given at the [LHC Reinterpretation Forum Workshop 2021](https://indico.cern.ch/event/982553)!
We'll first point you towards our documentation website ([pyhf.readthedocs.io/](https://pyhf.readthedocs.io/)) and recommend that you visit it for much more detailed explanations and examples.
Let's dive right in.


We won't review the full pedagogy of `HistFactory`, so instead we'll point you to
the [`pyhf` talk at SciPy 2020](https://github.com/matthewfeickert/talk-SciPy-2020).

<!-- http://www.get-youtube-thumbnail.com/ -->
[![SciPy 2020 talk YouTube](https://i3.ytimg.com/vi/FrH9s3eB6fU/maxresdefault.jpg)](https://youtu.be/FrH9s3eB6fU)

Instead, let's move to looking at the `pyhf` API right away.

## Installation

### Make a Virtual Environment

````{tabbed} Locally
```
$ python3 -m venv pyhf-tutorial
$ source pyhf-tutorial/bin/activate
(pyhf-tutorial) $ python -m pip install -U pip setuptools wheel
```
````

````{tabbed} On CC7 lxplus/tier-3

First we need to set up the 'views' with the right paths to ensure we use the correct `pip`

```
$ export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
$ source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh
$ lsetup "views LCG_96bpython3 x86_64-centos7-gcc8-opt"
$ export PYTHONPATH=/cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-centos7-gcc8-opt/python:/cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-centos7-gcc8-opt/lib
```

Then we can go ahead and create the virtual environment

```
$ python3 -m venv pyhf-tutorial
$ source pyhf-tutorial/bin/activate
(pyhf-tutorial) $ python -m pip install -U pip setuptools wheel
```
````

````{tabbed} On SLC6 lxplus/tier-3

First we need to set up the 'views' with the right paths to ensure we use the correct `pip`

```
$ export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
$ source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh
$ lsetup "views LCG_96bpython3 x86_64-slc6-gcc8-opt"
$ export PYTHONPATH=/cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-slc6-gcc8-opt/python:/cvmfs/sft.cern.ch/lcg/views/LCG_96bpython3/x86_64-slc6-gcc8-opt/lib
```

Then we can go ahead and create the virtual environment

```
$ python3 -m venv pyhf-tutorial
$ source pyhf-tutorial/bin/activate
(pyhf-tutorial) $ python -m pip install -U pip setuptools wheel
```
````

Once you have a virtual environment set up, you can use `source pyhf-tutorial/bin/activate` to get back into it again. Note the prefix `(pyhf-tutorial) $` on your command line, which indicates that you're inside a virtual environment named 'pyhf-tutorial'.

### Getting pyhf

If you haven't already, make a new Python 3 virtual environment and then install `pyhf` from either [PyPI](https://pypi.org/project/pyhf/) with `pip`

```
(pyhf-tutorial) $ python -m pip install pyhf
```

 or [Conda-forge](https://anaconda.org/conda-forge/pyhf)

```
(pyhf-tutorial) $ conda config --add channels conda-forge
(pyhf-tutorial) $ conda install pyhf
```

### Installation Extras

If you're installing from PyPI, you can also install with some of the "extras" that will be useful for doing typical HEP analysis workflows with `pyhf`.

````{tabbed} Read/Write XML+ROOT
```
(pyhf-tutorial) $ python -m pip install pyhf[xmlio]
```

The 'xmlio' extra additionally installs [`uproot`](https://github.com/scikit-hep/uproot) to read `ROOT` files.
````

````{tabbed} Use PyTorch and Tensorflow
```
(pyhf-tutorial) $ python -m pip install pyhf[torch,tensorflow]
```

The 'torch' extra installs [`pytorch`](https://pytorch.org/) and the 'tensorflow' extra installs [`tensorflow`](https://www.tensorflow.org/).
````

````{tabbed} Using Minuit Optimization
```
(pyhf-tutorial) $ python -m pip install pyhf[minuit]
```

The 'minuit' extra installs [`iminuit`](https://iminuit.readthedocs.io/).
````


See our [installation docs](https://pyhf.readthedocs.io/en/v0.6.1/installation.html) for more information about installation options.

### Dependencies for this tutorial

To get all the dependencies needed for this tutorial you can just install from the included `requirements.txt` in the top level `binder/` directory of [the source repository](https://github.com/pyhf/tutorial-Reinterpretation-Forum-2021)

```
(pyhf-tutorial) $ python -m pip install -r binder/requirements.txt
```

### Statistics References

For more information about some of the theoretical topics covered with `pyhf`, see Kyle Cranmer's [Statistics and Data Science](https://cranmer.github.io/stats-ds-book/intro.html) book.

### Questions and Further Information on `pyhf`

For more information on `pyhf` please check the [documentation website](https://pyhf.readthedocs.io/).
Additionally, if you have a question about the use of `pyhf` not covered in the documentation, please ask a question the `pyhf` [GitHub Discussions](https://github.com/scikit-hep/pyhf/discussions).
If you believe you have found a bug in `pyhf`, please report it in the [GitHub Issues](https://github.com/scikit-hep/pyhf/issues/new?template=Bug-Report.md&labels=bug&title=Bug+Report+:+Title+Here).
If you're interested in getting updates from the `pyhf` dev team and release announcements you can join the [`pyhf-announcements` mailing list](https://groups.google.com/group/pyhf-announcements/subscribe) (through Google Groups).
