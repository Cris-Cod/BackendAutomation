Feature: Verify if books are added and delete using Library API
  @library
  Scenario: Verify AddBook API functionality
    Given the book details which needs to be added to Library
    When we execute the Addbook PostAPI method
    Then book is successfully added

  @library
  Scenario Outline: Verify AddBook API functionality
    Given the book details which <isbn> and <aisle>
    When we execute the Addbook PostAPI method
    Then book is successfully added

    Examples:
      |  isbn  |  aisle |
      |  fdfee |  8974  |
      |  xcvbf |  1234  |
      |  uioo  |  0102  |