import os
import paths
from utils import load_dataset, load_schema

series_lengths = {
    "air_quality_kdd_2018_ratio_max": 10898,
    "pjm_energy_consumption_ratio_max": 10223,
    "seattle_burke_gilman_trail_ratio_max": 5088,
    "m4_hourly_miscellaneous_ratio_max": 1000,
    "m4_daily_miscellaneous_ratio_max": 1280,
    "theme_park_attendance_ratio_max": 1142,
    "daily_stock_prices_ratio_max": 1000,
    "online_retail_sales_ratio_max": 363,
    "avocado_sales_ratio_max": 169,
    "bank_branch_transactions_ratio_max": 169,
    "weekly_weather_ratio_max": 156,
    "atmospheric_co2_concentrations_ratio_max": 789,
    "m4_monthly_miscellaneous_ratio_max": 324,
    "airline_passengers_ratio_max": 144,
    "australian_beer_production_ratio_max": 218,
    "m4_quarterly_miscellaneous_ratio_max": 100,
    "sunspots_quarterly_ratio_max": 760,
    "gdp_per_capita_growth_ratio_max": 58,
    "climate_related_disasters_ratio_max": 43,
    "m4_yearly_miscellaneous_ratio_max": 46,
}

series_forecast_lengths = {
    "air_quality_kdd_2018_ratio_max": 72,
    "pjm_energy_consumption_ratio_max": 72,
    "seattle_burke_gilman_trail_ratio_max": 72,
    "m4_hourly_miscellaneous_ratio_max": 72,
    "m4_daily_miscellaneous_ratio_max": 28,
    "theme_park_attendance_ratio_max": 28,
    "daily_stock_prices_ratio_max": 28,
    "online_retail_sales_ratio_max": 28,
    "avocado_sales_ratio_max": 13,
    "bank_branch_transactions_ratio_max": 13,
    "weekly_weather_ratio_max": 13,
    "atmospheric_co2_concentrations_ratio_max": 12,
    "m4_monthly_miscellaneous_ratio_max": 12,
    "airline_passengers_ratio_max": 12,
    "australian_beer_production_ratio_max": 8,
    "m4_quarterly_miscellaneous_ratio_max": 8,
    "sunspots_quarterly_ratio_max": 8,
    "gdp_per_capita_growth_ratio_max": 3,
    "climate_related_disasters_ratio_max": 3,
    "m4_yearly_miscellaneous_ratio_max": 3,
}

dataset_names = [
    i
    for i in os.listdir(paths.processed_datasets_path)
    if os.path.isdir(os.path.join(paths.processed_datasets_path, i))
]

ratios = [2, 4, 6, 8, 10]


def validate_datasets_length():
    # Max scenario
    for name in dataset_names:
        correct_length = series_lengths[name]
        dataset = load_dataset(name, paths.processed_datasets_path)
        schema = load_schema(name, paths.processed_datasets_path)

        grouped = dataset.groupby(schema["idField"]["name"])
        for group in grouped:
            assert (
                len(group[1]) == correct_length
            ), f"Full Dataset {name} has group with length {len(group[1])} but should have length {correct_length}"
    print("Full datasets for max scenario validated successfully.")

    # Ratio scenario
    for name in dataset_names:
        for ratio in ratios:
            variation_name = name.replace("_max", f"_{ratio}")
            correct_length = series_forecast_lengths[name] * (ratio + 1)
            dataset = load_dataset(variation_name, paths.variations_datasets_path)
            schema = load_schema(variation_name, paths.variations_datasets_path)

            grouped = dataset.groupby(schema["idField"]["name"])
            for group in grouped:
                assert (
                    len(group[1]) == correct_length
                ), f"Full Dataset {name} has group with length {len(group[1])} but should have length {correct_length}"

    print("Full datasets for ratio scenarios validated successfully.")


def validate_forecast_length():
    # Max scenario
    for name in dataset_names:
        correct_length = series_forecast_lengths[name]
        dataset = load_dataset(name, paths.processed_datasets_path, test=True)
        schema = load_schema(name, paths.processed_datasets_path)

        grouped = dataset.groupby(schema["idField"]["name"])
        for group in grouped:
            assert (
                len(group[1]) == correct_length
            ), f"Testing Dataset {name} has group with forecast length {len(group[1])} but should have forecast length {correct_length}"
    print("Test datasets for max scenario validated successfully.")
    # Ratio scenario
    for name in dataset_names:
        for ratio in ratios:
            variation_name = name.replace("_max", f"_{ratio}")
            correct_length = series_forecast_lengths[name]
            dataset = load_dataset(
                variation_name, paths.variations_datasets_path, test=True
            )
            schema = load_schema(variation_name, paths.variations_datasets_path)

            grouped = dataset.groupby(schema["idField"]["name"])
            for group in grouped:
                assert (
                    len(group[1]) == correct_length
                ), f"Testing Dataset {name} has group with length {len(group[1])} but should have length {correct_length}"

    print("Test datasets for ratio scenario validated successfully.")


def validate_train_length():
    for name in dataset_names:
        correct_length = series_lengths[name] - series_forecast_lengths[name]
        dataset = load_dataset(name, paths.processed_datasets_path, train=True)
        schema = load_schema(name, paths.processed_datasets_path)

        grouped = dataset.groupby(schema["idField"]["name"])
        for group in grouped:
            assert (
                len(group[1]) == correct_length
            ), f"Training Dataset {name} has group with forecast length {len(group[1])} but should have forecast length {correct_length}"
    print("Train datasets for max scenario validated successfully.")
    for name in dataset_names:
        for ratio in ratios:
            variation_name = name.replace("_max", f"_{ratio}")
            correct_length = series_forecast_lengths[name] * ratio
            dataset = load_dataset(
                variation_name, paths.variations_datasets_path, train=True
            )
            schema = load_schema(variation_name, paths.variations_datasets_path)

            grouped = dataset.groupby(schema["idField"]["name"])
            for group in grouped:
                assert (
                    len(group[1]) == correct_length
                ), f"Training Dataset {name} has group with length {len(group[1])} but should have length {correct_length}"

    print("Train datasets for ratio scenario validated successfully.")


def validate_all():
    validate_datasets_length()
    validate_forecast_length()
    validate_train_length()
