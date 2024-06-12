class Bond():
    
    '''This class aim to calculate and show the details of bond investment.
    
    ---------
    Instance attribute:
        amount
        apr
        years
    
    -----------
    Methods:
        calculate_return
        risk_evaluation
        get_details
    '''
    
    def __init__(self, amount, apr, years):
        self.amount = amount
        self.apr = apr
        self.years = years
    
    def calculate_return(self):
        return self.amount * ((1 + self.apr) ** self.years)
    
    def risk_evaluation(self):
        return 'conserved'
    
    def get_details(self):
        return f"Bond Investment: ${self.amount:.2f}\nAPR: {self.apr * 100:.2f}%\nYears: {self.years:.2f}"


class Stock():
    
    '''
    This class Stock aim to calculate the return of stock investment and help individual to evaluate risk and get details of this investment.
    
    ----------
    Instance attributes:
        amount
        annual_growth_rate
        years
    
    
    ----------
    Methods:
        calculate_return
        risk-evaluation
        get_details
    '''
    
    def __init__(self, amount, annual_growth_rate, years):
        self.amount = amount
        self.annual_growth_rate = annual_growth_rate
        self.years = years
    
    def calculate_return(self):
        return self.amount * ((1 + self.annual_growth_rate) ** self.years)
    
    def risk_evaluation(self):
        return 'aggressive'
    
    def get_details(self):
        return f"Stock Investment: ${self.amount:.2f}\nAnnual Growth Rate: {self.annual_growth_rate * 100:.2f}%\nYears: {self.years:.2f}"

class RealEstate():
    
    ''' 
    This class RealEstate aim to calculate the return of a real estate investment. The return is determined by counting the total earning minus total cost from the real estate. This class is also able to determine the apprieciation of the real estate, calculate monthly mortgage, and property tax. Same as previous investments, it is also able to evaluate the risk and get details.
    
    ---------
    Instance attributes:
        amount 
        annual_appreciation_rate 
        years 
        annual_rental_income 
        down_payments 
        mortgage_rate 
        tax_rate 
        hoa_fees 
        maintenance_cost
        
    ----------
    Methods:
        calculate_monthly_mortgage
        calculate_property_tax_increase
            ---------
            Parameters:
                initial_assessed_value
                base_tax_rate
                additional_taxes
        calculate_return
        risk_evaluation
        get_details
    '''
    
    def __init__(self, amount, annual_appreciation_rate, years, annual_rental_income, down_payments, mortgage_rate, tax_rate, hoa_fees, maintenance_cost):
        
        self.amount = amount
        self.annual_appreciation_rate = annual_appreciation_rate
        self.annual_rental_income = annual_rental_income
        self.years = years
        self.down_payments = down_payments
        self.mortgage_rate = mortgage_rate
        self.tax_rate = tax_rate
        self.hoa_fees = hoa_fees
        self.maintenance_cost = maintenance_cost
    
    def calculate_monthly_mortgage(self):
        
        loan_amount = self.amount - self.down_payments
        monthly_rate = self.mortgage_rate / 12
        num_payments = int(self.years) * 12
        monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
        
        return monthly_payment
    
    def calculate_property_tax_increase(self, initial_assessed_value, base_tax_rate, additional_taxes):
        
        property_tax_values = []
        previous_property_tax = initial_assessed_value * base_tax_rate
        num_years = int(self.years)
        
        for year in range(1, num_years + 1):
            total_property_tax = previous_property_tax + additional_taxes
            property_tax_values.append(total_property_tax)
            initial_assessed_value *= 1 + self.annual_appreciation_rate
            previous_property_tax = initial_assessed_value * base_tax_rate
        
        return property_tax_values
        
    
    def calculate_return(self):
        appreciation = self.amount * ((1 + self.annual_appreciation_rate) ** self.years)
        rental_income = self.annual_rental_income * self.years
        mortgage_cost = self.calculate_monthly_mortgage() * 12 * self.years
        tax_cost = sum(self.calculate_property_tax_increase(self.amount, self.tax_rate, 0))
        total_hoa_fees = self.hoa_fees * self.years
        total_maintenance_cost = self.maintenance_cost * self.years
        total_costs = mortgage_cost + tax_cost + total_hoa_fees + total_maintenance_cost
        return appreciation + rental_income - total_costs
    
    def risk_evaluation(self):
        return 'modernate'
        
    def get_details(self):
        return (f"Real Estate Investment: ${self.amount:.2f}\n"
                f"Annual Appreciation Rate: {self.annual_appreciation_rate * 100:.2f}%\n"
                f"Annual Rental Income: ${self.annual_rental_income:.2f}\n"
                f"Years: {self.years:.2f}\n"
                f"Down Payments: ${self.down_payments:.2f}\n"
                f"Mortgage Rate: {self.mortgage_rate * 100:.2f}%\n"
                f"Tax Rate: {self.tax_rate * 100:.2f}%\n"
                f"HOA Fees: ${self.hoa_fees:.2f} per year\n"
                f"Maintenance Cost: ${self.maintenance_cost:.2f} per year")

    #citation: ChatGPT 3.5 introduce f-string to embed numbers and result from methods in a piece of string    
