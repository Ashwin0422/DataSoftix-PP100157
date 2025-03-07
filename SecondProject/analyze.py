import pandas as pd
import matplotlib.pyplot as plt

def analyze_csv(data):
    try:
        df = pd.read_csv(data)
        print("\nAvailable columns:", df.columns.tolist())
        column = input("Enter the column name to analyze: ").strip()
        
        if column not in df.columns:
            print("Error: Column not found.")
            return
        df[column] = pd.to_numeric(df[column], errors='coerce')
        df = df.dropna(subset=[column]) 
        
        if df[column].empty:
            print("Error: No valid numerical data in the selected column.")
            return
        
        avg_value = df[column].mean()
        max_value = df[column].max()
        min_value = df[column].min()
        
        print(f"Statistics for column '{column}':")
        print(f"Average: {avg_value}")
        print(f"Maximum: {max_value}")
        print(f"Minimum: {min_value}")
        
        visualize = input("\nWould you like to visualize the data? (yes/no): ").strip().lower()
        if visualize == 'yes':
            plt.hist(df[column], bins=20, edgecolor='black')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title(f'Distribution of {column}')
            plt.show()
        
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

data = input("Enter the path to the CSV file: ").strip()
analyze_csv(data)
