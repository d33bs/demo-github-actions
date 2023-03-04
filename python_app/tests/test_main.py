"""
Demonstrational tests for demo-github actions
"""

import pandas as pd
from python_app.main import df


def test_df():
    """
    Tests for the dataframe from main.py
    """

    assert isinstance(df, pd.DataFrame)
