import sqlite3

connection = sqlite3.connect('student_DB.db')
c = connection.cursor()

def create_tabel():

	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(name TEXT, score1 REAL, score2 REAL, score3 REAL)')

def data_entry():

	c.execute("INSERT INTO stuffToPlot VALUES('Joe Smith', '70', '30', '100')")
	c.execute("INSERT INTO stuffToPlot VALUES('Bob', '90', '50', '1000')")
	c.execute("INSERT INTO stuffToPlot VALUES('Charlie', '60', '70', '80')")
	c.execute("INSERT INTO stuffToPlot VALUES('Jeremy', '60', '60', '70')")
	c.execute("INSERT INTO stuffToPlot VALUES('Jackson', '90', '80', '70')")
	c.execute("INSERT INTO stuffToPlot VALUES('Todd', '100', '50', '50')")
	c.execute("INSERT INTO stuffToPlot VALUES('harry', '90', '60', '50')")
	c.execute("INSERT INTO stuffToPlot VALUES('Jason', '60', '50', '60')")
	c.execute("INSERT INTO stuffToPlot VALUES('Jack', '40', '60', '80')")
	c.execute("INSERT INTO stuffToPlot VALUES('Joe', '70', '80', '60')")

	connection.commit()
	c.close()
	connection.close()

create_tabel()
data_entry()


