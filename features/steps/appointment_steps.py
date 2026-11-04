
from behave import given, when, then
from datetime import date, timedelta



@given('a resident named "{name}"')
def step_resident_name(context, name):
    context.resident_name = name


@given('a resident named ""')
def step_empty_resident_name(context):
    context.resident_name = ""



@given('the resident selects the service "{service}"')
def step_select_service(context, service):
    context.service = service


@given('the resident selects a valid future date')
def step_select_date(context):
    context.appointment_date = date.today() + timedelta(days=1)


@given('the resident selects a past date')
def step_select_past_date(context):
    context.appointment_date = date.today() - timedelta(days=1)


@when('the resident submits the appointment request')
def step_submit_appointment(context):
    from app import book_appointment

    context.result = book_appointment(
        context.resident_name,
        context.service,
        context.appointment_date
    )


@then('the appointment should be confirmed')
def step_appointment_confirmed(context):
    assert context.result == "Appointment confirmed"

@then('the appointment should be rejected with "{error_message}"')
def step_appointment_rejected(context, error_message):
    assert context.result == error_message, (
        f"Expected: {error_message}, "
        f"but received: {context.result}"
    )
