def power_report(raw_data,threshold_str):
    cleaned=" ".join(raw_data.strip().split())
    data={}
    entries=cleaned.split("|")
    for entry in entries:
        appliance, kwh = entry.split(":")
        appliance = appliance.strip()
        kwh = float(kwh.strip())
        data[appliance] = kwh
    count = len(data)
    total = sum(data.values())
    average = round(total / count, 1)
    items = list(data.items())
    highest_appliance, highest_value = items[0]
    lowest_appliance, lowest_value = items[0]

    for appliance, value in items[1:]:
        if value > highest_value:
            highest_appliance, highest_value = appliance, value
        if value < lowest_value:
            lowest_appliance, lowest_value = appliance, value

    highest = f"{highest_appliance} ({highest_value} kWh)"
    lowest = f"{lowest_appliance} ({lowest_value} kWh)"
    threshold = float(threshold_str)
    above_threshold = 0
    for value in data.values():
        if value >= threshold:
            above_threshold += 1
    ranked = []
    for appliance, kwh in data.items():
        ranked.append((kwh, appliance))
    ranked.sort(reverse=True)

    ranking_parts = []
    i = 1
    for kwh, appliance in ranked:
        ranking_parts.append(f"{i}. {appliance} ({kwh})")
        i += 1

    ranking = ", ".join(ranking_parts)
    return {
        "appliances": count,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "above_30kwh": above_threshold,
        "ranking": ranking
    }
result = power_report(
    "  Fridge: 45.2  |  Washer: 22.8  |  AC: 88.4  |  Lighting: 18.5  |  TV: 31.6  ",
    "30.0"
)
print(result)
