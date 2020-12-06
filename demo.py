from guizero import App,Drawing, Text
app = App()


d = Drawing(app, width=300, height=300)
app.title = "Conveyor Path"



d.line(50, 180, 170, 180, color="blue",width=5)
d.line(170, 180, 170, 50, color="red",width=5)
d.line(170, 180, 170, 260, color="green",width=5)
d.line(50, 50, 100, 50, color="yellow",width=5)
d.line(50, 50, 50, 180, color="light blue",width=5) 
d.line(100, 50, 100, 180, color="orange",width=5)

d.line(0, 300, 300, 300, color="black",width=5)
d.line(300, 0, 300, 300, color="black",width=5)
d.line(0, 0, 0, 300, color="black",width=5)
d.line(0, 0, 300, 0, color="black",width=5)



text = Text(app, text="Conveyor Main Overview")
text.text_color ="Black"

text = Text(app, text="Conveyor 1 = Green")
text.text_color = "Green"

text = Text(app, text="Conveyor 2 = Red")
text.text_color = "Red"

text = Text(app, text="Conveyor 3 = Blue")
text.text_color = "Blue"

text = Text(app, text="Conveyor 4 = Orange")
text.text_color = "Orange"

text = Text(app, text="Conveyor 5 = Yellow")
text.text_color = "Yellow"

text = Text(app, text="Conveyor 6 = Light Blue")
text.text_color = "Light Blue" 



raspivid -md 1 -t 0 -p 22,50,960,540




app.display()

