import json

comp = {}
p_count, p_sum = 0, 0
with open('t7.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        profit = float(data[2]) - float(data[3])
        comp.update({data[0]: profit})
        if profit > 0:
            p_count += 1
            p_sum += profit

average_profit = p_sum / p_count
result = [comp, {'average_profit': average_profit}]

with open("result.json", 'w') as file:
    json.dump(result, file)
