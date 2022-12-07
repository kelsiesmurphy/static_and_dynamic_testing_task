### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      # to check equality, a double equals sign must be used (==) instead of the single equal sign used above.
      return True
    else
    # there is a missing colon following the else statement.
      return False
   

  dif highest_card(self, card1 card2):
  # there is a typo when defining the function, where it should be 'def' instead of 'dif'
  # There is a comma missing after the second argument (card1) in the above function.
  if card1.value > card2.value:
  # This if statement should be indented below the highest card function, it is currently outside the function.
    return card
  # There is no card instance to return, it should be card1 in this case.
  else:
    return card2
  

# The cards_total function below should be indented one level so that it is under the class CardGame, as right now it is outwith the class.
def cards_total(self, cards):
  total
  # The total variable above is not being assigned to anything, it should be something like 'total = 0'.
  for card in cards:
    total += card.value
    # The return statement should be outside the for loop.
    # The total is in an 'int' format and cannot concatenate with a str, so it must be coerced appropriately. 
  return "You have a total of" + str(total)
  
```
