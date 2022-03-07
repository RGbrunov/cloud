# Created by Mariela.Sejas at 3/1/2022
Feature: Create SRR for Classic Storage
  # Enter feature description here

  Scenario Outline: Create Staas v2 SRR
    Given I go to "http://stable.internal.qadal1301.softlayer.local/FileBlock/newStaas2Cluster"
      And I enter Username with "msagreda"
      And I click on login button
      And I select block protocol type
      And I enter cluster name with "<clusterName>", Management IP Address "<ipAddress>", Encryption key "<key>"
      And I click on Preview SRR button
      And I click on Create SRR button

      Examples:
      |clusterName   | ipAddress                | key
      |testMS        | 172.18.107.190           | xxxxx

