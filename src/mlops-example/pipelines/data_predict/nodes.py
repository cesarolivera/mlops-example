import pandas as pd

def predict_price_from_data(input_df: pd.DataFrame, regressor) -> float:
    result = regressor.predict(input_df)
    return result[0]