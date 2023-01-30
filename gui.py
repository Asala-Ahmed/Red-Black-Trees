from tkinter import *
from RBTree import *
rbt = RBTree()
window = Tk()
Label(window, text='EN-US-Dictionary', width=50, height=5).pack()
Label(window, text='Enter value to insert').pack()

entryInsert = Entry(window)
entryInsert.pack()

resultInsert = Label(window)
resultInsert.pack()


def clicked_insert():
    ans_insert = rbt.insert(entryInsert.get())
    if ans_insert == -1:
        resultInsert.configure(text="ERROR:Word already in the dictionary!")
    else:
        resultInsert.configure(text="Insertion complete")


Button(window, text='OK', command=clicked_insert, width=10).pack()

Label(window, text='Enter value to search').pack()

entrySearch = Entry(window)
entrySearch.pack()

resultSearch = Label(window)
resultSearch.pack()


def clicked_search():
    key = entrySearch.get()
    ans_search = rbt.search(rbt.root, key)
    if ans_search == rbt.leafNil:
        resultSearch.configure(text="NO")
    else:
        resultSearch.configure(text="YES")


Button(window, text='OK', command=clicked_search, width=10).pack()

print_size = Label(window)
print_size.pack()


def clicked_size():
    print_size.configure(text=rbt.totalNodes(rbt.root))


Button(window, text='Print Size', command=clicked_size, width=10).pack()
print_height = Label(window)
print_height.pack()


def clicked_height():
    print_height.configure(text=rbt.height(rbt.root))


Button(window, text='Print Height', command=clicked_height, width=10).pack()
Button(window, text='END', command=window.destroy, width=10).pack()
