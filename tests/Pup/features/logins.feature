Feature: Login feature scenarios

  Scenario: Basic login validation
    Given I go to the "https://dev.console.test.cloud.ibm.com"
      And I fill the email field with "salome.quispe+test005@mail.test.ibm.com"
      And I click on continue button
      And I enter "Test1301**++" data
      And I press login button
      And I click on navigation menu option
      And I hover mouse on classic Infrastructure

