import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.stats import chi2_contingency

def chi_square_test(contingency_table, alpha=0.05):
    """
    Perform a Chi-Square test of independence and interpret the results.

    Parameters:
    - contingency_table: pandas DataFrame or 2D array-like
      The observed frequencies in a contingency table.
    - alpha: float, optional (default=0.05)
      The significance level for rejecting the null hypothesis.

    Returns:
    - None
    """
    # Perform the Chi-Square test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    # Print results
    print(f"Chi-Square Statistic: {chi2:.4f}")
    print(f"P-value: {p:.4e}")
    print(f"Degrees of Freedom: {dof}")
    print(f"Significance Level (alpha): {alpha}")
    
    # Decision
    if p < alpha:
        print("Decision: Reject H0 (The variables are not independent).")
    else:
        print("Decision: Fail to reject H0 (No evidence of dependence).")
    
    # Optional: Print expected frequencies
    print("\nExpected Frequencies:")
    for row in expected:
        print("  ", [f"{x:.2f}" for x in row])
    return chi2, p, dof, expected

def cal_cramer_v(contingency_table):
    """
    to calculate Cramer's V to find the assocation

    Parameters
    ----------
    contingency_table : _type_
        pandas DataFrame or 2D array-like
    """
    chi2, _, _, _ = chi2_contingency(contingency_table)

    n = np.sum(contingency_table.values)
    k = min(contingency_table.shape)
    v = np.sqrt(chi2/(n*k))

    return v

def cal_cramer_v_adjusted(contingency_table):
    """
    to calculate Cramer's V adjusted to find the assocation (for large table with small samples)

    Parameters
    ----------
    contingency_table : _type_
        pandas DataFrame or 2D array-like

    # Example data: Contingency table
        data = np.array([[123, 203, 9704],
                        [27, 6, 98]])

        # Convert to DataFrame for visualization
        contingency_table = pd.DataFrame(data, columns=["Current Smoker", "Previous Smoker", "Never Smoker"], 
                                        index=["No", "Yes"])

        cal_cramer_v_adjusted(contingency_table)
    """
    chi2, _, _, _ = chi2_contingency(contingency_table)
    n = np.sum(contingency_table.values)
    n_row, n_col = contingency_table.shape
    
    numerator = max(0, chi2/n - (n_col-1)*(n_row-1)/(n-1))
    
    def cal_k_val(num, n):
        val = num-1/(n-1)*(r-1)**2
        return val
    k_col = cal_k_val(n_col, n)
    k_row =  cal_k_val(n_row, n)
    denominator = min(k_col, k_row)
   
    v = np.sqrt(numerator/denominator)

    return v