import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def load_data():
    dataframe = pd.read_csv("iris.csv")
    return dataframe

dataframe = load_data()

def species_data(dataframe,species=None):
    if species is None:
        dataframe = dataframe
    return dataframe[dataframe.species == species]

def regression_analysis(species_data):
    x = species_data.petal_length_cm
    y = species_data.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("petal_v_sepal_length_regress.png")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Perform regression analysis on iris dataset") 
    parser.add_argument("--species", default="setosa", help="Species to analyze")
    args = parser.parse_args()  

    species = args.species
    species_data = species_data(dataframe, species)
    regression_analysis(species_data)