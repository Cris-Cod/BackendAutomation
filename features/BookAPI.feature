Feature: Verify if books are added and delete using Library API

  Scenario: Verify AddBook API functionality
    Given the book details which needs to be added to Library
    When we execute the Addbook PostAPI method
    Then book is successfully added