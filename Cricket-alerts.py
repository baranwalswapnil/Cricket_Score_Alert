# ==== Importing all the necessary libraries
from tkinter import *
from PIL import ImageTk
from tkinter.ttk import Combobox
from bs4 import BeautifulSoup
import requests


# ==== creating main class
class CricketScore:

    # ==== creating gui window
    def __init__(self, root):
        self.root = root
        self.root.title("LIVE CRICKET SCORE")
        self.root.geometry('800x500')
        self.bg = ImageTk.PhotoImage(file="background_image.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)

        # adding live matches text to gui
        self.label = Label(self.root, text='Live Matches', font=("times new roman", 60), compound='center').pack(padx=100, pady=50)

        # ==== adding all live matches combobox in gui
        self.var = StringVar()
        self.matches = self.match_details()
        self.data = [i for i in self.matches.keys()]
        self.cb = Combobox(self.root, values=self.data, width=50)
        self.cb.place(x=250,y=200)

        # ==== adding check score button to gui
        self.b1 = Button(self.root, text="Check Score", font=("times new roman", 15), command=self.show_match_details).place(x=50, y=380)

    # ==== creating command for check score button
    def select(self):
        return self.cb.get()

    # ==== scrap data
    def scrap(self):
        URL = "https://www.espncricinfo.com/scores/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="main-container")
        scrap_results = results.find_all("div", class_="match-score-block")
        return scrap_results

    # ==== fetch match details
    def match_details(self):
        details = self.scrap()
        live_match = {}
        for detail in details:
            live_team_details = {}
            summary = self.match_summary(detail)
            start_time = self.match_time(detail)
            teams = self.teams_name(detail)
            score = self.team_score(detail)
            location = self.match_location(detail)
            description = self.match_decription(detail)
            live_team_details['summary'] = summary.text
            live_team_details['start_time'] = start_time.text
            live_team_details['score'] = score
            live_team_details['location'] = location.text
            live_team_details['description'] = description
            live_match[teams[0] + " VS " + teams[1]] = live_team_details
        return live_match

    # ==== fetch match summary
    def match_summary(self, detail):
        return detail.find("span", class_="summary")

    # ==== fetch match time
    def match_time(self, detail):
        return detail.find("time", class_="dtstart")

    # ==== fetch teams name
    def teams_name(self, detail):
        teams = detail.find_all("div", class_="team")
        l = []
        for i in teams:
            l.append(i.find("div", class_="name-detail").text)
        return l

    # ==== fetch team score
    def team_score(self, detail):
        t_score = detail.find("div", class_="score-detail")
        if t_score:
            return t_score.text
        return 'Match Not Started'

    # ==== fetch match location
    def match_location(self, detail):
        return detail.find("span", class_="location")

    # ==== fetch match description
    def match_decription(self, detail):
        return detail.find("div", class_='description').text

    # ==== show details in  gui
    def show_match_details(self):

        # ==== creating match details frame
        self.frame1 = Frame(self.root, bg="white")
        self.frame1.place(x=180, y=280, width=600, height=200)

        # ==== showing team names
        Label(self.frame1, text=self.select(), font=("times new roman", 15, "bold"), bg="white", fg="green",
                      bd=0).place(x=150, y=15)

        # ==== getting details of match
        x = self.matches[self.select()]

        # ==== Showing all details of match

        Label(self.frame1, text="Summary : ", font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=10, y=40)
        Label(self.frame1, text=x['summary'], font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=20, y=60)
        Label(self.frame1, text="Start Time : ", font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=300, y=40)
        Label(self.frame1, text=x['start_time'], font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=320, y=60)
        Label(self.frame1, text="Score : ", font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=10, y=90)
        Label(self.frame1, text=x['score'], font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=20, y=110)
        Label(self.frame1, text="Location : ", font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=300, y=90)
        Label(self.frame1, text=x['location'], font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=320, y=110)
        Label(self.frame1, text="Description : ", font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=10, y=140)
        Label(self.frame1, text=x['description'], font=("times new roman", 10, "bold"), bg="white", fg="black",
              bd=0).place(x=20, y=160)


# ==== creating main function
def main():
    # ==== create tkinter window
    root = Tk()

    # === creating object for class cricket_score
    obj = CricketScore(root)
    # ==== start the gui

    root.mainloop()

if __name__ == "__main__":
    # ==== calling main function
    main()