import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def model(n, i, j):
    """
    Model function for fitting the data.

    Args:
        n (ndarray): Independent variable data.
        i (float): Parameter for curve fitting.
        j (float): Parameter for curve fitting.

    Returns:
        ndarray: Fitted y-values.
    """
    return i * (j ** n)

def fit_curve(x_data, y_data):
    """
    Fit the curve to the given data.
    
    Args:
        x_data (ndarray): Independent variable data.
        y_data (ndarray): Dependent variable data.
    
    Returns:
        Tuple[float, float, ndarray]: Fitted parameters (i, j) and fitted y-values.
    """
    # Estimate initial guesses for i and j
    initial_i = np.max(y_data)
    initial_j = y_data[-1] / y_data[-2] if len(y_data) > 1 else 1.0

    # Use curve_fit to find the optimal i and j
    popt, _ = curve_fit(model, x_data, y_data, p0=(initial_i, initial_j))

    # Extract fitted parameters
    i_fitted, j_fitted = popt

    # Generate fitted y-values using the fitted parameters
    y_fitted = model(x_data, i_fitted, j_fitted)

    return i_fitted, j_fitted, y_fitted

def process_and_fit_data(x_data, y_data):
    """
    Process and fit the given data.

    Args:
        x_data (ndarray): Independent variable data.
        y_data (ndarray): Dependent variable data.

    Returns:
        Tuple[float, float, ndarray]: Fitted parameters (i, j) and fitted y-values.
    """
    # Estimate initial guesses for i and j
    initial_i = np.max(y_data)  # Initial guess for i
    initial_j = y_data[-1] / y_data[-2] if len(y_data) > 1 else 1.0  # Initial guess for j

    print(f"Initial guess for i: {initial_i}")
    print(f"Initial guess for j: {initial_j}")

    # Fit the curve to the given data
    i_fitted, j_fitted, y_fitted = fit_curve(x_data, y_data)

    # Print fitted parameters
    print(f"Fitted parameters: i = {i_fitted:.2f}, j = {j_fitted:.2f}")
    print(f"Equation between your risk and share is {round(i_fitted)}({round(j_fitted,2)}^n )")

    return i_fitted, j_fitted, y_fitted

def plot_data_and_curve(x_data, y_data, y_fitted):
    """
    Plot the given data and the fitted curve.

    Args:
        x_data (ndarray): Independent variable data.
        y_data (ndarray): Dependent variable data.
        y_fitted (ndarray): Fitted y-values.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, label='Data')
    plt.plot(x_data, y_fitted, label='Fitted curve', color='red')
    plt.xlabel("x data")
    plt.ylabel("y data")
    plt.title("Fitted curve for given data")
    plt.legend()
    plt.grid(True)
    plt.show()

def data_mine():
    x_data = np.fromstring(input("Enter x_data separated by commas or spaces: "), sep=',')
    y_data = np.fromstring(input("Enter y_data separated by commas or spaces: "), sep=',')

    return x_data, y_data


if __name__ == "__main__":
    #data
    x_data, y_data = data_mine()

    # Process and fit the data
    i_fitted, j_fitted, y_fitted = process_and_fit_data(x_data, y_data)

    # Plot the data and the fitted curve
    plot_data_and_curve(x_data, y_data, y_fitted)
