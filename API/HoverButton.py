import tkinter

class HoverButton(tkinter.Button):

    def __init__(self, master, hoverColor, backgroundColor, **kw):

        tkinter.Button.__init__(self, master=master, **kw)

        self.defaultBackground = backgroundColor
        self.activeBackground = hoverColor

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self.activeBackground

    def on_leave(self, e):
        self['background'] = self.defaultBackground

    def setHoverColor(self, color : str):
        self.activeBackground = color