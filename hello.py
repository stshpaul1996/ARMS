from datetime import datetime, timedelta

# Sample data
doctors_data = {
    "Cardiology": {
        "Dr. Smith": {
            "Monday": ["9:00 AM - 1:00 PM"],
            "Tuesday": ["9:00 AM - 1:00 PM", "3:00 PM - 6:00 PM"],
            "Thursday": ["9:00 AM - 1:00 PM"]
        },
        "Dr. Johnson": {
            "Wednesday": ["10:00 AM - 2:00 PM"],
            "Friday": ["9:00 AM - 1:00 PM", "3:00 PM - 6:00 PM"]
        }
    },
    "Orthopedics": {
        "Dr. Williams": {
            "Tuesday": ["10:00 AM - 1:00 PM"],
            "Thursday": ["10:00 AM - 1:00 PM"]
        }
    }
}

def get_next_available_date():
    today = datetime.now()
    while True:
        today += timedelta(days=1)
        weekday = today.strftime("%A")
        if any(doctors_data.get(spec, {}).get(doc, {}).get(weekday) for spec in doctors_data for doc in doctors_data[spec]):
            return today

def find_doctors_availability(specialization, day):
    doctors_available = []
    for doctor, schedule in doctors_data.get(specialization, {}).items():
        timings = schedule.get(day)
        if timings:
            doctors_available.append((doctor, timings))
    return doctors_available

def generate_report(specialization, day):
    doctors_available = find_doctors_availability(specialization, day)
    if doctors_available:
        print(f"Doctors available for {specialization} on {day}:")
        for doctor, timings in doctors_available:
            print(f"{doctor}: {', '.join(timings)}")
    else:
        print(f"No doctors available for {specialization} on {day}.")
        next_available_date = get_next_available_date()
        print(f"Next available date is {next_available_date.strftime('%Y-%m-%d')}")

# Example usage
generate_report("Cardiology", "Wednesday")
