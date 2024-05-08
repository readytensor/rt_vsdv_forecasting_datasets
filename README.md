# Forecasting Survey Project Datasets

This repository contains the scripts to create the datasets required for the **Forecasting Survey** project. The original datasets are preprocessed and converted into a format suitable for forecasting on the Ready Tensor platform. This project uses the original datasets and 5 variations derived from each dataset to analyze the impact of historical data length on the quality of forecasts from different forecasting models.

## Project Overview

The Forecasting Survey project contains 20 datasets, two of which are synthetically generated, and the other 18 are publicly sourced. There are 5 variations generated for each dataset. These variations are created by varying the ratio of the total number of observations in the history to the forecast length. The 5 scenarios are history lengths equal to 2, 4, 6, 8, and 10 times the forecast length. Collectively, there are 6 versions of each dataset: the original dataset and 5 variations. This repository contains the original raw datasets and all scripts required to generate processed files for each of the 6 versions of all datasets.

Processed files for the dataset versions are named with the following suffixes:

- `_ratio_max`: Original full dataset
- `_ratio_2`: Historical data length is truncated to be 2 times the forecast length
- `_ratio_4`: Historical data length is truncated to be 4 times the forecast length
- `_ratio_6`: Historical data length is truncated to be 6 times the forecast length
- `_ratio_8`: Historical data length is truncated to be 8 times the forecast length
- `_ratio_10`: Historical data length is truncated to be 10 times the forecast length

The following files are generated for each version of each dataset. `<dataset_name>` refers to the name of the dataset including the suffixes mentioned above:

- `<dataset_name>.csv`: The single CSV file containing the full data made of both training data, and test data representing the forecast horizon. This file is used to generate the train/test splits for the forecasting models.
- `<dataset_name>_train.csv`: The training data file containing the data used to train the forecasting models. Dataset contains the id field, time field, target field. The file also contains any past covariates, future covariates, and/or static covariates, if present in the dataset.
- `<dataset_name>_test.csv`: This is the test data file containing the data from the forecast horizon. It is used as an input to the prediction task. The file contains the id field, time field, future covariates, and static covariates. Note that the target field and past covariates (if any) are not included in this file.
- `<dataset_name>_test_key.csv`: This is the test data file containing the data from the forecast horizon. Dataset contains the id field, time field, and the target field. It is used in evaluating forecast accuracy.
- `<dataset_name>_schema_.json`: This is the schema file containing the metadata for the dataset. It is used to define the dataset schema on the Ready Tensor platform. The schema files are used by the forecasting models to parse and use the datasets for training and inference.

