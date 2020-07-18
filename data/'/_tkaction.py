"""Launcher of a needed file. *Undone.*"""


import tkinter
import os

import tkinter.messagebox as mbox
import tkinter.simpledialog as dialog


from action import action  # Mind this import.


### Tests ##############################################################################

# info = tkinter.Label(window, text="Possible tasks: get answers for the exect question")

window0 = tkinter.Tk()

buttons = tkinter.Label(window)


_TABLE = """
╔═╤═╤═╗
║ │ │ ║
╟─┼─┼─╢
║ │ │ ║
╟─┼─┼─╢ 
║ │ │ ║
╚═╧═╧═╝
"""

_TABLE0 = """
╔═╤═╤═╗
║{}│{}│{}║
╟─┼─┼─╢
║{}│{}│{}║
╟─┼─┼─╢ 
║{}│{}│{}║
╚═╧═╧═╝
"""

_TABLE01 = """
╔═══╤═══╤═══╗
║{}│{}│{}║
╟───┼───┼───╢
║{}│{}│{}║
╟───┼───┼───╢ 
║{}│{}│{}║
╚═══╧═══╧═══╝
"""

def table(a):
	def _align(line, n_times, *, by_symbol=" "):
		return by_symbol * ((n_times + 1 - 1) // 2) + line + by_symbol * ((n_times + 0 - 1) // 2)
	line = "╟" + "┼".join([
		                  "─"*a for i in range(3)  # Number of columns
		                  ]) + "╢"
	input_line = "║" + "│".join([
		                        _align("{}", a) for i in range(3) #t <-  # "{:=" + str(a) + "}" for i in range(3)  # Same as in previous
		                        ]) +"║"
	return f'╔{"═"*a}╤{"═"*a}╤{"═"*a}╗\n'\
+ input_line + '\n' \
+ line + '\n' \
+ input_line + '\n' \
+ line + '\n' \
+ input_line + '\n' \
+ f'╚{"═"*a}╧{"═"*a}╧{"═"*a}╝'  # \n"\"╚═══╧═══╧═══╝"

_TABLE02 = '\n' + table(3)

# TEST

answers, folder = [2, 8], 'NOT THIS'

maybe_result = tkinter.Label(window0, font=("Consolas", 14))
maybe_result.pack()

maybe_result.configure(text="""Answers:{}\nDetailed information is in folder {!r}.""".format(
			_TABLE02.format(*["•" if n in answers else " " for n in range(1, 10)]), folder))


__import__("time").sleep(10)
# ------------------------------------

### "Worker" ###########################################################################

# window = tkinter.Tk()
window.title("Suggested answers for the exect question")

main = tkinter.Label(window)


result = tkinter.Label(window, font=("Consolas", 14)) 

label = tkinter.Label(main, text="The text: ")
field = tkinter.Entry(main)

def res_config():
	text = field.get()
	action_res = action(text)
	folder, answers = action_res
	result.configure(text="""Answers:{}\nDetailed information is in folder {!r}.""".format(
			_TABLE02.format(*["•" if n in answers else " " for n in range(1, 10)]), folder))

field.bind("<Return>", lambda event: res_config())

label.pack(side="left")
field.pack(fill="x")
main.pack()

tkinter.Button(window, text="Quit", command=window.destroy).pack()  # (c) self, ~EOF


window.mainloop()


13.37/0
# -------------------------------------

# It was before as a part of testing with this file:

'''
def local_cmd():
	from action import action

	text = dialog.askstring("Entering of the string", "Input a string of the page's code here.")
	if mbox.askyesno("Question", "Process it? (It may last some seconds.)"):
		# folder, answers = action(text)
		#t:
		answers, folder = [2, 8], 'NOT THIS'

		print(1)
		mbox.showinfo("Result", """Answers:{}\nDetailed information is in folder {!r}.""".format(
			_TABLE0.format(*["•" if n in answers else " " for n in range(1, 10)]), folder), font=("Arial Black", 14))
		# mbox.showinfo("Result", "Answers: {}\n.More info is in {}.".format(result[1], result[0]))

	# mbox.showinfo("Done", "See the folder Local for the results. THIS IS UNDONE")

	"""
	from action import action
	w = tkinter.Tk()

	entry = tkinter.Entry(w)

	entry.bind('<Return>', lambda event: (action(entry.get()),
	                                      dialog.showinfo("Done. See the folder <...>")))  #?: 1+1 times

	entry.pack()
	w.mainloop()"""

launch_local = tkinter.Button(buttons, text="Get answers for the exect question", command=local_cmd)

# task = 


launch_local.pack()

# info.pack()
buttons.pack()

tkinter.Button(window, text="Quit", command=window.destroy).pack()  # The quit button.


window.mainloop()

__import__("sys").exit(None)
7/0

# ------------------
info = tkinter.Label(window)



def cinfo(*, text=None, is_text='yes'):  #?
    if text is None:
    	text = str(None)
    info.configure(text='Info: ' + text)

field = tkinter.Entry(window)

def ffield():
    maybe_filename = field.get()
    try:
        os.startfile(maybe_filename)
        cinfo(text=None)
    except Exception as e:
        cinfo(text=str(e))

field.bind('<Enter>', lambda event: ffield())

field.pack(fill='x'); info.pack(fill='x')


window.mainloop()


# if __name__ == '__main__': pass # os.startfile(input())
'''