# Changes
## I/O
The input files are useful to the code since now
cards may easily be added to the file to increase
card variety.

The text strings are now imported from a file as well.
This is of benefit to the program since it would simplify
the process of editing the text strings. This also accommodates
for localisation of the test strings. This is done by simply
translating the strings in the file and changing the string
input file in the Python scripts.

* Created a json file to load cards from as dicts
* Created a json file to load game text strings

## Code
The code is now written with an actual object-oriented design.
This was primarily used as an exercise for the developer to
concretely familiarise with the concepts of the paradigm, but
also this is a way of making the code significantly easier to
test since most of the functions are quite short.

* Created a Card class to read card attributes from
* Created a Pile class which is used to manipulate decks
* Created a Player class which is used to manipulate players
* Created a Game class which contains the rules and moves
* Created a Data class for extracting resource files
* Created a Board class for managing the central line
* Increased game risk by randomising central deck cards

## Interface
In the original version of the code, the interface was difficult to
understand since there was a lot of text. This was cleaned up by
clearing the screen for each move. This makes the game significantly
easier to understand for the player. I allowed the code to be tested
by users who had not played before and they had found this design 
intuitive and simple to understand.

* Game options no longer case sensitive
* Screen is now cleared after every action - cleaner interface 
* Catch implemented for input. Game won't break when user messes up input
* Bot actions are now delayed to simulate how playing against an opponent would be

