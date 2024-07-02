from datetime import datetime, timedelta

data = [
    (16.25, '05/01/2024'),
    (15.20, '03/01/2024'),
    (15.10, '11/01/2023'),
    (14.75, '08/01/2023'),
    (14.97, '05/01/2023'),
    (14.55, '03/01/2023'),
    (13.19, '11/01/2022'),
    (13.84, '08/01/2022'),
    (14.91, '05/01/2022'),
    (13.76, '04/15/2022'),
    (13.76, '03/01/2022'),
    (13.28, '11/01/2021'),
    (12.62, '08/01/2021'),
    (12.26, '05/01/2021'),
    (12.04, '03/01/2021'),
    (11.59, '11/01/2020'),
    (10.87, '08/01/2020'),
    (10.02, '05/01/2020'),
    (9.78, '03/01/2020'),
    (9.42, '11/01/2019'),
    (8.82, '08/01/2019'),
    (8.95, '05/01/2019'),
    (8.57, '03/01/2019'),
    (8.54, '11/01/2018'),
    (8.51, '08/01/2018'),
    (8.35, '05/01/2018'),
    (8.28, '03/01/2018'),
    (7.37, '11/01/2017'),
    (7.21, '08/01/2017'),
    (7.83, '05/01/2017'),
    (8.18, '03/01/2017'),
    (8.03, '11/01/2016'),
    (8.38, '08/01/2016'),
    (8.79, '05/01/2016'),
    (9.04, '03/01/2016'),
    (8.36, '11/01/2015'),
    (8.40, '08/01/2015'),
    (8.42, '05/01/2015'),
    (7.81, '03/01/2015'),
    (6.76, '11/01/2014'),
    (6.77, '08/01/2014'),
    (6.50, '05/01/2014'),
    (6.03, '03/01/2014'),
    (6.00, '11/01/2013'),
    (5.51, '08/01/2013'),
    (5.38, '05/01/2013'),
    (4.64, '03/01/2013'),
    (4.50, '11/01/2012'),
    (4.40, '08/01/2012'),
    (4.54, '05/01/2012'),
    (4.48, '03/01/2012'),
    (4.04, '11/01/2011'),
    (4.41, '08/01/2011'),
    (4.33, '05/01/2011'),
    (4.18, '03/01/2011'),
    (3.97, '11/01/2010'),
    (3.69, '08/01/2010'),
    (3.70, '05/01/2010'),
    (3.47, '03/01/2010'),
    (3.26, '11/01/2009'),
    (3.21, '08/01/2009'),
    (3.11, '05/01/2009'),
    (3.22, '03/01/2009'),
    (3.58, '11/01/2008'),
    (3.94, '08/01/2008'),
    (3.89, '05/01/2008'),
    (4.14, '03/01/2008'),
    (4.16, '11/01/2007'),
    (4.18, '08/01/2007'),
    (4.18, '05/01/2007'),
    (3.98, '03/01/2007'),
    (3.92, '11/01/2006'),
    (3.65, '08/01/2006'),
    (3.53, '07/01/2006'),
    (3.53, '05/01/2006'),
    (3.22, '03/01/2006'),
    (3.09, '11/01/2005'),
    (2.91, '08/01/2005'),
    (2.66, '05/01/2005'),
    (2.56, '03/01/2005'),
    (2.34, '11/01/2004'),
    (2.34, '08/01/2004'),
    (2.09, '05/01/2004'),
    (2.06, '03/01/2004'),
    (1.86, '11/01/2003'),
    (1.69, '08/01/2003'),
    (1.50, '05/01/2003'),
    (1.54, '03/01/2003'),
    (1.48, '11/01/2002'),
    (1.60, '08/01/2002'),
    (1.76, '05/01/2002'),
    (1.64, '03/01/2002'),
    (1.64, '11/01/2001'),
    (1.90, '08/01/2001'),
    (1.94, '05/01/2001'),
    (1.93, '03/01/2001'),
    (1.88, '11/01/2000'),
    (1.86, '08/01/2000'),
    (1.82, '05/01/2000'),
    (1.80, '03/01/2000'),
    (1.78, '11/01/1999'),
    (1.86, '03/01/1999'),
    (1.64, '11/01/1998'),
    (1.53, '08/01/1998'),
    (1.39, '05/01/1998'),
    (1.23, '03/01/1998'),
    (0.93, '11/01/1997'),
    (0.92, '08/01/1997'),
    (0.87, '05/01/1997'),
    (0.84, '03/01/1997'),
    (0.83, '11/01/1996'),
    (0.80, '08/01/1996'),
    (0.74, '05/01/1996'),
    (0.67, '03/01/1996'),
    (0.65, '11/01/1995'),
    (0.62, '08/01/1995'),
    (0.57, '05/01/1995'),
    (0.57, '03/01/1995'),
    (0.55, '11/01/1994'),
    (0.52, '08/01/1994'),
    (0.52, '05/01/1994'),
    (0.49, '03/01/1994'),
    (0.44, '11/01/1993'),
    (0.46, '08/01/1993'),
    (0.46, '04/29/1993'),
    (0.45, '03/17/1993'),
    (0.46, '11/01/1992'),
    (0.43, '08/01/1992'),
    (0.42, '07/01/1992'),
    (0.42, '05/01/1992'),
    (0.37, '11/01/1991'),
    (0.38, '08/01/1991'),
    (0.42, '05/01/1991'),
    (0.36, '11/07/1990'),
    (0.34, '08/01/1990'),
    (0.33, '05/02/1990'),
    (0.32, '11/16/1989'),
    (0.28, '09/01/1989'),
    (0.24, '05/02/1989'),
    (0.22, '11/15/1988'),
    (0.21, '11/17/1987'),
    (0.19, '11/14/1986'),
    (0.14, '07/29/1986'),
    (0.14, '04/01/1986'),
    (0.13, '08/01/1985'),
    (0.12, '11/15/1984'),
    (0.10, '08/07/1984'),
    (0.08, '02/25/1984'),
    (0.08, '11/16/1983'),
    (0.07, '11/24/1982'),
    (0.05, '11/03/1981'),
    (0.05, '12/03/1979'),
    (0.04, '11/27/1978'),
    (0.04, '09/15/1978'),
    (0.04, '04/03/1978'),
    (0.03, '11/03/1977'),
    (0.03, '07/01/1977'),
    (0.03, '12/01/1976'),
    (0.02, '09/01/1976'),
    (0.02, '03/24/1976'),
    (0.02, '12/22/1975'),
    (0.02, '08/01/1975'),
    (0.02, '10/01/1974'),
    (0.02, '01/01/1974'),
    (0.02, '08/24/1973'),
    (0.02, '01/01/1973'),
    (0.01, '03/23/1972'),
    (0.01, '02/02/1972'),
    (0.01, '03/01/1971'),
    (0.01, '01/01/1970'),
    (0.01, '02/25/1969'),
    (0.01, '01/01/1968'),
    (0.01, '08/01/1966'),
    (0.01, '01/01/1966'),
    (0.01, '01/01/1965')
]

