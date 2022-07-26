# Created by salome.quispe at 5/3/2022
Feature: Portable Storage
  # Enter feature description here

  Scenario: Create a portable storage
    Given I go to the "https://dev.console.test.cloud.ibm.com"
      And I fill the email field with "salome.quispe+test005@mail.test.ibm.com"
      And I click on continue button
      And I enter "Test1301**++" data
      And I press login button
      And I click on navigation menu option
      And I hover mouse on classic Infrastructure
      And I go to block list page
      And I click on 'order portable storage' button
      And I click on "US South" region
      And I select "Dallas" location
      And I click on "DAL10*" zone
#      And I select region "US South"
#      And I select location "Dallas"
#      And I select zone "Dal10"
      And I fill Disk Description: "sq] Portable created" text
      And I Storage select Storage size : "10 GB (SAN)"
       And I checked I have read and agree to the terms and conditions checkbox
      And I click on create button