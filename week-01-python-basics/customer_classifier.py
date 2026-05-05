# Día 4: Listas y ciclos aplicados a clientes


def classify_customer(replied, requested_info, follow_up):
    if replied and requested_info and follow_up:
        return "Hot lead"
    elif replied and requested_info:
        return "Warm lead"
    elif replied:
        return "Interested lead"
    else:
        return "Cold lead"


customer_names = ["Rafael", "Fernanda", "Enrique", "Paulina", "Daniel"]

replied_values = [True, True, False, True, True]
requested_info_values = [True, True, False, False, False]
follow_up_values = [False, True, False, False, True]

hot_leads_count = 0

for i in range(len(customer_names)):
    customer_status = classify_customer(
        replied_values[i],
        requested_info_values[i],
        follow_up_values[i]
    )

    print(f"{customer_names[i]}: {customer_status}")

    if customer_status == "Hot lead":
        hot_leads_count = hot_leads_count + 1

print(f"Total de clientes revisados: {len(customer_names)}")
print(f"Total de Hot leads: {hot_leads_count}")