import random
import sqlite3


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ti = 20
        self.p = 1

        Clock.schedule_once(self.exit_time, self.ti)
        Clock.schedule_interval(self.time, 1)

        con = sqlite3.connect("quizz.db")
        cur = con.cursor()

        self.cols = 2

        if self.ti > 9:
            self.label = Label(text="0:" + str(self.ti))
        else:
            self.label = Label(text="0:0" + str(self.ti))
        self.add_widget(self.label)

        table = "SELECT *FROM level_" + str(1) + " WHERE id=" + str(random.randint(1, 2))
        self.username = TextInput(text=cur.execute(table).fetchall()[0][1], multiline=True)
        self.add_widget(self.username)
        self.answer = cur.execute(table).fetchall()[0][6]

        self.submit_button1 = Button(text=cur.execute(table).fetchall()[0][2])
        self.submit_button1.on_release = self.submit1
        self.add_widget(self.submit_button1)
        self.submit_button2 = Button(text=cur.execute(table).fetchall()[0][3])
        self.submit_button2.on_release = self.submit2
        self.add_widget(self.submit_button2)
        self.submit_button3 = Button(text=cur.execute(table).fetchall()[0][4])
        self.submit_button3.on_release = self.submit3
        self.add_widget(self.submit_button3)
        self.submit_button4 = Button(text=cur.execute(table).fetchall()[0][5])
        self.submit_button4.on_release = self.submit4
        self.add_widget(self.submit_button4)

        self.output = Label(text="")
        self.add_widget(self.output)

    def next(self):
        con = sqlite3.connect("quizz.db")
        cur = con.cursor()
        if self.p < 6:
            table = "SELECT *FROM level_" + str(self.p) + " WHERE id=" + str(random.randint(1, 2))
            self.username.text = cur.execute(table).fetchall()[0][1]
            self.submit_button1.text = cur.execute(table).fetchall()[0][2]
            self.submit_button2.text = cur.execute(table).fetchall()[0][3]
            self.submit_button3.text = cur.execute(table).fetchall()[0][4]
            self.submit_button4.text = cur.execute(table).fetchall()[0][5]
            self.answer = cur.execute(table).fetchall()[0][6]
        else:
            self.output.text = "Вы победили!!!"

    def submit1(self):
        try:
            if self.answer == self.submit_button1.text:
                self.output.text = "Правильно"
                self.p += 1
                self.ti = 20
                Clock.unschedule(self.exit_time)
                Clock.schedule_once(self.exit_time, self.ti)
                self.next()

            else:
                self.ti -= 5
                Clock.unschedule(self.exit_time)
                Clock.schedule_once(self.exit_time, self.ti)
        except Exception as e:
            self.output.text = "%s" % e

    def submit2(self):
        try:
            if self.answer == self.submit_button2.text:
                self.output.text = "правильно"
                self.p += 1
                self.ti = 20
                Clock.unschedule(self.exit_time)
                Clock.schedule_once(self.exit_time, self.ti)
                self.next()
            else:
                self.ti -= 5
                Clock.unschedule(self.exit_time)
                Clock.schedule_once(self.exit_time, self.ti)
        except Exception as e:
            self.output.text = "%s" % e

    def submit3(self):
        try:
            if self.answer == self.submit_button3.text:
                self.output.text = "правильно"
                self.p += 1
                self.ti = 20
                Clock.unschedule(self.exit_time)
                Clock.schedule_once(self.exit_time, self.ti)
                self.next()
            else:
                self.ti -= 5
                Clock.unschedule(self.exit_time)
                Clock.schedule_once(self.exit_time, self.ti)
        except Exception as e:
            self.output.text = "%s" % e

    def submit4(self):
        try:
            if self.answer == self.submit_button4.text:
                self.output.text = "правильно"
                self.p += 1
                self.ti = 20
                Clock.unschedule(self.exit_time)
                Clock.schedule_once(self.exit_time, self.ti)
                self.next()
            else:
                self.ti -= 5
                Clock.unschedule(self.exit_time)
                Clock.schedule_once(self.exit_time, self.ti)
        except Exception as e:
            self.output.text = "%s" % e

    def exit_time(self, dt):
        exit()

    def time(self, dt):
        self.ti -= 1
        if self.ti > 9:
            self.label.text = "0:" + str(self.ti)
        else:
            self.label.text = "0:0" + str(self.ti)


class MyApp(App):

    def build(self):
        return LoginScreen()


MyApp().run()
