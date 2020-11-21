import tkinter as tk
from functools import partial

"""
Class : Application
This is a main application view.
Function : 
=> quit
"""
class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.book = Book()
		self.check = 1

	"""
	info => Destroying frame
	"""
	def quit(self):
		self.master.destroy


"""
Class : ContactView
This is contact view
Function :
=> add_contact
=> show_con
"""
class ContactView(Application):
	def __init__(self, master=None):
		super().__init__(master)

		label = tk.Label(self, text="Name :", width=22, anchor="nw")
		label.place(x=0,y=0)
		self.entry = tk.Entry(self)
		self.entry.place(x=100,y=0)

		label1 = tk.Label(self, text="Phone :", width=22, anchor="nw")
		label1.place(x=0,y=20)
		self.entry1 = tk.Entry(self)
		self.entry1.place(x=100,y=20)

		label2 = tk.Label(self, text="Address :", width=22, anchor="nw")
		label2.place(x=0,y=40)
		self.entry2 = tk.Entry(self)
		self.entry2.place(x=100,y=40)
		
		submit = tk.Button(self, text="Add", command=self.add_contact)
		quit= tk.Button(self, text='QUIT', fg='red', command=self.master.quit)
		show = tk.Button(self, text="Show", command=self.show_con)

		submit.place(x=10,y=370)
		quit.place(x=350,y=370)
		show.place(x=170, y=370)


	"""
	Function : add_contact
	info => Adding contact data to the book
	"""
	def add_contact(self):
		name = self.entry.get()
		phone = self.entry1.get()
		address = self.entry2.get()

		self.book.add(Contact(name, phone, address))
		self.check = 1
		print("Berhasil ditambahkan!")

	"""
	Function : show_cocn
	info => print all the contact in book
	"""
	def show_con(self):
		if(self.check):
			label = tk.Label(self,text=self.book.printBook())
			label.place(x=0,y=80)
			self.check = 0


"""
Class : Node
This is a Node class
Handling node.
"""
class Node:
	def __init__(self, data):
		self._data = data
		self._next = None

"""
Class : Book
This is a book class
Handing all the contact info.
Function :
=> add
=> search
=> delete
=> printBook
"""
class Book:
	def __init__(self):
		self._head = None

	"""
	Function : add
	info => add contact data to the node
	"""
	def add(self, Contact):
		newNode = Node(Contact)
		if(self._head is None):
			self._head = newNode
			return

		last = self._head
		while(last._next):
			last = last._next
		last._next = newNode
	
	"""
	Function : search
	info => search data in the node
	"""
	def search(self, name):
		tempNode = self._head
		index = 1
		while(tempNode is not None and tempNode._data.getName() != name):
			tempNode = tempNode._next
			index += 1

		print(name + " is at row " + str(index))

	"""
	Function : delete
	info => delete contact in node
	"""
	def delete(self,name):
		prev_node = self._head
		curr_node = self._head

		# Check head
		while(curr_node is not None and curr_node._data.getName() != name):
			curr_node = curr_node._next 

		#Check middle and tail
		if(prev_node._data.getName() == curr_node._data.getName()):
			self._head = self._head._next 
			return

		while(prev_node._next is not None and prev_node._next._data.getName() != name):
			prev_node = prev_node._next

		# If at middle
		if(curr_node._next is not None):
			prev_node._next = curr_node._next
			curr_node = None
		# If at tail
		else:
			prev_node._next = None
			curr_node = None

	"""
	Function : printBook
	info => print all the contact in node
	return => out
	"""
	def printBook(self):
		print("test")
		out = ""
		tempNode = self._head
		while(tempNode is not None):
			out += tempNode._data.getContact()
			out += "-------------\n"
			tempNode = tempNode._next
		return out

"""
Class : Contact
This is a contact class
Function :
=> getName
=> getPhone
=> getContact
"""
class Contact:
	def __init__(self, name='A', phone='08', address='-'):
		self.name = name
		self.phone = phone
		self.address = address
	
	"""
	Function : getName
	info => get name
	return => name
	"""
	def getName(self):
		return self.name

	"""
	Function : getPhone
	info => get phone number
	return => phone
	"""
	def getPhone(self):
		return self.phone

	"""
	Function :
	info => get all the contact data
	return => output : a string that contains of name, phone, and address
	"""
	def getContact(self):
		output = "Name : " + self.name + "\nPhone Number : " + self.phone + "\nAddress : " + self.address + "\n"
		return output


"""
Main
"""
if __name__ == '__main__':
	root = tk.Tk()
	main = ContactView(root)
	main.pack(side="top", fill="both", expand=True)
	root.geometry("400x400")
	root.mainloop()