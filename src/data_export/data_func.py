

from datetime import datetime, timedelta

def subtract_months_from_now(num_of_months):
    today = datetime.now()
    new_date = today - timedelta(days=num_of_months * 30)  # Approximation: Assuming 30 days per month

    return new_date.month, new_date.year

# Example usage of the function to subtract 3 months from the current date
num_months_to_subtract = 72
result_year = subtract_months_from_now(num_months_to_subtract)


