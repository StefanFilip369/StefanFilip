"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, 
  deaths and recovery change over time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def confirmed_cases_pichart(summary):
    
    countries = []
    confirmed_cases = []
    
    for group in summary:
        countries.append(group)
        confirmed_cases.append(summary[group]['confirmed'])
    
    plt.figure(figsize=(7, 7), dpi=72)
    plt.pie(confirmed_cases)
    plt.legend(labels=countries)
    plt.savefig('confirmed_cases_pichart.png')
    plt.show() 
    
    
    
    
    
def deaths_barchart(summary):
    countries_by_deaths = sorted(summary.items(), key=lambda item: item[1]['deaths'], reverse=True)
    
    data = countries_by_deaths[:5]
    countries = []
    deaths = []
    
    for i in range(5):
        countries.append(data[i][0])
        deaths.append(data[i][1]['deaths'])
    
    fig = plt.figure(figsize = (10, 5))
    # creating the bar plot
    plt.bar(countries, deaths, color ='maroon', width = 0.4)
    
    plt.xlabel("Countries")
    plt.ylabel("Deaths")
    plt.title("Top 5 countries for deaths")
    plt.savefig('deaths_barchart.png')
    plt.show()






def display_animation(groups, country):
    country_data = groups[country]
    
    def animate(i):
        y1.append(int(country_data[i][5]))
        y2.append(int(country_data[i][6]))
        y3.append(int(country_data[i][7]))
    
        ax.clear()
        ax.plot(y1, 'r', label='Confirmed')
        ax.plot(y2, 'b', label='Deaths')
        ax.plot(y3, 'g', label='Recoveries')
        ax.legend()
    

    y1 = []
    y2 = []
    y3 = []
    
    fig, ax = plt.subplots()
    
    ani = FuncAnimation(fig, animate, frames=len(country_data), interval=500, repeat=False)
    plt.title(country)
    plt.show()











    
    