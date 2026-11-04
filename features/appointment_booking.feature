
Feature: Council Appointment Booking
  As a local resident
  I want to book an appointment with the council
  So that I can access council services efficiently

  Scenario: Successfully book a council appointment
    Given a resident named "John Smith"
    And the resident selects the service "Housing Support"
    And the resident selects a valid future date
    When the resident submits the appointment request
    Then the appointment should be confirmed


  Scenario: Reject an appointment with an empty resident name
    Given a resident named ""
    And the resident selects the service "Housing Support"
    And the resident selects a valid future date
    When the resident submits the appointment request
    Then the appointment should be rejected with "Error: Invalid resident name"


  Scenario: Reject an appointment with a past date
    Given a resident named "John Smith"
    And the resident selects the service "Council Tax"
    And the resident selects a past date
    When the resident submits the appointment request
    Then the appointment should be rejected with "Error: Appointment date must be in the future"
