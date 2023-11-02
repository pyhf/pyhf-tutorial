# ---
# jupyter:
#   kernelspec:
#     display_name: Python (Pyodide)
#     language: python
#     name: python
# ---

# %% [markdown]
# # `pyhf` in the browser

# %% [markdown]
# * To run the code, click on the first cell (gray box) and press <kbd>Shift</kbd>+<kbd>Enter</kbd> or click on the (Run) ▶ button to run each cell.
# * Alternatively, from the `Run` menu select `Run All Cells`.

# %%
import micropip

# Install pyhf in the browser
await micropip.install(["pyhf==0.7.5", "matplotlib>=3.0.0"])
# %matplotlib inline
import pyhf

# You can now use pyhf!

# %% [markdown]
# Based on the way that Pyodide works with [third party packages](https://pyodide.org/en/stable/usage/packages-in-pyodide.html), you'll need to place the following cell at the top of each notebook that you'll use `pyhf` in.

# %%
import micropip

# Install pyhf in the browser
await micropip.install(["pyhf==0.7.5", "matplotlib>=3.0.0"])
