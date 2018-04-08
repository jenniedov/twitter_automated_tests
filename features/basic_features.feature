Feature: Basic features

  Scenario: Basic login , post tweet and delete it.
    Given I'm logged in with main_user
     When I post a tweet with the text "My hovercraft is full of eels."
     Then I wait for it to appear on my dashboard
     When I delete the tweet with the same text
     Then It is no longer visible

  Scenario: Hide tweet
    Given I'm logged in with main_user
     When I hide the first tweet I see
     Then It is no longer visible

  Scenario: Basic search
    Given I'm logged in with main_user
     When I search for "Kate Falanga"
      And I click on the People tab
     Then I see the user in the results

  Scenario: Type more characters then allowed
    Given I'm logged in with main_user
     When I type a tweet with 279 characters
     Then I can post it
     When I type a tweet with 281 characters
     Then I can't post it

    Scenario: Type in Hebrew
    Given I'm logged in with main_user
     When I post a tweet with the text "זרעי קיץ נישאים ברוח"
     Then I wait for it to appear on my dashboard
     When I delete the tweet with the same text
     Then It is no longer visible
