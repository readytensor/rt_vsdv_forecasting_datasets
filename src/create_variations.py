import os
import shutil
import pandas as pd
from tqdm import tqdm
import sys
import json
from copy import deepcopy

from utils import get_processed_datasets, read_data_schema, load_metadata, JSONEncoder
import paths as file_paths



def create_variation(
    data: pd.DataFrame, id_col: str, forecast_length: int, ratio: int
) -> pd.DataFrame:
    """
    Create a variation of the dataset by selecting the last N * ratio rows for each group.

    Args:
    - data (pd.DataFrame): The dataset.
    - id_col (str): The column to group by.
    - forecast_length (int): The forecast length.
    - ratio (int): The ratio to multiply the forecast length by.

    Returns (pd.DataFrame): The variation of the dataset.
    """
    length = (forecast_length * ratio) + forecast_length
    grouped = data.groupby(id_col)
    series = [i for _, i in grouped]

    concat = []
    for s in series:
        copy = s.copy().iloc[-length:]
        concat.append(copy)

    variation = pd.concat(concat)
    return variation


def get_title_and_desc_for_variation(
        load_metadata: pd.DataFrame, dataset: str, ratio: int) -> str:
    """
    Get the name and description for the variation.
    
    Args:
    - load_metadata (pd.DataFrame): The metadata.
    - dataset (str): The name of the dataset.
    - ratio (int): The ratio to multiply the forecast length by.

    Returns (str): The name and description for the variation.
    """
    variation_name = f"{dataset}_ratio_{ratio}"
    filtered = load_metadata[load_metadata["dataset_external_id"] == variation_name]
    if filtered.empty:
        raise Exception(f"Cannot find variation for {dataset}, ratio {ratio}")
    title = filtered['dataset_name'].values[0]
    dataset_desc = filtered['description'].values[0]
    return title, dataset_desc


def get_dataset_base_name(dataset: str) -> str:
    """
    Get the base name of the dataset.

    Args:
    - dataset (str): The name of the dataset.

    Returns (str): The base name of the dataset.
    """
    return dataset.removesuffix("_ratio_max")

def generate_variations():
    ratios = [2, 4, 6, 8, 10]
    datasets = get_processed_datasets(file_paths.processed_datasets_path)
    dataset_metadata = load_metadata(dataset_cfg_path=file_paths.dataset_cfg_path)
    for name, paths in tqdm(datasets.items(), desc="Creating variations"):
        data_path, schema_path = paths
        data = pd.read_csv(data_path)
        schema = read_data_schema(schema_path)
        forecast_length = schema["forecastLength"]
        id_col = schema["idField"]["name"]

        dataset_base_name = get_dataset_base_name(name)
        for ratio in ratios:
            variation = create_variation(
                data, id_col=id_col, forecast_length=forecast_length, ratio=ratio
            )
            variation_name = f"{name.removesuffix('_max')}_{ratio}"
            save_dir = os.path.join(file_paths.variations_datasets_path, variation_name)
            save_schema_path = os.path.join(save_dir, f"{variation_name}_schema.json")
            save_file_path = os.path.join(save_dir, f"{variation_name}.csv")
            os.makedirs(save_dir, exist_ok=True)
            variation.to_csv(save_file_path, index=False)

            title, description = get_title_and_desc_for_variation(
                dataset_metadata, dataset_base_name, ratio)
            variation_schema = deepcopy(schema)
            variation_schema["title"] = title
            variation_schema["description"] = description
            with open(save_schema_path, "w", encoding="utf-8") as file_:
                json.dump(variation_schema, file_, cls=JSONEncoder, indent=2)
