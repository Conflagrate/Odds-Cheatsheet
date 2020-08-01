# GREEN : '\033[92m'
# RED : '\033[91m'
# END : '\033[0m'

# ODDS ON : Easier to win, but less rewards.
# ODDS AGAINST : Harder to win, but more rewards.

# MONEYLINE (+) : Stake x (Odds / 100) = Potential Profit OR Stake x (Odds / 100) + Stake = Potential Return.
# MONEYLINE (-) : Stake / (Odds / 100) = Potential Profit OR Stake / (Odds / 100) + Stake = Potential Profit.

import fractions

odds = input('\nOdds? > ')

strippedOdds = odds.replace('-', '') if '-' in odds else odds.replace('+', '')
monetizedOdds = f'${strippedOdds}'
coloredOdds = '\033[92m' + odds + '\033[0m' if '-' in odds else '\033[91m' + odds + '\033[0m'

greenMoreLikely = '\033[92m' + 'more likely' + '\033[0m'
greenHigherColor = '\033[92m' + 'higher' + '\033[0m'
redLessLikely = '\033[91m' + 'less likely' + '\033[0m'
redLowerColor = '\033[91m' + 'lower' + '\033[0m'

print(f'With a moneyline of {coloredOdds}, you are {greenMoreLikely} to win. However, your profit will be {redLowerColor} due to the {greenHigherColor} likelihood of winning. If a {monetizedOdds} is placed, you will profit $100. This moneyline is equal to fractional odds of ' if '-' in odds else f'With a moneyline of {coloredOdds}, you are {redLessLikely} to win. However, your profit will be {greenHigherColor} due to the {redLowerColor} likelihood of winning. If a $100 is placed, you will profit {monetizedOdds}.')