# Function to calculate average annual growth rate and future stock price
def calculate_growth_rate(data, start_date, end_date):
    # Parse start_date and end_date into datetime objects
    start_date = datetime.strptime(start_date, '%m/%d/%Y')
    end_date = datetime.strptime(end_date, '%m/%d/%Y')
    
    # Filter prices and dates based on start_date and end_date
    filtered_prices = []
    filtered_dates = []
    for price, date_str in data:
        date = datetime.strptime(date_str, '%m/%d/%Y')
        if start_date <= date <= end_date:
            filtered_prices.append(price)
            filtered_dates.append(date)
    
    # Check if there are data points within the specified date range
    if len(filtered_prices) == 0:
        print(f"No data points found between {start_date.strftime('%Y-%m-%d')} and {end_date.strftime('%Y-%m-%d')}.")
        return None, None
    
    # Calculate growth rate
    initial_price = filtered_prices[0]
    final_price = filtered_prices[-1]
    num_years = (filtered_dates[-1] - filtered_dates[0]).days / 365.25  # Approximate years
    growth_rate = (final_price / initial_price) ** (1 / num_years) - 1
    
    return growth_rate

def calculate_future_stock_price(growth_rate, num_shares, current_stock_price, current_date_str):
    future_stock_prices = []
    
    # Define the dates as strings
    stock_split_date_str = '04/14/2022'

    current_date = datetime.strptime(current_date_str, '%m/%d/%Y')

    # Convert stock split date string to datetime object
    stock_split_date = datetime.strptime(stock_split_date_str, '%m/%d/%Y')

    # Calculate days since stock split
    days_since_stock_split = (current_date - stock_split_date).days

    # Define split factor and split check condition (13 years)
    split_factor = 5
    split_condition_days = (365.25 * 13)

    # Calculate future stock prices for each year from 1 to 40
    for years in range(1, 46):  # Loop through years 1 to 40
        if days_since_stock_split >= split_condition_days:
            print("\nApplying stock split...")
            # Apply stock split
            num_shares *= split_factor
            current_stock_price /= split_factor
            days_since_stock_split = 0
        else:
            days_since_stock_split += 365.25
            print(f"\nDays since stock split: {days_since_stock_split}")
            print("\nNo stock split applied, applying growth rate...")
            # No stock split, apply growth rate
            current_stock_price *= (1 + growth_rate)
        
        # Calculate future stock price after adjusting for splits or growth rate
        future_stock_price = current_stock_price * num_shares
        future_stock_prices.append(future_stock_price)
    
    return future_stock_prices



def print_future_stock_prices(future_stock_prices):
    # Print future stock prices in intervals of 5 years
    for i in range(5, len(future_stock_prices), 5):
        years = i
        print(f"Future stock price in {years} years: ${future_stock_prices[i]:,.2f}")


# Function to get user input for start and end dates
def get_user_dates():
    while True:
        start_date = input("Enter start date (MM/DD/YYYY): ")
        end_date = input("Enter end date (MM/DD/YYYY): ")
        
        try:
            # Attempt to parse dates
            datetime.strptime(start_date, '%m/%d/%Y')
            datetime.strptime(end_date, '%m/%d/%Y')
            break
        except ValueError:
            print("Invalid date format. Please enter dates in MM/DD/YYYY format.")
    
    return start_date, end_date

# Example usage with user input
def main():
    start_date, end_date = get_user_dates()
    growth_rate = calculate_growth_rate(data, start_date, end_date)
    
    if growth_rate is not None:
        print(f"Average annual growth rate from {start_date} to {end_date}: {growth_rate:.4f}")
        
        # Get current stock information from user
        num_shares = float(input("Enter number of shares you own: "))
        current_stock_price = float(input("Enter current stock price: $"))
        current_date_str = input("Enter the last stock date (MM/DD/YYYY): ")
            
    # Calculate future stock prices
    future_stock_prices = calculate_future_stock_price(growth_rate, num_shares, current_stock_price, current_date_str)
    
    # Print future stock prices in intervals of 5 years
    print_future_stock_prices(future_stock_prices)

if __name__ == "__main__":
    main()
