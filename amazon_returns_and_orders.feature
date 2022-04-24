# Created by Kate at 4/24/2022
Feature: TESTS FOR AMAZON "RETURNS AND ORDERS"

  Scenario: Logged out User sees Sign in page when clicking "Returns and Orders"
    Given Open Amazon page
    When  Verify Amazon page is opened
    When Click on Returns and Orders
    Then Verify Sign in page is opened
