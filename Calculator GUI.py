from tkinter import *
from tkinter import ttk, messagebox


class CalculatorGUI:
    """
    GUI for the ELO calculator.
    The calculator has fields for the player rating, opponent rating,
    actual score, and number of games played.
    The calculator will calculate the new rating for the player and display the rating change as well.
    """

    def __init__(self):
        self.root = Tk()
        self.root.title("ELO Calculator")
        self.root.iconbitmap("icon.ico")
        self.root.resizable(width=False, height=False)

        self.player_rating = StringVar()
        self.opponent_rating = StringVar()
        self.actual_score = StringVar()
        self.player_games_count = StringVar()
        self.new_rating = StringVar()
        self.rating_change = StringVar()

        # create gui widgets
        self.player_rating_label = Label(self.root, text="Player Rating:")
        self.player_rating_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.player_rating_entry = ttk.Entry(self.root, textvariable=self.player_rating)
        self.player_rating_entry.grid(row=0, column=1, padx=10, pady=10)

        self.opponent_rating_label = Label(self.root, text="Opponent Rating:")
        self.opponent_rating_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.opponent_rating_entry = ttk.Entry(self.root, textvariable=self.opponent_rating)
        self.opponent_rating_entry.grid(row=1, column=1, padx=10, pady=10)

        self.actual_score_label = Label(self.root, text="Actual Score:")
        self.actual_score_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.actual_score_radio = ttk.Radiobutton(self.root, text="Win", variable=self.actual_score, width=18, value=1)
        self.actual_score_radio.grid(row=2, column=1, padx=10, pady=10)

        self.actual_score_radio = ttk.Radiobutton(self.root, text="Draw", variable=self.actual_score, width=18,value=0.5)
        self.actual_score_radio.grid(row=3, column=1, padx=10, pady=10)

        self.actual_score_radio = ttk.Radiobutton(self.root, text="Loss", variable=self.actual_score, width=18, value=0)
        self.actual_score_radio.grid(row=4, column=1, padx=10, pady=10)

        self.player_games_count_label = Label(self.root, text="# of Player Games:")
        self.player_games_count_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        self.player_games_count_entry = ttk.Entry(self.root, textvariable=self.player_games_count)
        self.player_games_count_entry.grid(row=5, column=1, padx=10, pady=10)

        self.calculate_button = ttk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.new_rating_label = Label(self.root, text="New Rating:")
        self.new_rating_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)
        self.new_rating_entry = ttk.Label(self.root, textvariable=self.new_rating, width=18,
                                             background="dark blue", foreground="white", font="Calibre 10 bold")
        self.new_rating_entry.grid(row=7, column=1, padx=10, pady=10)

        self.rating_change_label = Label(self.root, text="Rating Change:")
        self.rating_change_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
        self.rating_change_entry = ttk.Label(self.root, textvariable=self.rating_change, width=18,
                                             background="grey", foreground="white", font="Calibre 10 bold")
        self.rating_change_entry.grid(row=8, column=1, padx=10, pady=10)

        # set default values
        self.player_games_count_entry.insert(END, "30")

        # set gui theme
        # self.style = ttk.Style()
        # self.style.theme_use("clam")

        self.root.mainloop()

    def expectedScore(self):
        # E = 1 / (1 + 10 ** ((Rb - Ra) / 400)) ref: https://en.wikipedia.org/wiki/Elo_rating_system
        return 1 / (1 + 10 ** ((int(self.opponent_rating.get()) - int(self.player_rating.get())) / 400))

    def playerKfactor(self):
        # ref: https://handbook.fide.com/chapter/B022017#:~:text=K%20is%20the,not%20exceed%20700
        if int(self.player_rating.get()) < 2400 and int(self.player_games_count.get()) < 30:
            return 40
        elif int(self.player_rating.get()) < 2400 and int(self.player_games_count.get()) >= 30:
            return 20
        return 10

    def newRating(self):
        # Rn = Ro + K(S - E) ref: https://en.wikipedia.org/wiki/Elo_rating_system
        return int(self.player_rating.get()) + self.playerKfactor() * (
                    float(self.actual_score.get()) - self.expectedScore())

    def calculate(self):
        """
        This function is called when the calculate button is pressed.
        It will calculate the new rating and rating change and display them.
        """
        try:
            # calculate new rating and rating change
            new_rating = self.newRating()
            rating_change = new_rating - int(self.player_rating.get())

            # round values to 2 decimal places and convert to string
            new_rating = str(round(self.newRating(), 2))
            rating_change = str(round(rating_change, 2))

            # display new rating and rating change
            # self.new_rating_entry.delete(0, END)
            # self.rating_change_entry.delete(0, END)
            self.new_rating.set(new_rating)
            self.rating_change.set(rating_change)
        except ValueError:
            # display error message if values are invalid
            messagebox.showinfo("Invalid Inputs", "One or more values entered are invalid.")


if __name__ == "__main__":
    EloCalculator = CalculatorGUI()
