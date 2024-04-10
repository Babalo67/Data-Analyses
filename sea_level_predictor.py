import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y, label='Sea Level Data')

    

    # Create first line of best fit

    slope, intercept, rvalue, pvalue, stderr= linregress(x,y)

    plt.plot(x,slope*x+intercept)

    future_years_all = range(1880, 2051)
    future_sea_levels_all = intercept + slope * future_years_all
    plt.plot(future_years_all, future_sea_levels_all, 'g--', label='Predicted Sea Level Rise in 2050 (All Data)')

    # Create second line of best fit

    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    plt.plot(recent_data['Year'], slope_recent + slope_recent * recent_data['Year'], 'b', label='Line of Best Fit (2000 Onwards)')
    
    future_years_recent = range(2000, 2051)
    future_sea_levels_recent = intercept_recent + slope_recent * future_years_recent
    plt.plot(future_years_recent, future_sea_levels_recent, 'y--', label='Predicted Sea Level Rise in 2050 (2000 Onwards)')

    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    plt.grid
    plt.show

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()