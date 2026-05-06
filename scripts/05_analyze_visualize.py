import os
import pandas as pd
import matplotlib.pyplot as plt

INPUT_PATH = "data/processed/integrated_flights_weather.csv"

TABLE_DIR = "results/tables"
FIGURE_DIR = "results/figures"

os.makedirs(TABLE_DIR, exist_ok=True)
os.makedirs(FIGURE_DIR, exist_ok=True)


def main():
    print("Loading integrated dataset...")

    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(
            "Integrated dataset not found. Run 04_integrate_data.py first."
        )

    df = pd.read_csv(INPUT_PATH, low_memory=False)

    print(f"Integrated rows loaded: {len(df)}")

    # Ensure numeric columns are numeric
    numeric_cols = [
        "departure_delay",
        "arrival_delay",
        "reported_weather_delay",
        "temperature_c",
        "visibility_m",
        "wind_speed_mps",
        "precipitation_mm"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Summary by precipitation day
    precip_summary = (
        df.groupby("precipitation_day")
        .agg(
            flight_count=("departure_delay", "count"),
            avg_departure_delay=("departure_delay", "mean"),
            median_departure_delay=("departure_delay", "median"),
            delayed_flight_rate=("is_departure_delayed", "mean"),
            avg_reported_weather_delay=("reported_weather_delay", "mean")
        )
        .reset_index()
    )

    precip_summary["delayed_flight_rate"] = precip_summary["delayed_flight_rate"] * 100
    precip_summary.to_csv(
        os.path.join(TABLE_DIR, "precipitation_delay_summary.csv"),
        index=False
    )

    # Summary by low visibility day
    visibility_summary = (
        df.groupby("low_visibility_day")
        .agg(
            flight_count=("departure_delay", "count"),
            avg_departure_delay=("departure_delay", "mean"),
            median_departure_delay=("departure_delay", "median"),
            delayed_flight_rate=("is_departure_delayed", "mean"),
            avg_reported_weather_delay=("reported_weather_delay", "mean")
        )
        .reset_index()
    )

    visibility_summary["delayed_flight_rate"] = visibility_summary["delayed_flight_rate"] * 100
    visibility_summary.to_csv(
        os.path.join(TABLE_DIR, "visibility_delay_summary.csv"),
        index=False
    )

    # Summary by high wind day
    wind_summary = (
        df.groupby("high_wind_day")
        .agg(
            flight_count=("departure_delay", "count"),
            avg_departure_delay=("departure_delay", "mean"),
            median_departure_delay=("departure_delay", "median"),
            delayed_flight_rate=("is_departure_delayed", "mean"),
            avg_reported_weather_delay=("reported_weather_delay", "mean")
        )
        .reset_index()
    )

    wind_summary["delayed_flight_rate"] = wind_summary["delayed_flight_rate"] * 100
    wind_summary.to_csv(
        os.path.join(TABLE_DIR, "wind_delay_summary.csv"),
        index=False
    )

    # Monthly delay summary
    monthly_summary = (
        df.groupby("month")
        .agg(
            flight_count=("departure_delay", "count"),
            avg_departure_delay=("departure_delay", "mean"),
            delayed_flight_rate=("is_departure_delayed", "mean"),
            avg_precipitation=("precipitation_mm", "mean"),
            avg_visibility=("visibility_m", "mean"),
            avg_wind_speed=("wind_speed_mps", "mean")
        )
        .reset_index()
    )

    monthly_summary["delayed_flight_rate"] = monthly_summary["delayed_flight_rate"] * 100
    monthly_summary.to_csv(
        os.path.join(TABLE_DIR, "monthly_delay_summary.csv"),
        index=False
    )

    # Correlation table
    correlation_cols = [
        "departure_delay",
        "reported_weather_delay",
        "temperature_c",
        "visibility_m",
        "wind_speed_mps",
        "precipitation_mm"
    ]

    available_corr_cols = [col for col in correlation_cols if col in df.columns]
    corr = df[available_corr_cols].corr()
    corr.to_csv(os.path.join(TABLE_DIR, "correlation_table.csv"))

    # Figure 1: Average departure delay by precipitation day
    plt.figure()
    precip_summary.plot(
        x="precipitation_day",
        y="avg_departure_delay",
        kind="bar",
        legend=False
    )
    plt.xlabel("Precipitation Day")
    plt.ylabel("Average Departure Delay (minutes)")
    plt.title("Average Departure Delay by Precipitation Day")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURE_DIR, "avg_delay_by_precipitation.png"))
    plt.close()

    # Figure 2: Monthly average departure delay
    plt.figure()
    plt.plot(monthly_summary["month"], monthly_summary["avg_departure_delay"], marker="o")
    plt.xlabel("Month")
    plt.ylabel("Average Departure Delay (minutes)")
    plt.title("Monthly Average Departure Delay")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURE_DIR, "monthly_avg_departure_delay.png"))
    plt.close()

    # Figure 3: Wind speed vs departure delay
    plt.figure()
    plt.scatter(df["wind_speed_mps"], df["departure_delay"], alpha=0.3)
    plt.xlabel("Wind Speed (m/s)")
    plt.ylabel("Departure Delay (minutes)")
    plt.title("Wind Speed vs Departure Delay")
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURE_DIR, "wind_speed_vs_departure_delay.png"))
    plt.close()

    print("Analysis complete.")
    print(f"Tables saved to: {TABLE_DIR}")
    print(f"Figures saved to: {FIGURE_DIR}")


if __name__ == "__main__":
    main()