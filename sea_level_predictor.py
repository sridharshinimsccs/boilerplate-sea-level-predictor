import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # **1. Read data from file**
    df = pd.read_csv("epa-sea-level.csv")

    # **2. Create scatter plot**
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data", color="blue")

    # **3. Create first line of best fit (1880 - 2050)**
    slope1, intercept1, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended1 = range(1880, 2051)
    plt.plot(years_extended1, [slope1 * year + intercept1 for year in years_extended1], 'r', label="Best Fit 1880-2050")

    # **4. Create second line of best fit (2000 - 2050)**
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_extended2 = range(2000, 2051)
    plt.plot(years_extended2, [slope2 * year + intercept2 for year in years_extended2], 'green', label="Best Fit 2000-2050")

    # **5. Add labels and title**
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # **6. Save plot and return data for testing (DO NOT MODIFY)**
    plt.savefig('sea_level_plot.png')
    return plt.gca()
