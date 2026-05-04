def classify_customer(replied, requested_info, follow_up):
    if replied and requested_info and follow_up:
        return "Hot client"
    elif replied and requested_info:
        return"Warm client"
    else: 
        return"Cold client"
    
customer_status = classify_customer(True, True, False)
print(customer_status)