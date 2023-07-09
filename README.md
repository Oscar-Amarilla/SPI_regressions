# [SPI_regressions](https://github.com/Oscar-Amarilla/SPI_regressions)

by Oscar Amarilla, 2023

[SPI_regressions](https://github.com/Oscar-Amarilla/SPI_regressions) is a project where different linear models that predict the [Standardized Precipitation Index](https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-index-spi) (SPI) values from various meteorological stations in Paraguay are sought. The stepwise linear regression technique is applied to the [Multivariate ENSO Index](https://psl.noaa.gov/enso/mei/) (MEI) values to obtain these models.

The scripts needed for the stepwise linear regression are exported from the [Stepwise_linear_regression_python](https://github.com/Oscar-Amarilla/Stepwise_linear_regresion_python) repository. Both the linear_regression.py and stepwise_regression.py files are needed and they must be placed in the scr directory.

You are free to copy, modify, and distribute this project, even for commercial purposes, without asking for permission. Please adapt this project for your own needs even if your data has nothing to do with meteorology. See *[Public domain dedication](https://github.com/ddbeck/readme-checklist#public-domain-dedication)* for details.

## How does [SPI_regressions](https://github.com/Oscar-Amarilla/SPI_regressions) works?

The project consist in a series of scripts that follows an **ELT** _(extract-load-transform)_ scheme to organize data about the different SPI values of meteorological stations from Paraguay and the MEI values.

The structure of the project is the following:

```
|--input/ (Input data)
|
|--src/
|    |
|    |- config.py (Path to necessary files for the project and settings for the extract_and_load script)
|    |
|    |- extract_and_load.py (Process of extraction and load of data in the workspace)
|    |
|    |- data_utils.py (Utility functions)
|    |
|    |- plots.py (Plots generator)
|
|-- regression.ipynb (Notebook with the project) 
|
|-- requirements.txt (List of necessary dependencies)
|
|__ README.md 
```

The user may take a look at the notebook, where the project has been explained in further details an could be a little more easy to follow.

## How to run [SPI_regressions](https://github.com/Oscar-Amarilla/SPI_regressions)?

First thing to do is to generate a python virtual environnment in a bash terminal.
```bash
python -m venv here_goes_the_name_of_the_venv # The name of the venv is up to the user.
```
Activate the virtual environment
```bash
source name_of_the_venv/bin/activate
```
Then install the requirements listed in the requirements.txt using pip.
```bash
pip install -r requirements.txt
```
Then the project can be run in the notebook. In the terminal, go to the notebook directory and run the notebook and open it.
```bash
jupyter notebook
```
## Contributing to [SPI_regressions](https://github.com/Oscar-Amarilla/SPI_regressions)

Every comment and/or suggestion for improving [SPI_regressions](https://github.com/Oscar-Amarilla/SPI_regressions) will be very welcome, so every user is cordially invited to [open an issue or pull request on GitHub](https://github.com/Oscar-Amarilla/SPI_regressions/issues).

## Public domain dedication

This work is dedicated to the [public domain (CC0 1.0)](https://creativecommons.org/publicdomain/zero/1.0/). To the extent possible under law, Oscar Amarilla has waived all copyright and related or neighboring rights to the README checklist. See the LICENSE file for all the legalese.