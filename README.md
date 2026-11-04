
# Council Appointment Booking System

## SWE6301 - Agile Programming

A Python-based prototype developed for the SWE6301
Agile Programming assessment.

## Project Description

The application allows residents to request appointments
for local council services.

## Features

- Book a council appointment
- Validate resident names
- Validate council services
- Reject appointments with past dates
- Confirm valid appointments

## Technologies

- Python 3.14
- Behave 1.3.3
- Behaviour-Driven Development (BDD)
- Gherkin
- Git and GitHub

## Running the Tests

Install dependencies:

python -m pip install -r requirements.txt

Run BDD tests:

python -m behave

## BDD Scenarios

1. Successful appointment booking
2. Reject an empty resident name
3. Reject a past appointment date
