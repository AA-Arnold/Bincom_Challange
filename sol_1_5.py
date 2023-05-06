'''
This file contains the solution to the following question

1.      Which color of shirt is the mean color?
2.      Which color is mostly worn throughout the week?
3.      Which color is the median?
4.      BONUS Get the variance of the colors
5.      BONUS if a colour is chosen at random, what is the probability that the color is red?

'''

import re
import pprint
import statistics

# Read the HTML file
with open("python_class_question.html") as fp:
    html = fp.read()

# Use regex to extract the day and color data and store it as a dict
pattern = r"<tr>\n\s*<td>(\w+)</td>\n\s*<td>(.*?)</td>\n\s*</tr>"
matches = re.findall(pattern, html, re.DOTALL)
data = {}
for match in matches:
    day = match[0]
    colors = match[1].split(", ")
    data[day] = colors


# Extract all the color values from the dictionary and convert them to a list
all_colors = []
for colors in data.values():
    all_colors.extend(colors)

# Getting color frequency
color_freq = {}
# Loop through the colors list and update the color frequency
for color in all_colors:
    if color in color_freq:
        color_freq[color] += 1
    else:
        color_freq[color] = 1

color_values = list(color_freq.values())

# Probability
num_red = all_colors.count('RED')
total_colors = len(all_colors)
probability_red = num_red / total_colors


variance = statistics.variance(color_values)
mean = statistics.mean(color_values)
mode = statistics.mode(all_colors)
median = statistics.median(all_colors)

pprint.pprint(f'solution 1 -----> Using the number of occurence of each color the mean is {mean} the colors that satisfies that are the color "ORANGE & RED"')
print(f'solution 2 -----> The color {mode} is mostly worn throughout the week')
print(f'solution 3 -----> The color {median} is the median')
print(f'solution 4 -----> The variance is {variance}')
print(f"solution 5 -----> The probability of choosing the color red is:", probability_red)
