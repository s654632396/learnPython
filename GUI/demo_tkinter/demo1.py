# coding=utf-8

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

"""
在GUI中，每个Button/Label/表单等，都是一个Widget
Frame则是一个可以包容其他Widget的Widget
所有的Widget组合起来就是一颗树
"""
app = Application()
app.master.title('hello World.')
app.mainloop()



