import requests
from tkinter import *

"""------------EDITOR's PANEL-----------"""
QUOTE_FONT = ("Arial", 30, "bold")
QUOTE_FONT_COLOR = "white"

#------------------------------------------#
"""____________get caught function_________"""
def get_quote():
    response = requests.get(url = "https://api.kanye.rest/")
    data = response.json()
    quote = data["quote"]

    canvas.itemconfig(quote_text, text = quote)

#------------------------------------------#
"""_________creating the window____________"""
window = Tk()
window.title("kanye's Quotes ....")
window.config(padx = 50, pady = 50)

#------------------------------------------#
"""_________creating the canvas:bg img and kanye text________________"""
canvas = Canvas(width = 300, height = 414)
background_img = PhotoImage(file ="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207,
                                text = "Click Kanye's face to get a quote",
                                width = 250,
                                font = QUOTE_FONT,
                                fill = QUOTE_FONT_COLOR
                                )
canvas.grid(column = 0, row = 0)

#-----------------------------------------------------------------------#
"""______________________Kanye button___________________________________"""
kanye_img = PhotoImage(file ="kanye.png")
kanye_button = Button(image = kanye_img, highlightthickness = 0, command=get_quote)
kanye_button.grid(column = 0, row = 1)




"""_______running the window without closing________"""
window.mainloop()

#----------------------------------------------------#