The project is conducted on the Ready Tensor platform. Reference the following page for the specifications for forecasting datasets on Ready Tensor: [Forecasting Specifications](https://docs.readytensor.ai/model-categories/forecasting/contributing-models).

## Repository Structure

The repository contains the following directories:

- **config**: Contains two configuration files required for running the scripts.
  - `forecasting_datasets.csv`: contains the name, description and attributes of the 120 datasets used in the project. This list includes the 20 original datasets and the 5 variations per dataset.
  - `forecasting_datasets_fields.csv`: contains information on all the fields in each of the datasets. Fields include the id, time field, target field, past covariates, future covariates, and static covariates.
- **datasets**: Contains all datasets files. It is further divided into:
  - **raw**: Contains the raw data files from the original source of the datasets and the Jupyter notebooks to preprocess each dataset into the main data file in the CSV format. These processed files are stored in the `processed` folder under the directories for each dataset.
  - **processed**: This folder contains the base datasets corresponding to the `ratio_max` scenario that are used for forecasting experiments. There are sub-directories for each dataset.
  - **variations**: This folder hosts variations of the original datasets found in the `processed` directory. These variations correspond to the `ratio_2`, `ratio_4`, `ratio_6`, `ratio_8`, and `ratio_10` scenarios.
- **src**: Contains the scripts to preprocess the datasets and create the variations. The script `run_all.py` is used to run all the scripts in the `src` directory.

## Dataset Variations

The datasets within the variations folder follow a specific naming convention to reflect the modifications made to the original datasets. The naming format is:

```
original_dataset_name_ratio_{variation}
```

Where:

- original_dataset_name: Refers to the name of the base dataset from the processed folder that this variation is derived from.
- variation: A numerical label (2, 4, 6, 8, 10) that indicates the ratio used in the dataset preparation. The variation number designates the ratio of the total number of observations in the training history to the forecast length.

### Example

For instance, consider the dataset named `airline_passengers_ratio_max` in the processed folder. The corresponding 4x ratio variation in the `datasets/variations` folder is named `airline_passengers_ratio_4`. This indicates that the dataset `airline_passengers_ratio_max` has been modified such that the total number of observations in training history is four times the length of the forecast period. In this case, the total number of observations in the dataset, including training and test splits, is 5x the forecast length.

## Usage

1. Create virtual environment and install dependencies in `requirements.txt`.
2. Run the script `run_all.py` to all necessary files in the `datasets/processed` and `datasets/variations` directories.

---

## Datasets Information

| Dataset                                             |      Dataset Industry       | Time Granularity | Series Length | # of Series | # Past Covariates | # Future Covariates | # Static Covariates |
| --------------------------------------------------- | :-------------------------: | :--------------: | :-----------: | :---------: | :---------------: | :-----------------: | :-----------------: |
| Air Quality KDD 2018                                |    Environmental Science    |      hourly      |    10,898     |     34      |         5         |          0          |          0          |
| Airline Passengers                                  |  Transportation / Aviation  |     monthly      |      144      |      1      |         0         |          0          |          0          |
| Atmospheric CO2 Concentrations                      |    Environmental Science    |     monthly      |      789      |      1      |         0         |          0          |          0          |
| Australian Beer Production                          |  Food & Beverage / Brewing  |    quarterly     |      218      |      1      |         0         |          0          |          0          |
| Avocado Sales                                       |    Agriculture and Food     |      weekly      |      169      |     106     |         7         |          0          |          1          |
| Bank Branch Transactions                            |     Finance / Synthetic     |      weekly      |      169      |     32      |         5         |          1          |          2          |
| Climate Related Disasters Frequency                 |       Climate Science       |      yearly      |      43       |     50      |         6         |          0          |          0          |
| Daily Stock Prices                                  |           Finance           |      daily       |     1,000     |     52      |         5         |          0          |          0          |
| GDP per Capita Change                               |    Economics and Finance    |      yearly      |      58       |     89      |         0         |          0          |          0          |
| M4 Forecasting Competition Sampled Daily Series     |        Miscellaneous        |      daily       |     1,280     |     60      |         0         |          0          |          0          |
| M4 Forecasting Competition Sampled Hourly Series    |        Miscellaneous        |      hourly      |      748      |     35      |         0         |          0          |          0          |
| M4 Forecasting Competition Sampled Monthly Series   |        Miscellaneous        |     monthly      |      324      |     80      |         0         |          0          |          0          |
| M4 Forecasting Competition Sampled Quarterly Series |        Miscellaneous        |    quarterly     |      78       |     75      |         0         |          0          |          0          |
| M4 Forecasting Competition Sampled Yearly Series    |        Miscellaneous        |      yearly      |      46       |     100     |         0         |          0          |          0          |
| Online Retail Sales                                 |     E-commerce / Retail     |      daily       |      363      |     38      |         1         |          0          |          0          |
| PJM Hourly Energy Consumption                       |           Energy            |      hourly      |    10,223     |     10      |         0         |          0          |          0          |
| Seattle Burke Gilman Trail                          |       Urban Planning        |      hourly      |     5,088     |      4      |         0         |          0          |          4          |
| Sunspots                                            |  Astronomy / Astrophysics   |    quarterly     |      760      |      1      |         0         |          0          |          0          |
| Weekly Weather in 26 World Cities                   |         Meteorology         |      weekly      |      156      |     25      |        16         |          0          |          2          |
| Theme Park Attendance                               | Entertainment / Theme Parks |      daily       |     1,142     |      1      |         0         |         56          |          0          |

More information about each dataset is provided in the sections below.

---

## Air Quality KDD 2018

#### Alias (on scoreboards): air_quality_kdd_2018

#### Domain / Industry: Environmental Science

#### Description

Air Quality KDD 2018 is a time series dataset from the KDD Cup 2018 competition, featuring 270 hourly series of air quality data from 59 stations in Beijing and London (01/01/2017 to 31/03/2018). It includes various air quality measurements and handles missing values through zero replacement and carrying forward last observations (LOCF). Useful for benchmarking time series forecasting algorithms in air quality prediction. Original dataset contained air quality data for stations from Beijing and London. In this curated dataset, only the air quality data for stations from Beijing is included.

#### Dataset characteristics

- Number of series = 34
- Series length = 10,890
- Time granularity = Hourly
- Number of past covariates = 5
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). KDD Cup Dataset (without Missing Values) (Version 4) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4656756

