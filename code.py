#Importing all Libraries needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define functions for reading and transposing data
def read_data_excel(excel_url, sheet_name, new_cols, countries):
    """
    Reads data from an Excel file and performs necessary preprocessing.

    Parameters:
    - excel_url (str): URL of the Excel file.
    - sheet_name (str): Name of the sheet containing data.
    - new_cols (list): List of columns to select from the data.
    - countries (list): List of countries to include in the analysis.

    Returns:
    - data_read (DataFrame): Preprocessed data.
    - data_transpose (DataFrame): Transposed data.
    """
    data_read = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3)
    data_read = data_read[new_cols]
    data_read.set_index('Country Name', inplace=True)
    data_read = data_read.loc[countries]

    return data_read, data_read.T

# Parameters for reading and transposing data
sheet_name = 'Data'
new_cols = ['Country Name','1964', '1971', '1978', '1985', '1992', '1999', '2006', '2013', '2020', '2022']
countries = ['Brazil', 'Nigeria', 'France', 'Japan', 'Mexico', 'Indonesia', 'Argentina', 'Italy', 'Canada', 'Spain', 'Thailand', 'Greece', 'Sweden', 'Pakistan', 'Bangladesh']

# The Excel URL below indicates GDP growth (annual %) for selected countries
excel_url_gdp = 'https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=excel'
data_gdp_read, data_gdp_transpose = read_data_excel(excel_url_gdp, sheet_name, new_cols, countries)

# The Excel URL below indicates Agriculture, forestry, and fishing, value added (% of GDP)
excel_url_agriculture = 'https://api.worldbank.org/v2/en/indicator/NV.AGR.TOTL.ZS?downloadformat=excel'
data_agriculture_read, data_agriculture_transpose = read_data_excel(excel_url_agriculture, sheet_name, new_cols, countries)

# The Excel URL below indicates electricity production from oil, gas, and coal sources (% of total)
excel_url_electricity = 'https://api.worldbank.org/v2/en/indicator/EG.ELC.FOSL.ZS?downloadformat=excel'
data_electricity_read, data_electricity_transpose = read_data_excel(excel_url_electricity, sheet_name, new_cols, countries)

# The Excel URL below indicates CO2 emissions (metric tons per capita)
excel_url_CO2 = 'https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=excel'
data_CO2, data_CO2_transpose = read_data_excel(excel_url_CO2, sheet_name, new_cols, countries)

# The Excel URL below indicates Forest area (% of land area)
excel_url_forest_area = 'https://api.worldbank.org/v2/en/indicator/AG.LND.FRST.ZS?downloadformat=excel'
data_forest_area, data_forest_area_transpose = read_data_excel(excel_url_forest_area, sheet_name, new_cols, countries)

# The Excel URL below indicates Arable land (% of land area)
excel_url_arable_land = 'https://api.worldbank.org/v2/en/indicator/AG.LND.ARBL.ZS?downloadformat=excel'
data_arable_land, data_arable_land_transpose = read_data_excel(excel_url_arable_land, sheet_name, new_cols, countries)

# The Excel URL below indicates Urban population growth (annual %)
excel_url_urban = 'https://api.worldbank.org/v2/en/indicator/SP.URB.GROW?downloadformat=excel'
data_urban_read, data_urban_transpose = read_data_excel(excel_url_urban, sheet_name, new_cols, countries)
# Function for Multiple line plots
def multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors):
    """
    Plot multiple line plots.

    Parameters:
    - x_data (array-like): X-axis data.
    - y_data (list of array-like): Y-axis data for each line.
    - xlabel (str): X-axis label.
    - ylabel (str): Y-axis label.
    - title (str): Plot title.
    - labels (list): Labels for each line.
    - colors (list): Colors for each line.
    """
    plt.figure(figsize=(8, 6))
    plt.title(title, fontsize=10)

    for i in range(len(y_data)):
        plt.plot(x_data, y_data[i], label=labels[i], color=colors[i])

    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.legend(bbox_to_anchor=(1.02, 1))
    plt.show()

