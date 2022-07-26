# Created by salome.quispe at 4/26/2022
Feature: File block creation
  # Enter feature description here

  Scenario: File Order page creation
    # Enter steps here
   Given I go to the "https://dev.console.test.cloud.ibm.com"
      And I fill the email field with "salome.quispe+test12@mail.test.ibm.com"
      And I click on continue button
      And I enter "Test1301**++" data
      And I press login button
      And I click on navigation menu option
      And I hover mouse on classic Infrastructure
      And I go to File list page
      And I click on Order_File_Storage button
      And I click on "US South" region
      And I select "Dallas" location
      And I click on "DAL10*" zone
      And I select "Monthly"  billing method
      And I fill the order size "55"
      And I select snapshot space "5 GB"
      And I Select "10 IOPS/GB" IOPS option
      And I checked I have read and agree to the terms and conditions checkbox
      And I click on create button
      Then Successful modal shows