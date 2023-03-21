# FIDE ELO Calculator
This is a simple ELO calculator to calculate rating changes from FIDE rated games. 
It is based on the [FIDE ELO system](https://en.wikipedia.org/wiki/Elo_rating_system).
I wrote this program to help me calculate rating changes for my chess games.

The K-factor values used are 40 for players with less than 30 rated games, 20 for players more than 30 rated games, and 10 for players above 2400.

The GUI was written using TKinter. It takes the following inputs from the user:
- Player 1's rating
- Player 2's rating
- Player 1's result (did they win, draw or lose?)
- The total number of rated games player 1 has played (used to calculate the K-factor)

## Usage
To use the calculator, simply run the `Calculator GUI.py` file.

### Example

<img width="932" alt="Elo Calculator" src="https://user-images.githubusercontent.com/63872314/226641893-741dd8e9-7892-453d-86a9-6e2afc10151e.PNG">

## Requirements
- Python 3.6 or higher

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

