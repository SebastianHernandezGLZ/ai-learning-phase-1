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


def read_customers_from_csv(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['nombre']} - {row['edad']} - {row['carrera_interes']} - {row['medio_contacto']} - {row['respondio']} - {row['pidio_info']} - {row['seguimiento']} - {row['dias_sin_responder']}")

    

if __name__ == "__main__":
    read_customers_from_csv("week-02-python-for-data/clientes.csv")