Dataset can be found here:
https://zenodo.org/records/4656756

---

## Airline Passengers

#### Alias (on scoreboards): airline_passengers

#### Domain / Industry: Transportation / Aviation

#### Description

This is the classic Box & Jenkins airline data which contains monthly totals of international airline passengers (1949--1960). It is a commonly used dataset in time series analysis and forecasting, making it valuable for studying seasonal patterns and applying forecasting techniques like ARIMA and exponential smoothing in the field of time series analysis.

#### Dataset characteristics

- Number of series = 1
- Series length = 144
- Time granularity = Yearly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Original source:
Box, G.E.P., Jenkins, G.M., Reinsel, G.C., & Ljung, G.M. (2015). Time Series Analysis: Forecasting and Control. John Wiley & Sons.

Dataset Source:

[https://www.kaggle.com/datasets/rakannimer/air-passengers](https://www.kaggle.com/datasets/rakannimer/air-passengers)

---

## Atmospheric CO2 Concentrations

#### Alias (on scoreboards): atmospheric_co2_concentrations

#### Domain / Industry: Environmental Science

#### Description

The Atmospheric CO2 Concentrations dataset comprises measurements of the concentration of carbon dioxide in the atmosphere, expressed in parts per million (ppm). The data spans from March 1958 onwards, providing a long-term record of one of the greenhouse gases affecting Earth's climate. The dataset's monthly resolution allows for observing seasonal variations and long-term trends in CO2 concentrations. Sourced from the National Oceanic and Atmospheric Association (NOAA) Global Monitoring Laboratory, this dataset is a valuable resource in climate change research and environmental studies.

#### Dataset characteristics

- Number of series = 1
- Series length = 789
- Time granularity = Monthly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This dataset is sourced from the IMF's Climate Change Indicators Dashboard. The Climate Change Indicators Dashboard is an international statistical initiative to address the growing need for climate-related data used in macroeconomic and financial stability analysis. See here for more information:  
https://climatedata.imf.org/pages/climatechange-data

---

## Australian Beer Production

#### Alias (on scoreboards): australia_beer_production

#### Domain / Industry: Food & Beverage / Brewing

#### Description

The "Australian Beer Production Dataset" provides a detailed record of beer production in Australia from 1956 to the second quarter of 2010. This dataset, presenting quarterly measurements, captures the volume of beer produced in megaliters each quarter, thus offering a rich, univariate time series for analysis. Its extensive historical span is ideal for examining seasonal patterns, long-term trends, and cyclical behaviors in the context of beer production. The dataset's value extends to economists, market analysts, and professionals in the brewing industry, offering them insights to forecast future production and comprehend historical industry trends. Furthermore, its pronounced seasonality and extensive timeline render it a quintessential resource for educational purposes and practical applications in time series forecasting methodologies, such as ARIMA and seasonal decomposition techniques.

#### Dataset characteristics

- Number of series = 1
- Series length = 218
- Time granularity = quarterly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This dataset is sourced from the repository for [Darts](https://unit8.com/resources/darts-time-series-made-easy-in-python/) python package for time series forecasting. See here for more information:  
https://github.com/unit8co/darts

---

## Avocado Sales

#### Alias (on scoreboards): avocado_sales

#### Domain / Industry: Agriculture and Food Industry

#### Description

This dataset is sourced from the Hass Avocado Board. It contains data from weekly retail scans over 169 weeks beginning in January 2015, detailing national sales volume (units) and prices of Hass avocados. The information is sourced directly from the sales records of retailers, reflecting actual sales. It covers various retail outlets including grocery stores, mass merchandisers, club and drug stores, dollar stores, and military commissaries. The average price listed represents the cost per individual avocado, even if sold in multi-unit bags. The dataset only includes Product Lookup codes (PLUs) for Hass avocados, excluding other avocado types like greenskins. This dataset is useful for timeseries forecasting and trend analysis in the context of the agricultural industry.

#### Dataset characteristics

- Number of series = 106
- Series length = 169
- Time granularity = Weekly
- Number of past covariates = 7
- Number of future covariates = 0
- Number of static covariates = 1

#### Attribution

The dataset is sourced from the Hass Avocado Board.
Dataset can be downloaded from here: https://hassavocadoboard.com/
Filter for "Category Data" and download the weekly level "UNIT SALES, DOLLAR SALES AND ASP" report.

---

## Bank Branch Transactions

#### Alias (on scoreboards): bank_branch_transactions

#### Domain / Industry: Finance / Retail Banking / Synthetic

#### Description

The "Bank Branch Transactions" dataset is a synthetic dataset that emulates the transaction activities of a fictitious bank network consisting of 32 branches over a period of 169 weeks. It captures the weekly transaction data for 6 different transaction types at each branch while simulating correlations between transaction types and branches. The dataset also models the impact of bank holidays. It is versatile, suitable for multi-variate forecasting, or individual series forecasting, with the option to use other transaction series as exogenous factors for forecasting tasks.

#### Dataset characteristics

- Number of series = 32
- Series length = 169
- Time granularity = Weekly
- Number of past covariates = 5
- Number of future covariates = 1
- Number of static covariates = 2

#### Attribution

This is a synthetic dataset generated by Ready Tensor. It is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## Climate Related Disasters Frequency

#### Alias (on scoreboards): climate_related_disasters

#### Domain / Industry: Climate Science

#### Description

This dataset, sourced from the IMF's Climate Change Indicators Dashboard, captures the count of climate-related disasters in the 50 largest countries by land area from 1980 to 2022. It categorizes disasters into six types: Drought, Extreme temperature, Flood, Landslide, Storm, and Wildfire. This data reflects the increasing importance of understanding the impacts of climate change on natural disasters, a link extensively documented in climate change literature.

#### Dataset characteristics

- Number of series = 50
- Series length = 43
- Time granularity = Yearly
- Number of past covariates = 6
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This dataset is sourced from the IMF's Climate Change Indicators Dashboard. The Climate Change Indicators Dashboard is an international statistical initiative to address the growing need for climate-related data used in macroeconomic and financial stability analysis. See here for more information:  
https://climatedata.imf.org/pages/climatechange-data

---

## Daily Stock Prices

#### Alias (on scoreboards): daily_stock_prices

#### Domain / Industry: Finance

#### Description

This dataset provides historical stock data from 52 selected S&P 500 companies over three decades. It aims to capture individual stock trends and patterns while avoiding market-wide influences. The dataset spans 1000 trading days for each stock, with random start dates to ensure decorrelation. Stock tickers have been anonymized to focus on technical analysis. It's ideal for time series forecasting and technical analysis in a real-world stock market context.

#### Dataset characteristics

- Number of series = 52
- Series length = 1000
- Time granularity = Daily
- Number of past covariates = 5
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Extracted using `yfinance` python library. See more information on the usage here: https://pypi.org/project/yfinance/

Dataset was extracted by Ready Tensor and is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## GDP Per Capita Growth

#### Alias (on scoreboards): gdp_per_capita_growth

#### Domain / Industry: Economics and Finance Industry

#### Description

This dataset detailing GDP per Capita change from 1961 to 2019 for 89 countries provides a comprehensive look at economic growth and contraction over nearly six decades. Sourced from the World Bank, a reputable authority in global economic data, this dataset offers annual percentage changes in Gross Domestic Product (GDP) for a wide range of countries, reflecting the economic performance of each nation over time. The dataset's extended timeframe and broad coverage make it an invaluable tool for testing various time series forecasting models, offering insights into cyclical patterns, long-term trends, and potential future trajectories of economies.

#### Dataset characteristics

- Number of series = 89
- Series length = 58
- Time granularity = Yearly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Dataset is extracted from The World Bank. The data can be downloaded from here:  
https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG

Dataset is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## M4 Forecasting Competition Sampled Daily Series

#### Alias (on scoreboards): m4_daily_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset comprises 60 timeseries at daily frequency, each spanning 1280 days, randomly sampled from the M4 forecasting competition. These series provide a consistent length of historical window and are ideal for exploring trends and seasonalities of various kinds such as day-of-week, day-of-month, day-of-year, etc. The M4 dataset contains
series drawn from across various sectors.

#### Dataset characteristics

- Number of series = 60
- Series length = 1280
- Time granularity = Daily
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo.

Dataset can be found here:  
https://zenodo.org/records/4656548

DOI: 10.5281/zenodo.4656548

---

## M4 Forecasting Competition Sampled Hourly Series

#### Alias (on scoreboards): m4_hourly_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset is a curated collection of 35 unique hourly time series, each with a length of 748 data points, sampled from the diverse and comprehensive series presented in the M4 forecasting competition. Encompassing a range of domains including finance, retail, and energy, these uni-variate series are selected for their variety and the richness they offer to hourly frequency forecasting tasks, despite originating from non-uniform time windows.

#### Dataset characteristics

- Number of series = 35
- Series length = 748
- Time granularity = Hourly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4656589

Dataset can be found here:  
https://zenodo.org/records/4656589

DOI: 10.5281/zenodo.4656589

---

## M4 Forecasting Competition Sampled Monthly Series

#### Alias (on scoreboards): m4_monthly_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset comprises 80 timeseries at monthly frequency, each spanning 324 months, randomly sampled from the M4 forecasting competition. These series provide a consistent length of historical window and are ideal for exploring long-term trends and seasonalities. The M4 dataset contains series drawn from across various sectors.

#### Dataset characteristics

- Number of series = 80
- Series length = 324
- Time granularity = Monthly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo.

Dataset can be found here:  
https://zenodo.org/records/4656480

DOI: 10.5281/zenodo.4656480

---

## M4 Forecasting Competition Sampled Quarterly Series

#### Alias (on scoreboards): m4_quarterly_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset comprises 75 quarterly time series, each spanning March 1998 to June 2017, randomly sampled from the M4 forecasting competition. These series provide a consistent historical window and are ideal for exploring long-term trends and forecasting challenges on quarterly-frequency series drawn from across various sectors.

#### Dataset characteristics

- Number of series = 75
- Series length = 78
- Time granularity = Quarterly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo.

Dataset can be found here:  
https://zenodo.org/records/4656480

DOI: 10.5281/zenodo.4656480

---

## M4 Forecasting Competition Sampled Yearly Series

#### Alias (on scoreboards): m4_yearly_miscellaneous

#### Domain / Industry: Miscellaneous

#### Description

This dataset comprises 100 yearly time series, each spanning 46 years from 1970 to 2015, sampled from the M4 forecasting competition. These series provide a consistent historical window and are ideal for exploring long-term trends and forecasting challenges across various sectors.

#### Dataset characteristics

- Number of series = 100
- Series length = 46
- Time granularity = Yearly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Citation:  
Godahewa, R., Bergmeir, C., Webb, G., Hyndman, R., & Montero-Manso, P. (2020). M4 Hourly Dataset (Version 3) [Data set]. Zenodo. https://zenodo.org/records/4656379

Dataset can be found here:  
https://zenodo.org/records/4656379

DOI: 10.5281/zenodo.4656379

---

## Online Retail Sales

#### Alias (on scoreboards): online_retail_sales

#### Domain / Industry: E-commerce / Retail

#### Description

The "Online Retail Sales" dataset aggregates daily transactions from a UK-based online retailer, focusing on the top 40 items by sales over a two-year period from 2018 to 2019. It provides insights into daily order counts and total sales per item, offering a granular view of consumer purchasing patterns and item performance within the niche market of unique all-occasion gifts. This dataset is particularly useful for retail trend analysis, inventory forecasting, and understanding seasonal impacts on e-commerce.

#### Dataset characteristics

- Number of series = 38
- Series length = 374
- Time granularity = Daily
- Number of past covariates = 1
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Dataset is sourced from here:
https://archive.ics.uci.edu/dataset/352/online+retail

DOI:  
10.24432/C5BW33

---

## PJM Hourly Energy Consumption

#### Alias (on scoreboards): pjm_energy_consumption

#### Domain / Industry: Energy

#### Description

This dataset contains data related to hourly level energy consumption in regions served by PJM Interconnection LLC (PJM). PJM Interconnection is a regional transmission organization (RTO) that coordinates the movement of wholesale electricity in all or parts of Delaware, Illinois, Indiana, Kentucky, Maryland, Michigan, New Jersey, North Carolina, Ohio, Pennsylvania, Tennessee, Virginia, West Virginia and the District of Columbia.

The hourly power consumption data comes from PJM's website and are in megawatts (GW). This particular dataset is filtered to represent the time span from May 1st, 2017 through June 30th, 2018. There are 10 regions represented in the data. This dataset is valuable for timeseries analysis at the hourly level. It contains seasonalities of different frequencies such as hour-of-day, day-of-week, and day-of-year.

#### Dataset characteristics

- Number of series = 10
- Series length = 10,223
- Time granularity = Daily
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

Dataset is sourced from here:
https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption?select=est_hourly.paruqet

---

## Seattle Burke Gilman Trail Dataset

#### Alias (on scoreboards): seattle_burke_gilman_trail

#### Domain / Industry: Urban Planning

#### Description

This dataset contains hourly level pedestrian and bicycle counts at the Burke Gilman Trail in Seattle. There are a total of 4 series in the dataset: 2 bicycle count series (north-bound and south-bound) and 2 pedestrian count series. The data is filtered to cover the date range from 1/1/2017 to 7/31/2017. This dataset is useful for timeseries analysis involving short-term seasonalities, especially intra-day (hour-of-the-day) and intra-week (day-of-the-week) seasonalities.

The dataset contains some extreme outliers, presumably due to one-off special events at the trail locations.

#### Dataset characteristics

- Number of series = 4
- Series length = 5,088
- Time granularity = hourly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 4

#### Attribution

This dataset is sourced from the City of Seattle Open Data Portal. See here for more information: https://data.seattle.gov/.

The specific dataset can be extracted here:  
https://data.seattle.gov/Transportation/Burke-Gilman-Trail-north-of-NE-70th-St-Bicycle-and/2z5v-ecg8/about_data

---

## Sunspots

#### Alias (on scoreboards): sunspots

#### Domain / Industry: Astronomy / Astrophysics

#### Description

The Sunspots dataset consists of observations of the number of sunspots on the Sun, recorded each month. It spans the time period from January 1749 to December 1983, providing a long-term view of solar activity. The original monthly frequency dataset is aggregated to quarterly frequency in this project.

Sunspots are temporary phenomena on the Sun's photosphere that appear as spots darker than the surrounding areas. They are regions of reduced surface temperature caused by concentrations of magnetic field flux that inhibit convection. Sunspots usually appear in pairs of opposite magnetic polarity. Their number varies according to the approximately 11-year solar cycle.

This dataset is invaluable for time series analysis and forecasting due to its longevity, regularity, and the clear cyclical patterns it presents, which are reflective of the approximately 11-year solar cycle. Researchers and analysts commonly use this dataset to practice and test forecasting models, including ARIMA, exponential smoothing, and more modern machine learning approaches. The dataset's extensive history makes it particularly suitable for studying long-term trends and cyclic behavior in solar activity, offering insights into past solar cycles and helping predict future solar phenomena.

#### Dataset characteristics

- Number of series = 1
- Series length = 760
- Time granularity = Quarterly
- Number of past covariates = 0
- Number of future covariates = 0
- Number of static covariates = 0

#### Attribution

This dataset is sourced from here:  
https://www.kaggle.com/datasets/robervalt/sunspots

## Theme Park attendance

#### Alias (on scoreboards): theme_park_attendance

#### Domain / Industry: Entertainment / Theme Parks

#### Description

This synthetic dataset represents daily attendance at a fictitious theme park in Los Angeles from 2016 to 2019. It is ideal for time series forecasting, showcasing the impact of annual and weekly seasonality, exogenous variables such as holidays and weather, and random fluctuations.

#### Dataset characteristics

- Number of series = 1
- Series length = 1,142
- Time granularity = Daily
- Number of past covariates = 0
- Number of future covariates = 56
- Number of static covariates = 0

#### Attribution

This is a synthetic dataset generated by Ready Tensor. It is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

---

## Weekly Weather in 26 World Cities

#### Alias (on scoreboards): daily_weather

#### Domain / Industry: Meteorology

#### Description

The "Weekly Weather Dataset" spans 3 years and includes weekly weather measurements for 26 cities worldwide. It comprises 17 weather parameters, making it suitable for both multi-variate and single-series forecasting tasks. With data from January 2020 to December 2022, it's an ideal resource for forecasting the 'maxtemp' series while leveraging other weather measurements as potential exogenous factors.

#### Dataset characteristics

- Number of series = 26
- Series length = 156
- Time granularity = Weekly
- Number of past covariates = 16
- Number of future covariates = 0
- Number of static covariates = 2

#### Attribution

Extracted using API provided by `https://www.weatherapi.com/`. See more information here: https://www.weatherapi.com/docs/.

Dataset was extracted by Ready Tensor and is available under the Creative Commons Attribution 4.0 International license (CC-BY 4.0).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

TBD.
