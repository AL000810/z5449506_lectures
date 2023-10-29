# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs,
# with the mapping going from suburb keys to population values.

# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:
#
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.
f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
print(f_suburbs)

# Step 1: Remove suburbs that don't start with "F"
f_suburbs = {suburb: population for suburb, population in f_suburbs.items() if suburb.startswith("F")}

# Step 2: Add or update the specified suburbs and their population values
additional_suburbs = {
    "Fairfield": 18081,
    "Fairfield East": 5273,
    "Fairfield Heights": 7517,
    "Fairfield West": 11575,
    "Fairlight": 5840,
    "Fiddletown": 233,
    "Five Dock": 9356,
    "Flemington": None,
    "Forest Glen": None,
    "Forest Lodge": 4583,
    "Forestville": 8329,
    "Freemans Reach": 1973,
    "Frenchs Forest": 13473,
    "Freshwater": 8866,
}

f_suburbs.update(additional_suburbs)

# Print the resulting dictionary f_suburbs
print(f_suburbs)