# Created by Marlon at 3/31/2025
Feature: Target search test cases

  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results


  Scenario Outline: User can search for a product on target
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search results <expected_text>
    Examples:
    |search_word  |expected_text  |
    |tea          |tea            |
    |iphone       |iphone         |
    |dress        |dress          |

Feature: Verify target Circle benefits

  Scenario: Check number of benefit cells
    Given Open the Target Circle page
    When Count the benefit cells
    Then There should be 10 benefit cells


  Scenario: Add a product to the shopping cart
    Given Open the Target website
    When Search for a product
    And Add the product to the cart
    Then The cart should contain the product