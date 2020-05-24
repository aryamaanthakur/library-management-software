"""
SUBMITTED BY:- ARYAMAAN THAKUR, CLASS-XII-A
"""

import os
from prettytable import PrettyTable
import mysql.connector as sqltor
import datetime

os.system("mode con cols=130")

mycon = sqltor.connect(host = 'localhost',
                       user = 'root',
                       passwd = 'root',
                       database = 'library')


cursor = mycon.cursor()

def banner():
	print("""  _    _ _                        __  __                                       _     ___       __ _                       
 | |  (_) |__ _ _ __ _ _ _ _  _  |  \/  |__ _ _ _  __ _ __ _ ___ _ __  ___ _ _| |_  / __| ___ / _| |___ __ ____ _ _ _ ___ 
 | |__| | '_ \ '_/ _` | '_| || | | |\/| / _` | ' \/ _` / _` / -_) '  \/ -_) ' \  _| \__ \/ _ \  _|  _\ V  V / _` | '_/ -_)
 |____|_|_.__/_| \__,_|_|  \_, | |_|  |_\__,_|_||_\__,_\__, \___|_|_|_\___|_||_\__| |___/\___/_|  \__|\_/\_/\__,_|_| \___|
                           |__/                        |___/                                                              """)

def Input(msg, data):
	while True:
		inp=input("[+] "+msg+": ")
		if inp!="":
			data.append(inp)
			break

def addbook():
	os.system("cls")
	banner()
	print("\tADD BOOK")
	data = ['NULL']

	Input("Enter book name", data)
	Input("Enter author's name", data)
	Input("Enter publication", data)
	Input("Enter category", data)

	while True:
		try:
			price = int(input("[+] Enter price: "))
			data.append(int(price))
			break
		except ValueError:
			print("[-] Enter a number")
	Input("Enter ISBN", data)

	cursor.execute("INSERT INTO books VALUES({},'{}','{}','{}','{}',{},'{}',DEFAULT);".format(*data))
	mycon.commit()
	input("[+] Book added successfully. Press Enter to continue...")

def deletebook():
	os.system("cls")
	banner()
	print("\tDELETE BOOK")

	while True:
		try:
			bookID = input("[+] Enter bookID: ")
			if bookID == "x":
				return None
			bookID = int(bookID)
			break
		except ValueError:
			print("[-] Enter a number")
			continue
	cursor.execute("SELECT * FROM books WHERE bookID={};".format(bookID))
	data = cursor.fetchone()
	if data==None or data[-1]=="DELETED":
		print("[-] Book does not exist")
	else:
		pt = PrettyTable()
		pt.field_names = ["BookID", "Name", "Author", "Publication", "Category", "Price", "ISBN", "Status"]
		pt.add_row(data)
		print(pt)
		while True:
			cmd = input("[+] Delete this book? [y/n]: ")
			if cmd.lower() == "y":
				cursor.execute("UPDATE books SET status='DELETED' WHERE bookID={}".format(bookID))
				mycon.commit()
				print("[+] Book deleted successfully")
				break
			elif cmd.lower() == "n":
				break

	input("[+] Press Enter to continue...")

def addmember():
	os.system("cls")
	banner()
	print("\tADD MEMBER")
	data = ['NULL']

	Input("Enter member's name", data)
	Input("Enter phone number", data)
	Input("Enter address", data)
	Input("Enter email address", data)

	cursor.execute("INSERT INTO members VALUES({},'{}','{}','{}','{}',DEFAULT);".format(*data))
	mycon.commit()
	input("[+] Member added successfully. Press Enter to continue...")

