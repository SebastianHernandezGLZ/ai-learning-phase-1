# Día 5: Diccionarios aplicados a clientes


def classify_customer(replied, requested_info, follow_up):
    if replied and requested_info and follow_up:
        return "Hot lead"
    elif replied and requested_info:
        return "Warm lead"
    elif replied:
        return "Interested lead"
    else:
        return "Cold lead"

separator = "---------------------------------------------"
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
    }
]


hot_leads_count = 0
warm_leads_count = 0

for customer in customers:
    customer_status = classify_customer(
        customer["replied"],
        customer["requested_info"],
        customer["follow_up"]
    )

    print(f'''Cliente: {customer['name']}
Edad: {customer['age']}
Carrera de interés: {customer['career_interest']}
Medio de contacto: {customer['contact_channel']}
Lead score: {customer["lead_score"]}
Clasificación: {customer_status}
{separator}''')

    if customer_status == "Hot lead":
        hot_leads_count += 1
    elif customer_status == "Warm lead":
        warm_leads_count += 1 


print(f"Total de clientes revisados: {len(customers)}")
print(f"Total de Hot leads: {hot_leads_count}")
print(f"Total de Warm leads: {warm_leads_count}")