'''
This file contains the solution to the following question

6.Save the colours and their frequencies in postgresql database

'''

import sqlalchemy 
import re


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
        


url = "postgresql://testuser:0000@127.0.0.1:5432/testdb"
engine = sqlalchemy.create_engine(url)
# engine.execution_options()


try:
	engine.connect()
	print('[*] Database server connection established!\n')
	table_name = 'tbl_staff_dress_code'
	query = '''
                CREATE TABLE tbl_staff_dress_code (
                _id serial PRIMARY KEY,                 
                colors VARCHAR(20) UNIQUE NOT NULL,
                color_frequency INTEGER
                );
	        '''
	with engine.begin() as conn:
		result = conn.execute(sqlalchemy.text(f"SELECT EXISTS (SELECT 1 FROM pg_catalog.pg_tables WHERE schemaname = 'public' AND tablename = '{table_name}');"))
		table_exists = result.fetchone().count(1)
		
		if table_exists:
			print(f"Table {table_name} exists in the database. inserting colors")
			for color, frequency in color_freq.items():
			    conn.execute(sqlalchemy.text(f"INSERT INTO {table_name} (colors, color_frequency) VALUES ('{color}', {frequency});"))
		else:
			print(f"Table {table_name} does not exist in the database creating table ...")
			result = conn.execute(sqlalchemy.text(query))
		

except Exception as e:
	print(f'[X] Database server connection failed: {e}')