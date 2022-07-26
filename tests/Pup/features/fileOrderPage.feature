# Created by salome.quispe at 4/28/2022
Feature: Order File page
  # Enter feature description here

  Scenario: Review the Regions options shows
  Given I go to the "https://dev.console.test.cloud.ibm.com"
      And I fill the email field with "salome.quispe+test005@mail.test.ibm.com"
      And I click on continue button
      And I enter "Test1301**++" data
      And I press login button
      And I click on navigation menu option
      And I hover mouse on classic Infrastructure
      And I go to File list page
      And I click on Order_File_Storage button
      And I go to region section
      Then seven regions shows
    # Enter steps here
  Scenario: Review the create button disabled
  Given I go to the "https://dev.console.test.cloud.ibm.com"
      And I fill the email field with "salome.quispe+test005@mail.test.ibm.com"
      And I click on continue button
      And I enter "Test1301**++" data
      And I press login button
      And I click on navigation menu option
      And I hover mouse on classic Infrastructure
      And I go to File list page
      And I click on Order_File_Storage button
      And I go to region section
      Then seven regions shows