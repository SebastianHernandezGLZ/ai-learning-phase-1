# Week 02 - Day 01: Cleaner functions


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


customers = [
    {
        "name": "Ana",
        "replied": True,
        "requested_info": True,
        "follow_up": True,
        "days_without_reply": 1
    },
    {
        "name": "Luis",
        "replied": False,
        "requested_info": False,
        "follow_up": False,
        "days_without_reply": 7
    },
    {
        "name": "Marta",
        "replied": True,
        "requested_info": True,
        "follow_up": False,
        "days_without_reply": 3
    },
    {
        "name": "Carlos",
        "replied": True,
        "requested_info": False,
        "follow_up": False,
        "days_without_reply": 5
    },
    {
        "name": "Sofía",
        "replied": False,
        "requested_info": False,
        "follow_up": False,
        "days_without_reply": 2
    },
    {
        "name": "Pedro",
        "replied": True,
        "requested_info": True,
        "follow_up": False,
        "days_without_reply": 5
    }
]



if __name__ == "__main__":
    for customer in customers:
        status = get_customer_status(customer)
        print_customer_result(customer["name"], status)