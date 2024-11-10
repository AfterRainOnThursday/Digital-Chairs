import json
# TODO решите задачу
def task() -> float:
    total = 0
    score_value = 0
    weight_value = 0

    with open("input.json", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "score" in line:
                score_value = float(line.split(":")[1].strip().strip(","))
            elif "weight" in line:
                weight_value = float(line.split(":")[1].strip().strip(","))

            if score_value != 0 and weight_value != 0:
                total += score_value * weight_value
                score_value, weight_value = 0, 0

    return round(total, 3)

print(task())
