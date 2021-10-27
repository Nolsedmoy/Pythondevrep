with open('from_task_3') as file:
    file_lines = file.readlines()
    employes = {}
    sum_salary = 0
    for line in file_lines:
        emp_info = line.split()
        employes.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
    average_sal = sum_salary / len(employes)
    print(f'Average = {average_sal}')

    for k, v in employes.items():
        if v < 20000:
            print(f'{k}: {v}')

