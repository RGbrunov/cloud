# Created by Mariela.Sejas at 3/1/2022
Feature: Login to SRR page
  # Enter feature description here

  Scenario: Login to SRR page with valid parameter
    Given I go to the "http://stable.internal.qadal1301.softlayer.local/FileBlock/newStaas2Cluster"
      And I enter Username with "msagreda"
      And I click on login button
      Then User must successfully login
