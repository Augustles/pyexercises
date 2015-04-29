# coding=utf-8

from Tkinter import *  # 导入tkinter
import tkMessageBox  # 导入message


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()  # 最简单的布局，图形管理器 .pack() .grid() .place()
        self.createWidgets()

    def createWidgets(self):  # 创建label和button
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='你好', command=self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self, text='quit')
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or '！'
        tkMessageBox.showinfo('Message', '你好, %s' % name)

if __name__ == '__main__':
    app = Application()
    app.master.title('welcome！')  # 窗体title
    app.mainloop()
