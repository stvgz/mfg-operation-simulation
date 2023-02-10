from sklearn.linear_model import LinearRegression
import pandas as pd
import os
import numpy as np
from scipy.stats import skewnorm

# Linear regression with one variable, return intercept and slope

def linear_regression_one_variable(x, y):
    model = LinearRegression()
    model.fit(x, y)
    
    return model.intercept_[0], model.coef_[0][0]


def get_product():
    
    from ops_config import BASE_DIR
    
    df = pd.read_csv(os.path.join(BASE_DIR, 'product.csv'))
    
    return df


def map_product(df, has = 'product_id', need = 'product_code'):
    """has = product_id or product_code"""
    product = get_product()
    product = product[[has, need]]
    
    _ = pd.merge(df,product,left_on=has, right_on=has)
    
    return _

# Generate a number based on gaussian distribution
def generate_gaussian(mean, std):
    return np.random.normal(mean, std)

# Generate a number based on skew normal distribution
def generate_skewnorm(size = 1, loc = 0, mode = 'hard', scale = 1):

    # as skewnorm
    
    a = 100
    mean, var, skew, kurt = skewnorm.stats(a, moments='mvsk', loc=loc, scale=scale)
    r = skewnorm.rvs(a, size=size)
    
    if size == 1:
        return r[0]
    else:
        return r.tolist()