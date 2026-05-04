def classify_customer(replied, requested_info, follow_up):
    if replied and requested_info and follow_up:
        return "Hot lead"
    elif replied and requested_info:
        return "Warm lead"
    else: 
        return "Cold lead"
    
customer_status = classify_customer(True, True, False)
print(customer_status)
print(classify_customer(True, True, True))
print(classify_customer(True, False, False))
print(classify_customer(False, False, False))