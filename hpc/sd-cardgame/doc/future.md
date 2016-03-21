### Future

* There is scope to add a name field, where the bot and player can have names
While not crucial to the game, having the player's name in the game adds a personal element to the game, 
that the user is a player of the game, not just a "Player".

* An early mockup of a graphical user interface was created using Qt4. This could be very doable given the
current code.
Graphical user interfaces are naturally a good option to have for a game. This would give a more 
accurate representation of that the game's design attempts to achieve. It also adds a more intuitive method
of user interaction with the game. It also may add an artistic element to the game, rather than simply
hacking code that runs a CLI game.

* The bot class was made in a hurry. Some of the functions may be migrated to it from the Game class
To improve code quality and encapsulate the Bot class would increase the reusability
of that piece of code. Some functions had been created but not yet filled in due to 
time constraints.

* The main game and bot functions in Game() are too long and complex. They could be refatored.
As mentioned in the previous point, these two functions are at the moment not trivial to
write tests for. Some work could be done to make this code better.

* Possibility of adding a coin toss before the game starts to determine starting player
This would be useful in order to increase the difficulty of the game. Since the human player
attacks first, it is trivial to achieve a victory.