def deletemember():
	os.system("cls")
	banner()
	print("\tDELETE MEMBER")
	while True:
		try:
			memberID = input("[+] Enter memberID: ")
			if memberID == "x":
				return None
			memberID = int(memberID)
			break
		except ValueError:
			print("[-] Enter a number")
	cursor.execute("SELECT * FROM members WHERE memberID={};".format(memberID))
	data = cursor.fetchone()
	if data==None or data[-1]=="DELETED":
		print("[-] Member does not exist")
	else:
		pt = PrettyTable()
		pt.field_names = ["MemberID", "Name", "Phone Number", "Address", "E-mail", "Status"]
		pt.add_row(data)
		print(pt)
		while True:
			cmd = input("[+] Delete this member? [y/n]: ")
			if cmd.lower() == "y":
				cursor.execute("UPDATE members SET status='DELETED' WHERE memberID={}".format(memberID))
				mycon.commit()
				print("[+] Member deleted successfully")
				break
			elif cmd.lower() == "n":
				break

	input("[+] Press Enter to continue...")

def issue():
	os.system("cls")
	banner()
	print("\tISSUE")

	while True:
		try:
			bookID = input("[+] Enter bookID: ")
			if bookID == "x":
				return None
			bookID = int(bookID)
		except ValueError:
			print("[-] Enter a number")
			continue
		cursor.execute("SELECT * FROM books WHERE bookID={};".format(bookID))
		data = cursor.fetchone()
		if data==None or data[-1]=="DELETED":
			print("[-] Book does not exist")
		elif data[-1]=="ISSUED":
			print("[-] Book is not available")
		else:
			pt = PrettyTable()
			pt.field_names = ["BookID", "Name", "Author", "Publication", "Category", "Price", "ISBN", "Status"]
			pt.add_row(data)
			print(pt)
			break

	while True:
		try:
			memberID = input("[+] Enter memberID: ")
			if memberID == "x":
				return None
			memberID = int(memberID)
		except ValueError:
			print("[-] Enter a number")
			continue
		cursor.execute("SELECT * FROM members WHERE memberID={};".format(memberID))
		data = cursor.fetchone()
		if data==None or data[-1]=="DELETED":
			print("[-] Member does not exist")
		elif data[-1]=="ISSUED":
			print("[-] Member has already issued a book")
		else:
			pt = PrettyTable()
			pt.field_names = ["MemberID", "Name", "Phone Number", "Address", "E-mail", "Status"]
			pt.add_row(data)
			print(pt)
			break

	while True:
			cmd = input("[+] Issue? [y/n]: ")
			if cmd.lower() == "y":
				data = ['NULL', bookID, memberID, datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')]
				print(data)
				cursor.execute("INSERT INTO transactions VALUES({},{},{},'{}', NULL, DEFAULT)".format(*data))
				cursor.execute("UPDATE books SET status='ISSUED' WHERE bookID={}".format(bookID))
				cursor.execute("UPDATE members SET status='ISSUED' WHERE memberID={}".format(memberID))
				mycon.commit()
				print("[+] Book issued successfully")
				break
			elif cmd.lower() == "n":
				break
	input("[+] Press Enter to continue...")

def Return():
	os.system("cls")
	banner()
	print("\tRETURN")

	while True:
		try:
			transactionID = input("[+] Enter transactionID: ")
			if transactionID == "x":
				return None
			transactionID = int(transactionID)
		except ValueError:
			print("[-] Enter a number")
			continue
		cursor.execute("SELECT * FROM transactions WHERE transactionID={};".format(transactionID))
		data = cursor.fetchone()
		if data==None:
			print("[-] Transaction does not exist")
		elif data[-1]=="RETURNED":
			print("[-] Book returned already")
		else:
			pt = PrettyTable()
			pt.field_names = ["TransactionID", "BookID", "MemberID", "Issue Date", "Return Date", "Status"]
			pt.add_row(data)
			print(pt)
			bookID = data[1]
			memberID = data[2]
			break
	while True:
			cmd = input("[+] Return? [y/n]: ")
			if cmd.lower() == "y":
				
				print(data)
				cursor.execute("UPDATE transactions SET status='RETURNED', returndate='{}' WHERE transactionID={}".format(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), transactionID))
				cursor.execute("UPDATE books SET status='ACTIVE' WHERE bookID={}".format(bookID))
				cursor.execute("UPDATE members SET status='ACTIVE' WHERE memberID={}".format(memberID))
				mycon.commit()
				print("[+] Book returned successfully")
				break
			elif cmd.lower() == "n":
				break
	input("[+] Press Enter to continue...")

