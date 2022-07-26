Feature: Order creation for block Volumes

  Scenario: Block Order page
    Given I go to the "https://dev.console.test.cloud.ibm.com"
      And I fill the email field with "salome.quispe+test12@mail.test.ibm.com"
      And I click on continue button
      And I enter "Test1301**++" data
      And I press login button
      And I click on navigation menu option
      And I hover mouse on classic Infrastructure
      And I go to block list page
      And I click on Order_Block_Storage button
      And I click on "US South" region
      And I select "Dallas" location
      And I click on "DAL10*" zone
      And I select "Hourly"  billing method
      And I fill the order size "200"
      And I select snapshot space "5 GB"
      And I select "Linux" OS type
      And I Select "2IOPS/GB" IOPS option
      And I checked I have read and agree to the terms and conditions checkbox
      And I click on create button
