import numpy as np
import pandas as pd
import random

# Create an array with 12 different colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple',
          'pink', 'brown', 'grey', 'black', 'white', 'silver']

# Generate 1000 random color samples
color_samples = [random.choice(colors) for i in range(1000)]

# Convert the color samples to a numerical label using the `pd.factorize` function
color_labels, color_uniques = pd.factorize(color_samples)

# Convert the color labels to a one-hot encoded representation using the `pd.get_dummies` function
one_hot_labels = pd.get_dummies(color_labels)

# Create a data frame with the one-hot encoded labels and the original color samples
data = pd.DataFrame(one_hot_labels)
data['colors'] = color_samples

# Export the data frame to a CSV file
data.to_csv('color_data.csv', index=False)
