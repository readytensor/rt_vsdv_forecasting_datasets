import os
import shutil
import pandas as pd
from tqdm import tqdm

from utils import get_processed_datasets, read_data_schema

PROCESSED_DIR = "./datasets/processed"
VARATIONS_DIR = "./datasets/variations"


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
    length = forecast_length * ratio
    grouped = data.groupby(id_col)
    series = [i for _, i in grouped]

    concat = []
    for s in series:
        copy = s.copy().iloc[-length:]
        concat.append(copy)

    variation = pd.concat(concat)
    return variation


def generate_variations():
    ratios = [2, 4, 6, 8, 10]
    datasets = get_processed_datasets(PROCESSED_DIR)
    for name, paths in tqdm(datasets.items(), desc="Creating variations"):
        data_path, schema_path = paths
        data = pd.read_csv(data_path)
        schema = read_data_schema(schema_path)
        forecast_length = schema["forecastLength"]
        id_col = schema["idField"]["name"]

        for ratio in ratios:
            variation = create_variation(
                data, id_col=id_col, forecast_length=forecast_length, ratio=ratio
            )
            variation_name = f"{name}_ratio_{ratio}"
            save_dir = os.path.join(VARATIONS_DIR, variation_name)
            save_schema_path = os.path.join(save_dir, f"{variation_name}_schema.json")
            save_file_path = os.path.join(save_dir, f"{variation_name}.csv")
            os.makedirs(save_dir, exist_ok=True)
            variation.to_csv(save_file_path, index=False)
            shutil.copy(schema_path, save_schema_path)