def searchbook():

	fields = {"2":"name", "3":"author", "4":"publication", "5":"category"}

	while True:
		os.system("cls")
		banner()
		print("\tSEARCH BOOK\n")

		print("""Search by:
		[1] BookID
		[2] Name
		[3] Author
		[4] Publication
		[5] Category
		[6] Price
		[7] ISBN
		[8] Status
		""")
		cmd = input()
		if cmd == "1":
			while True:
				try:
					bookID = input("[+] Enter bookID: ")
					if bookID == "x":
						return None
					bookID = int(bookID)
					break
				except ValueError:
					print("[-] Enter a number")
					continue
			cursor.execute("SELECT * FROM books WHERE bookID={};".format(bookID))
			data = cursor.fetchone()
			if data==None:
				print("[-] Book does not exist")
			else:
				pt = PrettyTable()
				pt.field_names = ["BookID", "Name", "Author", "Publication", "Category", "Price", "ISBN", "Status"]
				pt.add_row(data)
				print(pt)

		elif cmd == "7":
			while True:
				isbn = input("Enter ISBN: ")
				if isbn != "":
					break
				elif isbn.lower() == "x":
					return None
			cursor.execute("SELECT * FROM books WHERE isbn={};".format(isbn))
			data = cursor.fetchall()
			if data==[]:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["BookID", "Name", "Author", "Publication", "Category", "Price", "ISBN", "Status"]
				for row in data:
					pt.add_row(row)
				print(pt)

		elif cmd in fields:
			focus = fields[cmd]
			while True:
				term = input("Enter "+fields[cmd]+": ")
				if term!="":
					break
			cursor.execute("SELECT * FROM books WHERE {} LIKE '%{}%' ORDER BY {}".format(focus,term,focus))
			data = cursor.fetchall()
			if data==[]:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["BookID", "Name", "Author", "Publication", "Category", "Price", "ISBN", "Status"]
				for row in data:
					pt.add_row(row)
				print(pt)

		elif cmd == "6":
			while True:
				try:
					Min = input("[+] Enter minimum price: ")
					if Min == "x":
						return None
					Min = int(Min)
					break
				except ValueError:
					print("[-] Enter a number")
					continue
			while True:
				try:
					Max = input("[+] Enter maximum price: ")
					if Max == "x":
						return None
					Max = int(Max)
					break
				except ValueError:
					print("[-] Enter a number")
					continue
			cursor.execute("SELECT * FROM books WHERE price BETWEEN {} AND {} ORDER BY price".format(Min, Max))
			data = cursor.fetchall()
			if data==[]:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["BookID", "Name", "Author", "Publication", "Category", "Price", "ISBN", "Status"]
				for row in data:
					pt.add_row(row)
				print(pt)

		elif cmd == "8":
			print("""
		[1] ACTIVE
		[2] ISSUED
		[3] DELETED
				""")
			while True:
				cmd = input()
				if cmd == "1":
					status = "ACTIVE"
					break
				elif cmd == "2":
					status = "ISSUED"
					break
				elif cmd == "3":
					status = "DELETED"
				elif cmd.lower() == "x":
					return None
				else:
					input("[-] Invalid command. Press Enter to continue...")
					continue
			cursor.execute("SELECT * FROM books WHERE status='{}'".format(status))
			data = cursor.fetchall()
			if data==[]:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["BookID", "Name", "Author", "Publication", "Category", "Price", "ISBN", "Status"]
				for row in data:
					pt.add_row(row)
				print(pt)

		elif cmd.lower() == "x":
			return None
		elif cmd == "": continue
		else:
			input("[-] Invalid Command. Press Enter to continue...")
			continue
		input("[+] Press Enter to continue...")
				
