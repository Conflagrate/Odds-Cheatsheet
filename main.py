import os
import math

from fractions import Fraction

os.system('pip install --upgrade pip')

# fractional odds: sometimes called British odds or traditional odds and are sometimes written as a fraction, such as 6/1, or expressed as a ratio, like six-to-one.
# decimal odds: represent the amount that is won for every $1 that is wagered. For instance, if the odds are 3.00 that a certain horse wins, the payout is $300 for every $100 wagered.
# american odds: sometimes called moneyline odds and are accompanied by a plus (+) or minus (-) sign, with the plus sign assigned to the lower probability event with the higher payout.

# fractional to decimal
def fractionalToDecimal(fractionalOdds):
  decimalOdds = 1 + fractionalOdds
  return decimalOdds

# fractional to american
def fractionalToAmerican(fractionalOdds):
  if fractionalOdds >= 1:
    americanOdds = 100 * fractionalOdds
  elif fractionalOdds < 1:
    americanOdds = -100 / fractionalOdds 
  return americanOdds

# decimal to fractional
def decimalToFractional(decimalOdds):
  fractionalOdds = decimalOdds - 1
  return Fraction(fractionalOdds)

# decimal to american
def decimalToAmerican(decimalOdds):
  if decimalOdds > 2:
    americanOdds = 100 * (decimalOdds - 1)
  elif decimalOdds < 2:
    americanOdds = -100 / (decimalOdds - 1)
  return americanOdds

# american to decimal
def americanToDecimal(americanOdds):
  if americanOdds > 0:
    decimalOdds = (americanOdds / 100) + 1
  elif americanOdds < 0:
    decimalOdds = (-100 / americanOdds ) + 1
  return decimalOdds

# american to fractional
def americanToFractional(americanOdds):
  if americanOdds > 0:
    fractionalOdds = americanOdds / 100
  elif americanOdds < 0:
    fractionalOdds = -100 / americanOdds
  return fractionalOdds