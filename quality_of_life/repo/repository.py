from pathlib import Path

import pandas as pd

from quality_of_life.utils import get_root_dir


def read_dataset(path: str) -> pd.DataFrame:
    file_path = Path(get_root_dir().parent / path)
    return pd.read_csv(file_path)
