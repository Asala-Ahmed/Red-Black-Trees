import gui
if __name__ == "__main__":
    rbt = gui.rbt
    f = open("EN-US-Dictionary.txt", "r")
    for x in f:
        rbt.insert(x.strip('\n'))
    f.close()
    gui.window.mainloop()
    rbt.printinorder(rbt.root)

