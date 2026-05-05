import os
import pandas as pd

# File paths
FLIGHTS_PATH = "data/raw/flights_2019.csv"
WEATHER_PATH = "data/raw/weather_2019.csv"
OUTPUT_DIR = "results/tables"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def profile_dataset(file_path, dataset_name):
    """
    Creates a basic data profile for a dataset:
    - number of rows
    - number of columns
    - column names
    - missing values
    - duplicate rows
    """

    print(f"\nProfiling {dataset_name}...")

    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        return None

    df = pd.read_csv(file_path, low_memory=False)

    profile = {
        "dataset": dataset_name,
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": df.duplicated().sum()
    }

    missing_values = df.isna().sum().reset_index()
    missing_values.columns = ["column", "missing_count"]
    missing_values["dataset"] = dataset_name
    missing_values["missing_percent"] = (missing_values["missing_count"] / len(df)) * 100

    print(f"{dataset_name} rows: {profile['rows']}")
    print(f"{dataset_name} columns: {profile['columns']}")
    print(f"{dataset_name} duplicate rows: {profile['duplicate_rows']}")

    return profile, missing_values, df.columns.tolist()


def main():
    all_profiles = []
    all_missing = []
    column_records = []

    datasets = [
        (FLIGHTS_PATH, "BTS Flight Data"),
        (WEATHER_PATH, "NOAA Weather Data")
    ]

    for file_path, dataset_name in datasets:
        result = profile_dataset(file_path, dataset_name)

        if result is not None:
            profile, missing_values, columns = result

            all_profiles.append(profile)
            all_missing.append(missing_values)

            for col in columns:
                column_records.append({
                    "dataset": dataset_name,
                    "column": col
                })

    if all_profiles:
        profiles_df = pd.DataFrame(all_profiles)
        profiles_df.to_csv(f"{OUTPUT_DIR}/data_profile_summary.csv", index=False)

    if all_missing:
        missing_df = pd.concat(all_missing, ignore_index=True)
        missing_df.to_csv(f"{OUTPUT_DIR}/missing_values_summary.csv", index=False)

    if column_records:
        columns_df = pd.DataFrame(column_records)
        columns_df.to_csv(f"{OUTPUT_DIR}/dataset_columns.csv", index=False)

    print("\nData profiling complete.")
    print(f"Outputs saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
