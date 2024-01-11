from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        file = open("data.txt", mode="r")
        self.high_score = file.read()
        file.close()
        self.pu()
        self.goto(0, 250)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 16, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", move=False, align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
            file = open("data.txt", mode="w")
            file.write(self.high_score)
            file.close()
        self.score = 0
        self.update_scoreboard()