def searchmember():

	fields = {"2":"name", "3":"phone", "4":"address", "5":"email"}

	while True:
		os.system("cls")
		banner()
		print("\tSEARCH BOOK\n")

		print("""Search by:
		[1] BookID
		[2] Name
		[3] Phone number
		[4] Address
		[5] E-mail
		[6] Status
		""")
		cmd = input()
		if cmd == "1":
			while True:
				try:
					memberID = input("[+] Enter memberID: ")
					if memberID == "x":
						return None
					memberID = int(memberID)
					break
				except ValueError:
					print("[-] Enter a number")
					continue
			cursor.execute("SELECT * FROM members WHERE memberID={};".format(memberID))
			data = cursor.fetchone()
			if data==None:
				print("[-] Member does not exist")
			else:
				pt = PrettyTable()
				pt.field_names = ["MemberID", "Name", "Phone", "Address", "E-mail", "Status"]
				pt.add_row(data)
				print(pt)

		elif cmd in fields:
			focus = fields[cmd]
			while True:
				term = input("Enter "+fields[cmd]+": ")
				if term!="":
					break
			cursor.execute("SELECT * FROM members WHERE {} LIKE '%{}%' ORDER BY {}".format(focus,term,focus))
			data = cursor.fetchall()
			if data==[]:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["MemberID", "Name", "Phone", "Address", "E-mail", "Status"]
				for row in data:
					pt.add_row(row)
				print(pt)

		elif cmd == "6":
			print("""
		[1] ACTIVE
		[2] ISSUED
		[3] DELETED
				""")
			while True:
				cmd = input()
				if cmd == "1":
					status = "ACTIVE"
					break
				elif cmd == "2":
					status = "ISSUED"
					break
				elif cmd == "3":
					status = "DELETED"
					break
				elif cmd.lower() == "x":
					return None
				else:
					input("[-] Invalid command. Press Enter to continue...")
					continue
			cursor.execute("SELECT * FROM members WHERE status='{}'".format(status))
			data = cursor.fetchall()
			if data==[]:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["MemberID", "Name", "Phone", "Address", "E-mail", "Status"]
				for row in data:
					pt.add_row(row)
				print(pt)

		elif cmd.lower() == "x":
			return None
		elif cmd == "": continue
		else:
			input("[-] Invalid Command. Press Enter to continue...")
			continue
		input("[+] Press Enter to continue...")

def transactionsearch():
	fields = {"4":"issuedate", "5":"returndate"}

	while True:
		os.system("cls")
		banner()
		print("\tSEARCH BOOK\n")

		print("""Search by:
		[1] TrasactionID
		[2] BookID
		[3] MemberID
		[4] Issue Date
		[5] Return Date
		[6] Status
		""")

		cmd = input()
		if cmd == "1":
			while True:
				try:
					transactionID = input("[+] Enter TransactionID: ")
					if transactionID == "x":
						return None
					transactionID = int(transactionID)
					break
				except ValueError:
					print("[-] Enter a number")
					continue
			cursor.execute("SELECT * FROM transactions WHERE transactionID={};".format(transactionID))
			data = cursor.fetchone()
			if data==None:
				print("[-] Transaction does not exist")
			else:
				pt = PrettyTable()
				pt.field_names = ["TransactionID", "BookID", "MemberID", "Issue Date", "Return Date", "Status"]
				pt.add_row(data)
				print(pt)

		elif cmd == "2":
			while True:
				try:
					bookID = input("[+] Enter bookID: ")
					if bookID == "x":
						return None
					bookID = int(bookID)
					break
				except ValueError:
					print("[-] Enter a number")
					continue
			cursor.execute("SELECT * FROM transactions WHERE bookID={};".format(bookID))
			data = cursor.fetchone()
			if data==None:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["TransactionID", "BookID", "MemberID", "Issue Date", "Return Date", "Status"]
				pt.add_row(data)
				print(pt)

		elif cmd == "3":
			while True:
				try:
					memberID = input("[+] Enter memberID: ")
					if memberID == "x":
						return None
					memberID = int(memberID)
					break
				except ValueError:
					print("[-] Enter a number")
					continue
			cursor.execute("SELECT * FROM transactions WHERE memberID={};".format(memberID))
			data = cursor.fetchone()
			if data==None:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["TransactionID", "BookID", "MemberID", "Issue Date", "Return Date", "Status"]
				pt.add_row(data)
				print(pt)


		elif cmd in fields:
			focus = fields[cmd]
			while True:
				term = input("Enter "+fields[cmd]+": ")
				if term!="":
					break
			cursor.execute("SELECT * FROM transactions WHERE {} LIKE '%{}%' ORDER BY {}".format(focus,term,focus))
			data = cursor.fetchall()
			if data==[]:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["TransactionID", "BookID", "MemberID", "Issue Date", "Return Date", "Status"]
				for row in data:
					pt.add_row(row)
				print(pt)

		elif cmd == "6":
			print("""
		[1] ISSUED
		[2] RETURNED
				""")
			while True:
				cmd = input()
				if cmd == "1":
					status = "ISSUED"
					break
				elif cmd == "2":
					status = "RETURNED"
					break
				elif cmd.lower() == "x":
					return None
				else:
					input("[-] Invalid command. Press Enter to continue...")
					continue
			cursor.execute("SELECT * FROM transactions WHERE status='{}'".format(status))
			data = cursor.fetchall()
			if data==[]:
				print("[-] No records found")
			else:
				pt = PrettyTable()
				pt.field_names = ["TransactionID", "BookID", "MemberID", "Issue Date", "Return Date", "Status"]
				for row in data:
					pt.add_row(row)
				print(pt)

		elif cmd.lower() == "x":
			return None
		elif cmd == "": continue
		else:
			input("[-] Invalid Command. Press Enter to continue...")
			continue
		input("[+] Press Enter to continue...")

