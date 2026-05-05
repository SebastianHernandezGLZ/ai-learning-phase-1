# Week 02 - Day 01: Cleaner functions

import csv


def classify_customer(replied, requested_info, follow_up, days_without_reply):
    if not replied and days_without_reply >= 5:
        return "Needs follow-up"
    elif replied and requested_info and not follow_up and days_without_reply >= 5:
        return "Needs reminder"
    elif replied and requested_info and follow_up:
        return "Hot lead"
    elif replied and requested_info:
        return "Warm lead"
    elif replied:
        return "Interested lead"
    else:
        return "Cold lead"


def print_customer_result(name, status):
    print(f"{name}: {status}")


def get_customer_status(customer):
    return classify_customer(
        customer["replied"],
        customer["requested_info"],
        customer["follow_up"],
        customer["days_without_reply"]
    )


def convert_yes_no_to_bool(value):
    if value == "si":
        return True
    else:
        return False
    

def convert_row_to_customer(row):
    new_customer = {
        "name": row['nombre'],
        "age": int(row['edad']),
        "career_interest": row['carrera_interes'],
        "contact_channel": row['medio_contacto'],
        "replied": convert_yes_no_to_bool(row['respondio']),
        "requested_info": convert_yes_no_to_bool(row['pidio_info']),
        "follow_up": convert_yes_no_to_bool(row['seguimiento']),
        "days_without_reply": int(row['dias_sin_responder'])
    }

    return new_customer


def read_customers_from_csv(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        customers = []

        for row in reader:
            customer = convert_row_to_customer(row)
            customers.append(customer)
            
        return customers


def process_customers(customers):
    status_counts = {}
    
    for customer in customers:
        status = get_customer_status(customer)
        print_customer_result(customer['name'], status)
        status_counts[status] = status_counts.get(status, 0) + 1

    print_summary(status_counts, len(customers))


def print_summary(status_counts, total_customers):
    print("Summary:")
    print(f"Total customers: {total_customers}")
    
    for status, count in status_counts.items():
        print(f"{status}: {count}")
    

if __name__ == "__main__":
    customers = read_customers_from_csv("week-02-python-for-data/clientes.csv")
    process_customers(customers)