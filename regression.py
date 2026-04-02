#!/usr/bin/env python3

"""Perform regression analysis on the iris 
dataset and save the plot to a file."""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import argparse

def load_data(data_path: str="iris.csv") -> pd.DataFrame:
    '''Load the data from a CSV file and 
    return it as a pandas DataFrame.
    
    Args:
        `data_path:` The path to the CSV file containing the data.
        
        `Returns:` 
        A pandas DataFrame containing the loaded data.
        '''
    dataframe = pd.read_csv(data_path)
    return dataframe

def species_data(dataframe: pd.DataFrame, species: str=None) -> pd.DataFrame:
    '''Filter the DataFrame for a specific species.
    
    `Args:`
        dataframe: A pandas DataFrame containing the data.
        species: The species to filter for. If None, return the entire DataFrame.
        
        `Returns:` A pandas DataFrame containing the filtered data.
        
        '''
    if species is None:
        return dataframe
    return dataframe[dataframe.species == species]

def regression_analysis(species_data: pd.DataFrame, output_file: str="petal_v_sepal_length_regress.png")-> None:
    """Perform regression analysis on the petal length and sepal length
      of the given species data and save the plot to a file.
      
      Args: 
      species_data: A pandas DataFrame containing the data for a specific species.
        output_file: The name of the file to save the plot to.

         Returns:
            None
    """
    x = species_data.petal_length_cm
    print(x)
    y = species_data.sepal_length_cm
    print
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig(output_file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        formatter_class = argparse.ArgumentDefaultsHelpFormatter,
        description="Perform regression analysis on iris dataset"
    )
    parser.add_argument("-s", "--species", 
                        default="Iris_setosa",
                        metavar="SPECIES",
                         help="Species to analyze")
    
    parser.add_argument("-d", "--data",
                        default='dataframe',
                        metavar="DAT",
                        help="This is the data to be analyzed")
    
    #parser.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    parser.add_argument("-o", "--output",
                        default="petal_v_sepal_length_regress.png",
                        metavar="OUT",
                        help="Output file for the plot") 
    
    args = parser.parse_args()  
    print(f"Loading the data from the file {args.data}")
    dataframe = load_data(args.data)
    
    print(f"Performing regression analysis for the species {args.species}")
    species = args.species
    species_data = species_data(dataframe, species)
    regression_analysis(species_data, args.output)
    print("Regression analysis complete. Plot saved as " + args.output)