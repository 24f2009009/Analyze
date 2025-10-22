import json
import pandas as pd


def main():
    # Create a tiny deterministic dataframe (requires pandas)
    df = pd.DataFrame({"col1":[1, 2, 3], "col2":["a", "b", "c"]})
    summary = {"row_count": int(df.shape[0]), "columns": int(df.shape[1])}
    result = {
        "summary": summary,
        "data_preview": df.head().to_dict(orient="records")
    }
    with open("result.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    main()
