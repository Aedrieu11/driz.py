import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load CSV data into a pandas DataFrame."""
    return pd.read_csv(file_path)

def basic_statistics(df):
    """Calculate basic statistics for numerical columns."""
    return df.describe()

def plot_correlation_heatmap(df):
    """Plot a correlation heatmap for numerical features."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Feature Correlation Heatmap")
    plt.show()

def plot_histograms(df):
    """Plot histograms for numerical features."""
    df.hist(figsize=(12, 8), bins=20)
    plt.suptitle("Feature Distributions")
    plt.show()

def main():
    file_path = "data.csv" 
    df = load_data(file_path)
    
    print("Basic Statistics:")
    print(basic_statistics(df))
    
    plot_correlation_heatmap
    plot_platograms 

    
if __name__ == "__main__":
    main()