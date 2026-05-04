def classify_customer(replied, requested_info, follow_up):
    if replied and requested_info and follow_up:
        return "Hot lead"
    elif replied and requested_info:
        return "Warm lead"
    elif replied:
        return "Interested lead"
    else:
        return "Cold lead"


customer_name_1 = "Rafael"
customer_status_1 = classify_customer(True, True, False)

customer_name_2 = "Fernanda"
customer_status_2 = classify_customer(True, True, True)

customer_name_3 = "Enrique"
customer_status_3 = classify_customer(False, False, False)

customer_name_4 = "Paulina"
customer_status_4 = classify_customer(True, False, False)

print(f"{customer_name_1}: {customer_status_1}")
print(f"{customer_name_2}: {customer_status_2}")
print(f"{customer_name_3}: {customer_status_3}")
print(f"{customer_name_4}: {customer_status_4}")