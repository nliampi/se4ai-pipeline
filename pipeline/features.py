"""Stage 3: features -- turn cleaned sales into the model's inputs.

Training and prediction must both call this one function, so the model
always sees features encoded the same way (no training-serving skew).
"""
import pandas as pd


def encode(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Return (X, y): feature matrix and target price.

    X columns: sqft, bedrooms, age, and one 0/1 column per region.
    """
    # TODO (Task 1): move the "3. features" block from train_all.py here.
    # Leave the dead USE_LOG_PRICE experiment behind -- nobody uses it.
    # ---- 3. features --------------------------------------------------------
    if "year_built" not in df.columns:
        raise ValueError("encode: missing year_built column")
    df["age"] = df["sold_date"].dt.year - df["year_built"]

    required_columns = {"sqft", "bedrooms", "age", "region"}
    if not required_columns.issubset(df.columns):
        raise ValueError("encode: missing one of sqft, bedrooms, age, region columns")
    X = pd.get_dummies(df[["sqft", "bedrooms", "age", "region"]], columns=["region"], dtype=int)
    
    if "price" not in df.columns:
        raise ValueError("encode: missing price column")
    y = df["price"]
    return X, y

    raise NotImplementedError("features.encode: move the code from train_all.py")
