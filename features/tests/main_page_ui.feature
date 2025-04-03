# Created by Marlon at 4/3/2025
Feature: Main page UI test
  # Enter feature description here

  Scenario: Verify header links has at least 1 link
    Given Open target main page
    Then Verify at least 1 link shown


  Scenario: Verify all header links shown
    Given Open target main page
    Then Verify 6 links shown
    # Enter steps here