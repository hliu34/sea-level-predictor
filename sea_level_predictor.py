import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df, s=5)
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create first line of best fit
    fit1 = linregress(x, y)

    # constructing best fit line
    
    years_extended = np.arange(df.Year.min(), 2051, 1)
    y_pred = fit1.intercept + fit1.slope * years_extended
    plt.plot(years_extended, y_pred, color="red", label=f"Best fit line (1880-2050): y={fit1.slope:.2f}x{fit1.intercept:.2f}")
    

    # Create second line of best fit
    selected_years = df[df["Year"] >= 2000]
    x2 = selected_years["Year"]
    y2 = selected_years["CSIRO Adjusted Sea Level"]

    year_range = np.arange(selected_years.Year.min(), 2051, 1)
    fit2 = linregress(x2, y2)
    y_pred2 = fit2.intercept + fit2.slope * year_range
    plt.plot(year_range, y_pred2, color="orange", label=f'Best fit line (2000-2050): y={fit2.slope:.2f}x{fit2.intercept:.2f}')



    # Add labels and title   

    plt.legend()
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()