# The function below constructs a bar plot
def bar_plot(labels_array, width, y_data, y_label, label, title, rotation=0):
    """
    Plot a grouped bar plot.

    Parameters:
    - labels_array (array-like): X-axis labels.
    - width (float): Width of each bar group.
    - y_data (list of array-like): Y-axis data for each bar.
    - y_label (str): Y-axis label.
    - label (list): Labels for each bar group.
    - title (str): Plot title.
    - rotation (float): Rotation angle for X-axis labels.
    """
    x = np.arange(len(labels_array))
    fig, ax = plt.subplots(figsize=(8, 6), dpi=200)

    for i in range(len(y_data)):
        plt.bar(x + width * i, y_data[i], width, label=label[i])

    plt.title(title, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.xlabel(None)
    plt.xticks(x + width * (len(y_data) - 1) / 2, labels_array, rotation=rotation)

    plt.legend()
    ax.tick_params(bottom=False, left=True)

    plt.show()


def correlation_heatmap(data, corr, title):
    """
    Display a correlation heatmap.

    Parameters:
    - data (DataFrame): Input data.
    - corr (DataFrame): Correlation matrix.
    - title (str): Heatmap title.
    """
    plt.figure(figsize=(8, 6), dpi=200)
    plt.imshow(corr, cmap='bone', interpolation='none')
    plt.colorbar()

    plt.xticks(range(len(data.columns)), data.columns, rotation=90, fontsize=10)
    plt.yticks(range(len(data.columns)), data.columns, rotation=0, fontsize=10)

    plt.title(title, fontsize=10)

    labels = corr.values
    for i in range(labels.shape[0]):
        for j in range(labels.shape[1]):
            plt.text(j, i, '{:.2f}'.format(labels[i, j]),
                     ha="center", va="center", color="white")

    plt.show()

# Print the transposed GDP data for fifteen countries
print(data_gdp_transpose)

# Plot a multiple line plot for GDP growth (annual %) for selected countries
x_data_gdp = data_gdp_transpose.index
y_data_gdp = [data_gdp_transpose[country] for country in countries]
xlabel_gdp = 'Years'
ylabel_gdp = '(%) GDP Growth'
labels_gdp = countries
colors_gdp = ['orange', 'pink', 'cyan', 'purple', 'green', 'red', 'blue', 'yellow', 'brown', 'gray', 'teal', 'magenta', 'purple', 'orange', 'blue']
title_gdp = 'Annual (%) GDP Growth for Selected Countries'

# Plot the line plots for GDP of selected countries
multiple_plot(x_data_gdp, y_data_gdp, xlabel_gdp, ylabel_gdp, title_gdp, labels_gdp, colors_gdp)

# Plot a grouped bar plot for Agriculture, forestry, and fishing, value added (% of GDP) for fifteen countries
labels_array_agr = countries
width_agr = 0.2
y_data_agr = [
    data_agriculture_read['1964'],
    data_agriculture_read['1971'],
    data_agriculture_read['1978'],
    data_agriculture_read['1985']
]
y_label_agr = '% of GDP'
label_agr = ['Year 1964', 'Year 1971', 'Year 1978', 'Year 1985']
title_agr = 'Agriculture, forestry, and fishing, value added (% of GDP) for Random Countries'

# Plot the grouped bar plot for fifteen countries
bar_plot(labels_array_agr, width_agr, y_data_agr, y_label_agr, label_agr, title_agr, rotation=55)

# Dataframe for Australia using selected indicators
data_Argentina = {
    'Urban pop. growth': data_arable_land_transpose['Argentina'],
    'Electricity production': data_electricity_transpose['Argentina'],
    'Agric. forestry and Fisheries': data_agriculture_transpose['Argentina'],
    'CO2 Emissions': data_CO2_transpose['Argentina'],
    'Forest Area': data_forest_area_transpose['Argentina'],
    'GDP Annual Growth': data_gdp_transpose['Argentina']
}
df_Argentina = pd.DataFrame(data_Argentina)

# Display the dataframe and correlation matrix Australia
print(df_Argentina)
corr_Argentina = df_Argentina.corr()
print(corr_Argentina)

# Display the correlation heatmap for Australia
correlation_heatmap(df_Argentina, corr_Argentina, 'Argentina')

# Dataframe for Canada using selected indicators
data_Canada = {
    'Urban pop. growth': data_arable_land_transpose['Canada'],
    'Electricity production': data_electricity_transpose['Canada'],
    'Agric. forestry and Fisheries': data_agriculture_transpose['Canada'],
    'CO2 Emissions': data_CO2_transpose['Canada'],
    'Forest Area': data_forest_area_transpose['Canada'],
    'GDP Annual Growth': data_gdp_transpose['Canada']
}
df_canada = pd.DataFrame(data_Canada)

# Display the dataframe and correlation matrix Canada
print(df_canada)
corr_canada = df_canada.corr()
print(corr_canada)

# Display the correlation heatmap for Canada
correlation_heatmap(df_canada, corr_canada, 'Canada')

# Parameters for producing grouped bar plots of Agriculture land (% of land area) for different years
labels_array_arable = countries
width_arable = 0.2
y_data_arable = [
    data_arable_land['1964'],
    data_arable_land['1971'],
    data_arable_land['1978'],
    data_arable_land['1985']
]
y_label_arable = '% of Land Area'
label_arable = ['Year 1964', 'Year 1971', 'Year 1978', 'Year 1985']
title_arable = 'Agriculture land (% of land area) Comparison for Different Years'

# The parameters are passed into the defined function and produce the desired plot
bar_plot(labels_array_arable, width_arable, y_data_arable, y_label_arable, label_arable, title_arable, rotation=55)

# Plot a multiple line plot for Electricity Production (annual %) for selected countries
x_data_electricity = data_electricity_transpose.index
y_data_electricity = [data_electricity_transpose[country] for country in countries]
xlabel_electricity = 'Years'
ylabel_electricity = '(%) Electricity Production'
labels_electricity = countries
colors_electricity = ['orange', 'pink', 'cyan', 'purple', 'green', 'red', 'blue', 'yellow', 'brown', 'gray', 'teal', 'magenta', 'purple', 'orange', 'blue']
title_electricity = 'Annual (%) of Electricity Production of different Countries'

# Plot the line plots for Electricity Production of selected countries
multiple_plot(x_data_electricity, y_data_electricity, xlabel_electricity, ylabel_electricity, title_electricity, labels_electricity, colors_electricity)

# Extract data for urban population growth
urban_growth_data = data_urban_transpose.loc[:, countries]

# Print urban population growth data
print("Urban Population Growth Data:")
print(urban_growth_data)

# Plot a multiple line plot for Urban Population Growth (%) for selected countries# Extract data for urban population growth
urban_growth_data = data_urban_transpose.loc[:, countries]

# Print urban population growth data
print("Urban Population Growth Data:")
print(urban_growth_data)

# Plot a multiple line plot for Urban Population Growth (%) for selected countries
x_data_urban = urban_growth_data.index
y_data_urban = [urban_growth_data[country] for country in countries]
xlabel_urban = 'Years'
ylabel_urban = '(%) Urban Population Growth'
labels_urban = countries
colors_urban = ['orange', 'pink', 'cyan', 'purple', 'green', 'red', 'blue', 'yellow', 'brown', 'gray', 'teal', 'magenta', 'purple', 'orange', 'blue']
title_urban = 'Annual (%) Urban Population Growth for Selected Countries'

# Plot the line plots for Urban Population Growth of selected countries
multiple_plot(x_data_urban, y_data_urban, xlabel_urban, ylabel_urban, title_urban, labels_urban, colors_urban)

# parameters for producing multiple plots of CO2 emissions (metric tons per capita)
x_data = data_CO2_transpose.index # the  row index is used as the values for the x-axis
y_data = [data_CO2_transpose['Nigeria'], 
          data_CO2_transpose['Brazil'], 
          data_CO2_transpose['Mexico'],
          data_CO2_transpose['Indonesia'], 
          data_CO2_transpose['Argentina'], 
          data_CO2_transpose['Canada']]
xlabel = 'Year'
ylabel = 'metric tons'
labels = ['Nigeria', 'Brazil', 'Mexico', 'Indonesia', 'Argentina', 'Pakistan', 'Canada']
colors = ['red', 'magenta', 'blue', 'yellow', 'green', 'purple', 'black']
title = 'CO2 emissions (metric tons per capita)'

# the attributes are passed into the function and returned to give the desired plot
multiple_plot(x_data, y_data, xlabel, ylabel, title, labels, colors)
