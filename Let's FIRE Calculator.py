#!/usr/bin/env python
# coding: utf-8

# # Project Description

# FIRE Calculator

# Financial Independence, Retire Early (FIRE) movement aims to encourage individuals to achieve financial independence and retire significantly earlier than traditional retirement ages. By saving and increase passive income, it is important to start investing at young age and accumulate enough wealth to cover the basic needs for living.
# The goal of FIRE is to achieve financial independence, providing the flexibility to choose our lifestyle and preparing for financial risks. By saving and investing, we gain higher chance for a more fulfilling, less stressful life, free from traditional employment constraints, and aligned with personal values and desires.
# 
# This calculator is designed to calculate individual's current assets and investment returns. It contains three of the most common investments that able to help individual to make passive income, which includes bond (commonly considered low risk and low return), stock (higher risk but higher return), real estate (modernate risk but requires management).
# 
# Individual could use this calculator to calculate their current or future investment returns. It will give you an idea of how much passive income or how your money growth through out the time. Hopefully we are all able to achieve the financial freedom and live in a relatively stressless life soon! 
# 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


import investment

from investment import Bond, Stock, RealEstate


# In[2]:


def investment_calculator():
    
    #First let's get the percentage of each investment you would like to allocate.
    name = input('Please enter your name: ')
    print(f'Hi {name}!\nWelcome to the FIRE calculator! Let us start investing and reach the goal together!')
    
    total_amount = float(input("Enter the total amount of money you want to invest: $"))
    bond_percentage = float(input("Enter the percentage of money to invest in bonds: ")) / 100
    stock_percentage = float(input("Enter the percentage of money to invest in stocks: ")) / 100
    real_estate_percentage = float(input("Enter the percentage of money to invest in real estate: ")) / 100

    bond_amount = total_amount * bond_percentage
    stock_amount = total_amount * stock_percentage
    real_estate_amount = total_amount * real_estate_percentage

    total_years = int(input('Please enter the length of years: '))

    # Bond
    bond_apr = float(input('Please enter the APR% of the bond in percentage: ')) / 100
    bond = Bond(bond_amount, bond_apr, total_years)

    # Stock
    stock_annual_growth = float(input('Please enter the expected annual growth of the stock in percentage: ')) / 100
    stock = Stock(stock_amount, stock_annual_growth, total_years)

    # Real Estate
    real_estate_appreciation_rate = float(input("Please enter the annual appreciation rate for real estate: ")) / 100
    real_estate_rental_income = float(input("Please enter the annual rental income for real estate: "))
    down_payment = float(input("Please enter the down payment for the real estate investment: $"))
    mortgage_rate = float(input("Please enter the annual mortgage rate in percentage: ")) / 100
    tax_rate = float(input("Please enter the annual tax rate in percentage: ")) / 100
    hoa_fees = float(input("Enter the annual HOA fees: $"))
    maintenance_cost = float(input("Enter the annual maintenance cost: $"))
    real_estate = RealEstate(real_estate_amount, real_estate_appreciation_rate, total_years, real_estate_rental_income, down_payment, mortgage_rate, tax_rate, hoa_fees, maintenance_cost)

    # Calculate returns
    bond_return = bond.calculate_return()
    stock_return = stock.calculate_return()
    real_estate_return = real_estate.calculate_return()

    # Display results
    print("\nInvestment Details and Returns:\n")
    print(bond.get_details())
    print(f"Return after {total_years:.2f} year(s): ${bond_return:.2f}\n")
    print(stock.get_details())
    print(f"Return after {total_years:.2f} year(s): ${stock_return:.2f}\n")
    print(real_estate.get_details())
    print(f"Return after {total_years:.2f} year(s): ${real_estate_return:.2f}\n")

    # Total return
    total_return = bond_return + stock_return + real_estate_return
    print(f"Total Return after {total_years:.2f} year(s): ${total_return:.2f}")

#We could also use this calculator to access the risk our current investment profolio.
def risk_accessment(bond_percentage, stock_percentage, real_estate_percentage):
    if bond_percentage >= 0.5 and bond_percentage <= 1:
        output = 'Relative low risk'
    elif stock_percentage >= 0.5 and stock_percentage <= 1:
        output = 'High risk'
    elif real_estate_percentage >= 0 and real_estate_percentage < 0.5:
        output = 'Modernate risk'
    elif real_estate_percentage > 0.5 and real_estate_percentage <= 1:
        output = 'Relative high risk'
    elif stock_percentage >= 0.25 and stock_percentage < 0.5:
        output = 'Modernate rate'
    else:
        output = 'High risk'
    return output
        


# In[3]:


# test it out
current_risk = risk_accessment(0.25, 0.35, 0.4)
print(current_risk)


# In[4]:


Bond(1000, 0.03, 1)
bond_risk = Bond.risk_evaluation(1000)
print(bond_risk)


# In[5]:


current_stock = Stock(10000, 0.09, 10)
current_stock_return = current_stock.calculate_return()
print(current_stock_return)


# In[6]:


current_real_estate = RealEstate(1000000, 0.03, 20, 50000, 500000, 0.07, 0.01, 0, 5000)
current_real_estate_return = current_real_estate.calculate_return()
print(current_real_estate_return)


# In[7]:


real_estate_details = current_real_estate.get_details()
print(real_estate_details)


# In[8]:


investment_calculator()


# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. I self learned python before taking this course through coursera. However, this course do provide me more practices in coding and hopefully I could do more stuff and utilizing python in my research.
# 
# 2. I started my idea with a calculator of real-estate investment to help individual determine if a real estate is worth purchasing under the high interest rate circumstance. But the idea of FIRE came through my mind so I included two other common types of investments (bond and stock) in my calculator. I also included an evaluation for individual to see the risk of their current asset allocation. It took more hours than I expected since there are many calculations especially in the real estate part. I got stucked in some minor errors though calculations and using integer/float in the command 'in range'. ChatGPT also optimize my calculator by introducing f-string to me, so I am able to display the details of each investment in a more user friendly way.

# In[ ]:




