"""Stage 2: clean -- fix types and drop rows we cannot trust."""
import pandas as pd
from sklearn.impute import SimpleImputer


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the raw sales.

    Guarantees for the next stage:
      * sold_date is a datetime column
      * sqft has no missing values
      * rows with an obviously wrong price (<= 10,000) are removed
    """
    # TODO (Task 1): move the "2. clean" block from train_all.py here.

    # ---- 2. clean -----------------------------------------------------------
    if "sold_date" not in df.columns:
        raise ValueError("clean_sales: missing sold_date column")
    df["sold_date"] = pd.to_datetime(df["sold_date"], format="ISO8601", utc=True)
    df = df[df["price"] > 10_000]           # drop obvious data-entry errors (price typos)

    if "sqft" not in df.columns:
        raise ValueError("clean_sales: missing sqft column")
    num_imputer = SimpleImputer(strategy="median")
    df["sqft"] = num_imputer.fit_transform(df[["sqft"]])


    return df

    # TODO (Task 2): make it work for data/sales_2026_q1.csv as well
    #                (run `pytest` to see what is expected).
    raise NotImplementedError("clean.clean_sales: move the code from train_all.py")
