from enum import Enum
from random import shuffle

class Playing_Card_Suit(Enum):
    """
    An enumeration representing the four suits of a standard deck of playing cards.

    Attributes:
        CLUBS (str): Represents the clubs suit.
        DIAMONDS (str): Represents the diamonds suit.
        HEARTS (str): Represents the hearts suit.
        SPADES (str): Represents the spades suit.
    """
    CLUBS    = "clubs"
    DIAMONDS = "diamonds"
    HEARTS   = "hearts"
    SPADES   = "spades"

    def is_red(self):
        """
        Determines if the card suit is red (Hearts or Diamonds).

        Returns:
            bool: True if the suit is red, False otherwise.
        """
        return self.value in ("hearts", "diamonds")

    def is_black(self):
        """
        Determines if the card suit is black (Clubs or Spades).

        Returns:
            bool: True if the suit is black, False otherwise.
        """
        return not self.is_red()

    def is_same_color(self, other):
        """
        Checks if this suit shares the same color as another suit.

        Args:
            other (Playing_Card_Suit): The other suit to compare against.

        Returns:
            bool: True if both suits are the same color, False otherwise.

        Raises:
            TypeError: If 'other' is not an instance of Playing_Card_Suit.
        """
        if isinstance(other, Playing_Card_Suit):
            return self.is_red() == other.is_red()
        raise TypeError("Ayusin mo. Hindi Playing_Card_Suit 'yung isa.")

    def __str__(self):
        """
        Returns the string representation of the suit value.

        Returns:
            str: The lower-case name of the suit.
        """
        return self.value

    def __repr__(self):
        """
        Returns a formal string representation of the suit object.

        Returns:
            str: A string prefixed with 'A Playing_Card_Suit: '.
        """
        return "A Playing_Card_Suit: " + self.value

    def rep_char(self):
        """
        Gets a single uppercase character representation of the suit.

        Returns:
            str: 'C', 'D', 'H', or 'S' depending on the suit.
        """
        return self.value[0].upper()

    def match_char(char):
        """
        Matches a string/character to its corresponding Playing_Card_Suit enum member.

        Args:
            char (str): A string whose first character indicates the suit.

        Returns:
            Playing_Card_Suit: The matched enum member, or None if no match is found.
        """
        if char[0].upper() == 'C':
            return Playing_Card_Suit.CLUBS
        if char[0].upper() == 'D':
            return Playing_Card_Suit.DIAMONDS
        if char[0].upper() == 'H':
            return Playing_Card_Suit.HEARTS
        if char[0].upper() == 'S':
            return Playing_Card_Suit.SPADES

class Playing_Card_Face(Enum):
    """
    An enumeration representing the face value of a playing card (Ace through King).

    Attributes:
        ACE to KING (int): Numerical rank representation from 1 to 13.
    """
    ACE   =  1 
    TWO   =  2
    THREE =  3
    FOUR  =  4
    FIVE  =  5
    SIX   =  6
    SEVEN =  7
    EIGHT =  8
    NINE  =  9
    TEN   = 10
    JACK  = 11
    QUEEN = 12
    KING  = 13

    def __str__(self):
        """
        Returns the string representation of the numerical value.

        Returns:
            str: The string version of the integer rank.
        """
        return str(self.value)

    def __repr__(self):
        """
        Returns the word representation of the face value.

        Returns:
            str: The lower-case word representation (e.g., 'ace').
        """
        return self.rep_word()

    def rep_word(self):
        """
        Retrieves the lowercase word corresponding to the card face.

        Returns:
            str: The name of the card face rank.
        """
        words = ("ace", "two", "three",
                 "four", "five", "six",
                 "seven", "eight", "nine", "ten",
                 "jack", "queen", "king")
        return words[self.value - 1]

    def rep_char(self):
        """
        Retrieves a short, single-character string representation for the card face.

        Returns:
            str: 'A', 'T', 'J', 'Q', 'K' for special faces, or digits '2'-'9' for others.
        """
        if 1 < self.value < 10:
            return str(self.value)
        if self.value == Playing_Card_Face.ACE.value:
            return 'A'
        if self.value == Playing_Card_Face.TEN.value:
            return 'T'
        if self.value == Playing_Card_Face.JACK.value:
            return 'J'
        if self.value == Playing_Card_Face.QUEEN.value:
            return 'Q'
        if self.value == Playing_Card_Face.KING.value:
            return 'K'

    def match_value(value):
        """
        Matches an integer value to its corresponding Playing_Card_Face enum member.

        Args:
            value (int): Numerical rank value (1-13).

        Returns:
            Playing_Card_Face: The matching enum member, or None if unmatched.
        """
        for face in Playing_Card_Face:
            if face.value == value:
                return face

