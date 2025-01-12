import pandas as pd

#Zadanie 8:
#a) wczytaj z niego arkusz 'employee_details' do ramki danych emp_det, zaś arkusz 'performance' do
#ramki danych emp_perf,
emp_det = pd.read_excel('employee.xlsx', sheet_name = 'employee_details')
emp_per = pd.read_excel('employee.xlsx', sheet_name = 'performance')

#b) przekształć w tych ramkach danych kolumnę 'name' na indeks,
emp_det.set_index('name', inplace=True)
emp_per.set_index('name', inplace=True)

#c) połącz je kolumna po kolumnie do ramki danych o nazwie employees
employees = pd.concat([emp_det, emp_per], axis='columns')

#d) zameń nazwy kolumn tak, by zaczynały się od wielkiej litery
employees.columns = employees.columns.str.capitalize()

#e) wyświetl informacje o zmodyfikowanej ramce danych i jej strukturze oraz jej zawartość.
employees.info()
print(employees)

#Zadanie 9:
#a) utwórz z niej ramkę danych o nazwie emp_finance, wybierając pracowników działu finasowego,
#zarabiających powyżej 20000,
emp_finance = employees[(employees['Department'] == 'Finance') & (employees['Income'] > 20000)]
print(emp_finance)

#b) zapisz ramkę danych emp_finance do skoroszytu MS Excel o nazwie 'emp_finance.xlsx', umiesz?
#czając dane w arkuszu o nazwie 'employee_finance'.
emp_finance.to_excel('emp_finance.xlsx', sheet_name='employee_finance', index=False)