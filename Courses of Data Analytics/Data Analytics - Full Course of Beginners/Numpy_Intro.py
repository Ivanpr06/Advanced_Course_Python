import random
import statistics
import numpy as np

salary_list = [random.randint(5000, 10000) for i in range(1000000)]

def media():
 # Con statistics tarda mucho más en hacer la operación
 print(statistics.mean(salary_list))

 # Con numpy tarda mucho menos
 print(np.mean(salary_list))

 myarray = np.array([1,2,3,4])
 print(myarray.mean())

def media2():
 job_titles = np.array(["Data Analytics", "Data Scientist", "Data Engineer", "Machine Learning Engineer", "AI Engineer"])
 # No usar None porq da error por el tipo de variable, con np.nan devielve una variable vacía pero es un float asi q no dará problema
 base_salaries = np.array([60000, 80000, 75000, 90000, np.nan])
 bonus_rate = np.array([0.05, 0.1, 0.08, 0.12, np.nan])

 total_salary = base_salaries * (1 + bonus_rate)
 print(total_salary)
 print(np.nanmean(total_salary))