class Playing_Card:
  """
  Represents an individual playing card with a specific suit and face value.
  
  Attributes:
      __suit (Playing_Card_Suit): Private attribute holding the suit of the card.
      __face (Playing_Card_Face): Private attribute holding the face value of the card.
  """
  def __init__(self,
               suit = Playing_Card_Suit.CLUBS,
               face = Playing_Card_Face.ACE):
    """
    Constructs a Playing_Card object using either enum instances, characters, or integers.

    Args:
        suit (Playing_Card_Suit or str, optional): The suit. Defaults to Playing_Card_Suit.CLUBS.
        face (Playing_Card_Face or int, optional): The face value. Defaults to Playing_Card_Face.ACE.

    Raises:
        TypeError: If the 'suit' type or 'face' type cannot be parsed.
    """
    if suit:
      if type(suit) == Playing_Card_Suit:
        self.__suit = suit
      elif type(suit) == str:
        self.__suit = Playing_Card_Suit.match_char(suit)
      else:
        raise TypeError("An unrecognized type is given for the suit.")
    if face:
      if type(face) == Playing_Card_Face:
        self.__face = face
      elif type(face) == int:
        self.__face = Playing_Card_Face.match_value(face)
      else:
        raise TypeError("An unrecognized type is given for the face.")

  def get_suit(self):
    """
    Accessor method for the card's suit.

    Returns:
        Playing_Card_Suit: The suit of the card.
    """
    return self.__suit

  def get_face(self):
    """
    Accessor method for the card's face value.

    Returns:
        Playing_Card_Face: The face value of the card.
    """
    return self.__face

  def __str__(self):
    """
    Returns a human-readable description of the card.

    Returns:
        str: Format like 'ace of clubs'.
    """
    return self.__face.rep_word() + " of " + str(self.__suit)

  def __repr__(self):
    """
    Returns a compact two-character string shorthand of the card.

    Returns:
        str: Combined short character representations of the face and suit (e.g., 'AH').
    """
    return self.__face.rep_char() + self.__suit.rep_char()

  def is_same_color(self, other):
    """
    Checks if this card has the same color as another card.

    Args:
        other (Playing_Card): The card to compare colors with.

    Returns:
        bool: True if colors match, False otherwise.

    Raises:
        TypeError: If 'other' is not an instance of Playing_Card.
    """
    if isinstance(other, Playing_Card):
      return self.get_suit().is_same_color(other.get_suit())
    raise TypeError('Comparing Playing_Card with another type.')

  def __eq__(self, other):
    """
    Evaluates equality based on the face value of the cards.

    Args:
        other (Playing_Card): The card to compare against.

    Returns:
        bool: True if both cards have the same face value value.

    Raises:
        TypeError: If 'other' is not an instance of Playing_Card.
    """
    if isinstance(other, Playing_Card):
      return self.__face.value == other.__face.value
    raise TypeError('Comparing Playing_Card with another type.')
    
  def __lt__(self, other):
    """
    Evaluates if this card's face value is less than another card's.

    Args:
        other (Playing_Card): The card to compare against.

    Returns:
        bool: True if this card's value is lower.

    Raises:
        TypeError: If 'other' is not an instance of Playing_Card.
    """
    if isinstance(other, Playing_Card):
      return self.__face.value < other.__face.value
    raise TypeError('Comparing Playing_Card with another type.')

  def __gt__(self, other):
    """
    Evaluates if this card's face value is greater than another card's.

    Args:
        other (Playing_Card): The card to compare against.

    Returns:
        bool: True if this card's value is higher.

    Raises:
        TypeError: If 'other' is not an instance of Playing_Card.
    """
    if isinstance(other, Playing_Card):
      return self.__face.value > other.__face.value
    raise TypeError('Comparing Playing_Card with another type.')

class Playing_Card_Deck:
  """
  Represents a standard deck containing 52 unique Playing_Card objects.

  Attributes:
      __deck (list): Private list storing the Playing_Card objects currently in the deck.
  """
  def __init__(self):
    """
    Initializes the deck by generating all 52 combinations of suits and face values.
    """
    self.__deck = []
    for suit in Playing_Card_Suit:
      for face in Playing_Card_Face:
        self.__deck.append(Playing_Card(suit, face))

  def __repr__(self):
    """
    Delegates to the __str__ presentation logic for the object representation.

    Returns:
        str: Grid layout string of the deck contents.
    """
    return str(self)

  def __str__(self):
    """
    Returns a formatted grid string representation of cards currently in the deck.

    Returns:
        str: Shorthand representations of cards arranged in rows of 13.
    """
    to_return = ""
    counter = 0
    for card in self.__deck:
        if counter == 12:
          to_return += repr(card) + " " + '\n'
          counter = 0
        else:
          to_return += repr(card) + " "
          counter += 1
    return to_return

  def __len__(self):
    """
    Calculates the number of cards remaining in the deck.

    Returns:
        int: Total card count.
    """
    return len(self.__deck)

  def shuffle(self):
    """
    Shuffles the deck randomly in place.
    """
    shuffle(self.__deck)

  def is_empty(self):
    """
    Checks if the deck contains no more cards.

    Returns:
        bool: True if the deck has 0 cards, False otherwise.
    """
    return len(self) == 0

  def deal(self):
    """
    Removes and returns the top card from the deck.

    Returns:
        Playing_Card: The dealt card.

    Raises:
        ValueError: If attempting to deal from an empty deck.
    """
    if self.is_empty():
      raise ValueError("Wala nang cards!")
    return self.__deck.pop(0)
"""
# Instantiate variables
card = Playing_Card('H', 2)
card2 = Playing_Card('S', 4)
card3 = Playing_Card('D', 11)
card4 = Playing_Card('C', 4)
pcd = Playing_Card_Deck()"""