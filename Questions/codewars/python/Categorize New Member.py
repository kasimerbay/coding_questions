def open_or_senior(data):
    result = []
    status = "Open"
    
    for i in data:
        if i[0] >=55 and i[1] >=7:
            status = "Senior"
        else: status = "Open"
        result.append(status)
    return result

test_cases = [
    
    [(45, 12),(55,21),(19, -2),(104, 20)],
    
    [(16, 23),(73,1),(56, 20),(1, -1)]
    
    ]

for data in test_cases:
    print(open_or_senior(data))