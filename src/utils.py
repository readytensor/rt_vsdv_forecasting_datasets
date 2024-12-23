import pandas as pd
import numpy as np
import json
import os
from typing import Dict, Any, Type
from pathlib import Path


def strip_quotes(val: str) -> str:
    """
    Strips leading and trailing quotes from a string.
    Args:
    val (str): The string to strip quotes from.

    Returns:
    str: The stripped string.
    """
    if isinstance(val, str) and len(val) >= 2:
        if (val[0] == val[-1]) and val.startswith(("'", '"')):
            return val[1:-1]
    return val


def load_metadata(dataset_cfg_path: str) -> pd.DataFrame:
    """
    Loads the dataset metadata.

    Args:
    dataset_cfg_path (str): The path to the dataset configuration file.

    Returns:
    pd.DataFrame: The dataset metadata.
    """
    # Load the dataset metadata
    dataset_metadata = pd.read_csv(dataset_cfg_path)
    # Apply the function to each element in the DataFrame
    dataset_metadata = dataset_metadata.apply(strip_quotes)
    return dataset_metadata


def load_features_config(features_cfg_path: str) -> pd.DataFrame:
    """
    Loads the data features configuration.

    Args:
    features_cfg_path (str): The path to the features configuration file.

    Returns:
    pd.DataFrame: The data features configuration.
    """
    # Load the data features configuration
    data_features_config = pd.read_csv(features_cfg_path, encoding="latin-1")
    return data_features_config


def load_dataset(
    dataset_name: str,
    processed_datasets_path: str,
    train: bool = False,
    test: bool = False,
) -> pd.DataFrame:
    """
    Read dataset

    Args:
    dataset_name (str): Name of the dataset.
    processed_datasets_path (str): Path where processed data files are to be saved per dataset.
    train (bool): If True, load training data.
    test (bool): If True, load testing data.

    Returns:
    pd.DataFrame: The data features configuration.
    """
    assert not (train and test), "Train and test cannot be True at the same time."
    suffix = "_train" if train else "_test" if test else ""
    dataset_path = os.path.join(
        processed_datasets_path, dataset_name, f"{dataset_name}{suffix}.csv"
    )
    dataset = pd.read_csv(dataset_path)

    return dataset


def load_schema(dataset_name: str, processed_datasets_path: str) -> Dict[str, Any]:
    """
    Load and return schema for given dataset.

    Args:
    dataset_name (str): Name of the dataset.
    processed_datasets_path (str): Path where processed data files are to be saved per dataset.

    Returns:
    Dict: The data features configuration.
    """
    schema_path = os.path.join(
        processed_datasets_path, dataset_name, f"{dataset_name}_schema.json"
    )
    with open(schema_path, "r", encoding="utf-8") as file_:
        schema = json.load(file_)
    return schema


class JSONEncoder(json.JSONEncoder):
    """
    Custom JSONEncoder class to handle Numpy data types.
    """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.bool_):
            return bool(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(JSONEncoder, self).default(obj)


def convert_numpy_types(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert numpy data types to native Python data types.

    Args:
        data (dict): The dictionary to convert.

    Returns:
        dict: The converted dictionary.
    """

    for key, value in data.items():
        if isinstance(value, (np.integer, np.int64)):
            data[key] = int(value)
        elif isinstance(value, (np.floating, np.float64)):
            data[key] = float(value)
        elif isinstance(value, np.bool_):
            data[key] = bool(value)
        elif value is pd.NaT or pd.isnull(value):
            data[key] = None
        elif isinstance(value, pd.Timestamp):
            data[key] = str(value)

    return data


def get_processed_datasets(processed_dir_path: str) -> Dict[str, str]:
    """
    Get the dictionary of processed datasets names along with their paths.

    Returns: Dict[str, str]
    """
    dataset_names = [
        i
        for i in os.listdir(processed_dir_path)
        if os.path.isdir(os.path.join(processed_dir_path, i))
    ]
    dataset_dir_paths = [os.path.join(processed_dir_path, i) for i in dataset_names]
    dataset_file_paths = [
        os.path.join(i, f"{Path(i).name}.csv") for i in dataset_dir_paths
    ]
    dataset_schema_paths = [
        os.path.join(i, f"{Path(i).name}_schema.json") for i in dataset_dir_paths
    ]
    data_schema_pair = list(zip(dataset_file_paths, dataset_schema_paths))
    return dict(zip(dataset_names, data_schema_pair))


def read_data_schema(data_schema_path: str) -> Dict[str, Any]:
    """Read the data schema from the given path."""
    with open(data_schema_path, "r", encoding="utf-8") as file_:
        schema = json.load(file_)
    return schema
