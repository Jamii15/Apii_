import requests

# Hacer la solicitud a la API
url = "https://dummy.restapiexample.com/api/v1/employees"
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()

    # Obtener la cantidad de empleados
    num_employees = len(data["data"])

    # Calcular el promedio de salario
    salaries = [float(employee["employee_salary"]) for employee in data["data"]]
    average_salary = sum(salaries) / num_employees

    # Calcular el promedio de edad
    ages = [int(employee["employee_age"]) for employee in data["data"]]
    average_age = sum(ages) / num_employees

    # Obtener salario mínimo y máximo
    min_salary = min(salaries)
    max_salary = max(salaries)

    # Obtener la edad menor y mayor
    min_age = min(ages)
    max_age = max(ages)

    # Imprimir los resultados
    print(f"Total de empleados: {num_employees}")
    print(f"Promedio de salario: {average_salary}")
    print(f"Promedio de edad: {average_age}")
    print(f"Salario mínimo: {min_salary}")
    print(f"Salario máximo: {max_salary}")
    print(f"Edad menor: {min_age}")
    print(f"Edad mayor: {max_age}")

# Si la solicitud no fue exitosa, imprimir el código de estado
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
