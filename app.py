
from datetime import date


def book_appointment(resident_name, service, appointment_date):
    """
    Book an appointment for a local council service.
    """

    available_services = [
        "Housing Support",
        "Council Tax",
        "Resident Support"
    ]

    # Validate resident name
    if not isinstance(resident_name, str) or not resident_name.strip():
        return "Error: Invalid resident name"

    # Validate selected service
    if service not in available_services:
        return "Error: Invalid council service"

    # Validate appointment date
    if not isinstance(appointment_date, date):
        return "Error: Invalid appointment date"

    if appointment_date <= date.today():
        return "Error: Appointment date must be in the future"

    return "Appointment confirmed"
