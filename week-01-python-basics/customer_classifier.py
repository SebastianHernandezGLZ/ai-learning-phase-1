# Week 01: Customer Classifier
# Basic Python project using variables, conditionals, lists, dictionaries, loops, and functions.


def classify_customer(replied, requested_info, follow_up):
    if replied and requested_info and follow_up:
        return "Hot lead"
    elif replied and requested_info:
        return "Warm lead"
    elif replied:
        return "Interested lead"
    else:
        return "Cold lead"


def print_customer_summary(customer, customer_status):
    print(f'''Cliente: {customer['name']}
Edad: {customer['age']}
Carrera de interés: {customer['career_interest']}
Medio de contacto: {customer['contact_channel']}
Lead score: {customer["lead_score"]}
Clasificación: {customer_status}
-----------------------------------------------''')


def print_summary_totals(total_customers, hot_count, warm_count, interested_count, cold_count):
    print(f"Total de clientes revisados: {total_customers}")
    print(f"Total de Hot leads: {hot_count}")
    print(f"Total de Warm leads: {warm_count}")
    print(f"Total de Interested leads: {interested_count}")
    print(f"Total de Cold leads: {cold_count}")


def process_customers(customers):
    hot_leads_count = 0
    warm_leads_count = 0
    interested_leads_count = 0
    cold_leads_count = 0

    for customer in customers:
        customer_status = classify_customer(
            customer["replied"],
            customer["requested_info"],
            customer["follow_up"]
        )

        print_customer_summary(customer, customer_status)

        if customer_status == "Hot lead":
            hot_leads_count += 1
        elif customer_status == "Warm lead":
            warm_leads_count += 1
        elif customer_status == "Interested lead":
            interested_leads_count += 1
        elif customer_status == "Cold lead":
            cold_leads_count += 1

    print_summary_totals(
        len(customers),
        hot_leads_count,
        warm_leads_count,
        interested_leads_count,
        cold_leads_count
    )


customers = [
    {
        "name": "Rafael",
        "age": 21,
        "career_interest": "Inteligencia Artificial",
        "contact_channel": "WhatsApp",
        "replied": True,
        "requested_info": True,
        "follow_up": False,
        "lead_score": 70
    },
    {
        "name": "Fernanda",
        "age": 19,
        "career_interest": "Psicología",
        "contact_channel": "Instagram",
        "replied": True,
        "requested_info": True,
        "follow_up": True,
        "lead_score": 95
    },
    {
        "name": "Enrique",
        "age": 23,
        "career_interest": "Derecho",
        "contact_channel": "Facebook",
        "replied": False,
        "requested_info": False,
        "follow_up": False,
        "lead_score": 10
    },
    {
        "name": "Paulina",
        "age": 20,
        "career_interest": "Administración",
        "contact_channel": "WhatsApp",
        "replied": True,
        "requested_info": False,
        "follow_up": False,
        "lead_score": 45
    },
    {
        "name": "Daniel",
        "age": 22,
        "career_interest": "Mercadotecnia",
        "contact_channel": "Instagram",
        "replied": True,
        "requested_info": False,
        "follow_up": True,
        "lead_score": 50
    },
    {
        "name": "Sofía",
        "age": 18,
        "career_interest": "Medicina",
        "contact_channel": "Facebook",
        "replied": False,
        "requested_info": True,
        "follow_up": False,
        "lead_score": 25
    }
]


if __name__ == "__main__":
    process_customers(customers)