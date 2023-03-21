# calculate the expected score for each player
def expectedScore(playerRating, opponentRating):
    # E = 1 / (1 + 10 ** ((Rb - Ra) / 400)) ref: https://en.wikipedia.org/wiki/Elo_rating_system
    return 1 / (1 + 10 ** ((opponentRating - playerRating) / 400))


# calculate the new rating for each player
def newRating(expectedScore, actualScore, playerRating, Kfactor):
    # Rn = Ro + K(S - E) ref: https://en.wikipedia.org/wiki/Elo_rating_system
    return playerRating + Kfactor * (actualScore - expectedScore)


def playerKfactor(playerRating, totalGamesPlayed=30):
    # ref: https://handbook.fide.com/chapter/B022017#:~:text=K%20is%20the,not%20exceed%20700
    if playerRating < 2400 and totalGamesPlayed < 30:
        return 40
    elif playerRating < 2400 and totalGamesPlayed >= 30:
        return 20
    return 10


def main():
    # get the players ratings
    playerRating = int(input("Enter the player rating: "))
    opponentRating = int(input("Enter the opponent rating: "))

    # get the actual score
    actualScore = float(input("Enter the actual score (1 for win, 0.5 for draw, 0 for loss): "))

    # get the number of games played by the player
    playerGamesCount = int(input("Enter the number of games played by the player: "))

    # calculate the expected score
    Es = expectedScore(playerRating, opponentRating)

    # calculate the new rating
    kFactor = playerKfactor(playerRating, playerGamesCount)
    nR = newRating(Es, actualScore, playerRating, kFactor)

    # print the new rating
    print("The new rating is: ", round(nR, 2))


if __name__ == "__main__":
    main()
