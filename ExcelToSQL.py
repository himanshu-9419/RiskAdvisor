import xlrd
import MySQLdb
import time
import datetime

# Open the workbook and define the worksheet
book = xlrd.open_workbook("StockData.xlsx")
sheet = book.sheet_by_index(0)

# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "root", passwd = "no", db = "RiskAdvisor")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO stock_stock (Date, Open, High, Low, Close, Volume, Adj, Stock) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
      dateInt      = sheet.cell(r,0).value
      open = sheet.cell(r,1).value
      high          = sheet.cell(r,2).value
      low     = sheet.cell(r,3).value
      close       = sheet.cell(r,4).value
      volume = sheet.cell(r,5).value
      adj       = sheet.cell(r,6).value
      stock       = sheet.cell(r,7).value
      date = datetime.datetime(*time.strptime("Dec 30 1899", "%b %d %Y")[:6]) +datetime.timedelta(days=int(dateInt))
      date=date.date()            
      print date
      # Assign values from each row
      values = (date,open,high,low,close,volume,adj,stock)

      # Execute sql Query
      cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done! Bye, for now."
print ""