def reports():
	
	while True:
		os.system("cls")
		banner()
		print("\tREPORTS\n")

		print("""
		[1] Books
		[2] Members
		[3] Transactions
		""")
		cmd = input()
		if cmd=="1":
			file = open("books.txt", mode = "w")
			cursor.execute("SELECT * FROM books")
			data = cursor.fetchall()
			pt = PrettyTable()
			pt.field_names = ["BookID", "Name", "Author", "Publication", "Category", "Price", "ISBN", "Status"]
			for row in data:
				pt.add_row(row)
			file.write(str(pt))
			file.close()
			print("[+] The database has been copied to books.txt")
		elif cmd=="2":
			file = open("members.txt", mode = "w")
			cursor.execute("SELECT * FROM members")
			data = cursor.fetchall()
			pt = PrettyTable()
			pt.field_names = ["MemberID", "Name", "Phone", "Address", "E-mail", "Status"]
			for row in data:
				pt.add_row(row)
			file.write(str(pt))
			file.close()
			print("[+] The database has been copied to members.txt")
		elif cmd=="3":
			file = open("transactions.txt", mode = "w")
			cursor.execute("SELECT * FROM transactions")
			data = cursor.fetchall()
			pt = PrettyTable()
			pt.field_names = ["TransactionID", "BookID", "MemberID", "Issued On", "Returned On", "Status"]
			for row in data:
				pt.add_row(row)
			file.write(str(pt))
			file.close()
			print("[+] The database has been copied to transactions.txt")
		elif cmd.lower()=="x":
 			break
		elif cmd == "": continue
		else:
 			input("[-] Invalid command. Press Enter to continue...")

while True:
	os.system("cls")
	banner()
	
	print("""
	[1] Issue
	[2] Return
	[3] Add Book
	[4] Add Member
	[5] Delete Book
	[6] Delete Member
	[7] Search Books
	[8] Search Members
	[9] Search Transactions
	[0] Reports
	[x] Exit
	""")
	cmd = input()
	if cmd == "1": issue()
	elif cmd == "2": Return()
	elif cmd == "3": addbook()
	elif cmd == "4": addmember()
	elif cmd == "5": deletebook()
	elif cmd == "6": deletemember()
	elif cmd == "7": searchbook()
	elif cmd == "8": searchmember()
	elif cmd == "9": transactionsearch()
	elif cmd == "0": reports()
	elif cmd.lower() == "x": break
	elif cmd == "": None
	else: 
		print("[-] Invalid Command. Press Enter to continue...")
		input()

mycon.close()
