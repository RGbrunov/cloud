# Created by Mariela.Sejas at 3/1/2022
Feature: Login to SRR page
  # Enter feature description here

  Scenario: Login to SRR page with valid parameter
    Given I go to the url
      When I enter Username
      Then I click on Login button
      And I need to see the text with "Volumes" on FileBlock page