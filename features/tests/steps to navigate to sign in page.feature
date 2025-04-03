# Created by Marlon at 4/1/2025
Feature: User navigation to Sign In page

  Scenario: Logged out user navigates to Sign In page
    Given Open target.com
    When Click Sign In
    Then Verify Sign In form opened

