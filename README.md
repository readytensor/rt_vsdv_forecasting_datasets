# Forecasting Survey Project Datasets

This repository contains the scripts to create the datasets requiered for the project

## Overview

The repository contains the following directories:

- **config**: Contains configuration files required for running the scripts.

- **datasets**: Contains all datasets files. It is further divided into:
  - **/raw**: Contains the notebooks to preprocess each dataset into the requiered format.
  - **/processed**: This folder contains the base datasets that are used for initial forecasting experiments. Each dataset within this folder represents a unique time-series data set intended for direct forecasting applications.
  - **/variations**: This folder hosts variations of the original datasets found in the processed/ directory. These variations are designed to analyze the impact of historical data length on the quality of forecasts.


## Variations Datasets
The datasets within the variations folder follow a specific naming convention to reflect the modifications made to the original datasets. 
The naming format is: 
```
original_dataset_name_ratio_{variation}
```

Where:

* original_dataset_name: Refers to the name of the base dataset from the processed folder that this variation is derived from.
* variation: A numerical label (2, 4, 6, 8, 10) that indicates the ratio used in the dataset preparation. The variation number designates the ratio of the total number of observations in the dataset to the forecast length.


### Example
For instance, if you have a base dataset named `temperature` in the processed folder, a corresponding variation in the variations folder might be named `temperature_ratio_4`. This indicates that the dataset `temperature` has been modified such that the total number of observations is four times the length of the forecast period. This setup allows researchers to assess how different lengths of historical data affect the accuracy and effectiveness of their forecasting models.

## Usage

1. Create virtual environment and install dependencies in `requirements.txt`.
2. Run the script `run_all.py` to create the variations dataset

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

TBD.
