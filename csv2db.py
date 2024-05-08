import csv
from database.operations import insert_db_data
import os
from pprint import pprint as pp
from termcolor import cprint
from tqdm import tqdm
os.system('color')

cprint(f"\n Processing CSV file...", "green", attrs=['reverse'])

num_lines = sum(1 for line in open('data_2023.csv', encoding="'utf-8"))

with tqdm (total=num_lines) as pbar:

    with open('data_2023.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')

        line_count = 0

        for row in reader:
            if line_count!=0:
                result = insert_db_data(name=row[5], age_group=row[6], household_type=row[7], apartment_type=row[8], 
                                life_situation=row[9], paid=row[10])
                print(f"Inserted row number {line_count} with id={result}")
                
            line_count+=1
            pbar.update(1)
pbar.close()
