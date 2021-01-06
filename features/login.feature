
Feature: Login

  Scenario: Login successfully
Given the user accesses the Fábrica de Sinais platform
When the user authenticates with valid credentials
Then the platform returns a welcome message to the user.