
import tkinter
from tkinter import filedialog, messagebox
import sqlite3



class accountingWindow(tkinter.Frame):
    #accounting Window

    def __init__(self, parent):

        self.parent = parent

        tkinter.Frame.__init__(self, parent)

        self.menuBar =  tkinter.Menu(parent)
        self.parent.config(menu = self.menuBar)
        self.fileMenu = tkinter.Menu(self.menuBar, tearoff = 0)
        self.menuBar.add_cascade(label = 'File', menu = self.fileMenu)
        self.fileMenu.add_command(label = 'Connect', command = self.connectDatabase)
        self.fileMenu.add_command(label = 'About')
        self.fileMenu.add_command(label = 'Exit') 

        self.generateWidgets()

    def generateWidgets(self):

        self.mainFrame = tkinter.LabelFrame(self, text = "Accounts")


        #Accounts Window

        #Account List Frame
        self.mainFrame.accountListFrame = tkinter.LabelFrame(self.mainFrame, text = "Master Account List")  
        self.mainFrame.accountListFrame.accountList = tkinter.Listbox(self.mainFrame.accountListFrame, width = 50)
        self.mainFrame.accountListFrame.accountList.bind('<<ListboxSelect>>', self.masterAccountListClicked)
        self.mainFrame.accountListFrame.accountList.grid(row = 1, column = 0, columnspan = 3)
        self.mainFrame.accountListFrame.grid(row = 0, column = 0, rowspan = 2)
              

        #First Name
        self.mainFrame.accountListFrame.firstNameLabel = tkinter.Label(self.mainFrame.accountListFrame, text = "First Name:")
        self.mainFrame.accountListFrame.firstNameLabel.grid(row = 2, column = 0, sticky = "E")
        self.mainFrame.accountListFrame.firstNameTextField = tkinter.Text(self.mainFrame.accountListFrame, height = 1, width = 20)
        self.mainFrame.accountListFrame.firstNameTextField.grid(row = 2, column = 1, sticky = "WE")

        #Last Name
        self.mainFrame.accountListFrame.lastNameLabel = tkinter.Label(self.mainFrame.accountListFrame, text = "Last Name:")
        self.mainFrame.accountListFrame.lastNameLabel.grid(row = 3, column = 0, sticky = "E")
        self.mainFrame.accountListFrame.lastNameTextField = tkinter.Text(self.mainFrame.accountListFrame, height = 1, width = 20)
        self.mainFrame.accountListFrame.lastNameTextField.grid(row = 3, column = 1, sticky = "WE")

        #Account Number
        self.mainFrame.accountListFrame.accountNumLabel = tkinter.Label(self.mainFrame.accountListFrame, text = "Account Number:")
        self.mainFrame.accountListFrame.accountNumLabel.grid(row = 4, column = 0, sticky = "E")
        self.mainFrame.accountListFrame.accountNumTextField = tkinter.Text(self.mainFrame.accountListFrame, height = 1, width = 10)
        self.mainFrame.accountListFrame.accountNumTextField.grid(row = 4, column = 1, sticky = "WE")
        
        self.mainFrame.accountListFrame.clearFilterButton = tkinter.Button(self.mainFrame.accountListFrame, text = "Clear Search Filters", command = self.clearSearchFilters)
        self.mainFrame.accountListFrame.newSearchButton = tkinter.Button(self.mainFrame.accountListFrame, text = "Search", command = self.accountNumSearch)
        self.mainFrame.accountListFrame.newSearchButton.grid(row = 4, column = 2, sticky = "w")
        self.mainFrame.accountListFrame.newfirstSearchButton = tkinter.Button(self.mainFrame.accountListFrame, text = "Search", command = self.firstNameSearch)
        self.mainFrame.accountListFrame.newfirstSearchButton.grid(row = 2, column = 2, sticky = "w")
        self.mainFrame.accountListFrame.newlastSearchButton = tkinter.Button(self.mainFrame.accountListFrame, text = "Search", command = self.lastNameSearch)
        self.mainFrame.accountListFrame.newlastSearchButton.grid(row = 3, column = 2, sticky = "w")
        self.mainFrame.accountListFrame.clearFilterButton.grid(row = 5, column = 0, columnspan = 3)

        #Account Detail Frame
        self.mainFrame.accountDetailFrame = tkinter.LabelFrame(self.mainFrame, text = "Account Details")

        #First Name
        self.mainFrame.accountDetailFrame.firstNameLabel = tkinter.Label(self.mainFrame.accountDetailFrame, text = "First Name:")
        self.mainFrame.accountDetailFrame.firstNameLabel.grid(row = 1, column = 0, sticky = "E")
        self.mainFrame.accountDetailFrame.firstNameTextField = tkinter.Text(self.mainFrame.accountDetailFrame, height = 1, width = 20)
        self.mainFrame.accountDetailFrame.firstNameTextField.grid(row = 1, column = 1, sticky = "WE")

        #Last Name
        self.mainFrame.accountDetailFrame.lastNameLabel = tkinter.Label(self.mainFrame.accountDetailFrame, text = "Last Name:")
        self.mainFrame.accountDetailFrame.lastNameLabel.grid(row = 2, column = 0, sticky = "E")
        self.mainFrame.accountDetailFrame.lastNameTextField = tkinter.Text(self.mainFrame.accountDetailFrame, height = 1, width = 20)
        self.mainFrame.accountDetailFrame.lastNameTextField.grid(row = 2, column = 1, sticky = "WE")

        #Account Number
        self.mainFrame.accountDetailFrame.accountNumLabel = tkinter.Label(self.mainFrame.accountDetailFrame, text = "Account Number:")
        self.mainFrame.accountDetailFrame.accountNumLabel.grid(row = 0, column = 0, sticky = "E")
        self.mainFrame.accountDetailFrame.accountNumTextField = tkinter.Text(self.mainFrame.accountDetailFrame, height = 1, width = 10)
        self.mainFrame.accountDetailFrame.accountNumTextField.grid(row = 0, column = 1, sticky = "WE")

        #Balance
        self.mainFrame.accountDetailFrame.accountBalanceLabel = tkinter.Label(self.mainFrame.accountDetailFrame, text = "Balance:")
        self.mainFrame.accountDetailFrame.accountBalanceLabel.grid(row = 3, column = 0, sticky = "E")
        self.mainFrame.accountDetailFrame.accountBalanceVariable = tkinter.StringVar()
        self.mainFrame.accountDetailFrame.accountBalanceVariable.set("$0.00")
        self.mainFrame.accountDetailFrame.accountBalanceDisplayLabel = tkinter.Label(self.mainFrame.accountDetailFrame, textvar = self.mainFrame.accountDetailFrame.accountBalanceVariable)
        self.mainFrame.accountDetailFrame.accountBalanceDisplayLabel.grid(row = 3, column = 1, sticky = "WE")

        self.mainFrame.accountDetailFrame.grid(row = 0, column = 1)

        #Control Frame
        self.mainFrame.controlFrame = tkinter.LabelFrame(self.mainFrame, text = "Control Panel")
        self.mainFrame.controlFrame.newAccountButton = tkinter.Button(self.mainFrame.controlFrame, text = "New", command = self.newAccount)
        self.mainFrame.controlFrame.newAccountButton.grid(row = 0, column = 0, sticky = "WE")
        self.mainFrame.controlFrame.newPaymentButton = tkinter.Button(self.mainFrame.controlFrame,text = "Apply Payment", command = self.applyPayment)
        self.mainFrame.controlFrame.newPaymentButton.grid(row = 1, column = 0, sticky = "WE")



        self.mainFrame.controlFrame.grid(row = 1, column = 1, sticky = "NEWS")


        #Put Main Grid On Screen
        self.mainFrame.grid(row = 0, column = 0)
        self.grid(row = 0, column = 0)

        #Autoconnect
        #self.fileName = filedialog.askopenfilename(filetypes = (('SQL3LITE Database files', '*.sq3'),('All Files', '*.*') ) )
        self.fileName = '/home/pi/accounts.sq3'
        print(self.fileName)
        self.conn = sqlite3.connect(self.fileName)
        self.cursor = self.conn.cursor()

        self.updateMasterList()

    def connectDatabase(self):

        #Query File Selection and Connect to Seleted Database
        self.fileName = filedialog.askopenfilename(filetypes = (('SQL3LITE Database files', '*.sq3'),('All Files', '*.*') ) )
        print(self.fileName)
        self.conn = sqlite3.connect(self.fileName)
        self.cursor = self.conn.cursor()

        self.updateMasterList()


    def updateMasterList(self):

        #Populate Master Account List

        #Clear Out Whats In There
        self.mainFrame.accountListFrame.accountList.delete(0, tkinter.END)
        
        self.rows = self.cursor.execute("SELECT * FROM CUSTOMER")
        self.rows = [row for row in self.rows]
        #print(self.rows)
        self.curID = len(self.rows)
        #print('real size:', self.curID)
        
        for eachRecord in self.rows:
            #print(eachRecord)
            recordString = ""
            
            for eachEntry in eachRecord:
                print(eachEntry)
                recordString = recordString + str(eachEntry) + " | "
        
            print(recordString)
            self.mainFrame.accountListFrame.accountList.insert(0, recordString)

    def masterAccountListClicked(self, e):
        
        try:
            print("Listbox Clicked!")
            clickedRecordNumber = self.mainFrame.accountListFrame.accountList.curselection()[0]
            #print(type(clickedRecordNumber))
            selectedString = self.mainFrame.accountListFrame.accountList.get(clickedRecordNumber)
            recordValues = selectedString.split(" | ")
        
            print("Database Record Number:", recordValues[0])
            databaseRecord = self.cursor.execute("SELECT * FROM CUSTOMER WHERE id = ?", (recordValues[0],) )
            rows = self.cursor.fetchall()
            #print(rows)

            self.mainFrame.accountDetailFrame.firstNameTextField.delete('1.0', tkinter.END)
            self.mainFrame.accountDetailFrame.firstNameTextField.insert('1.0', rows[0][1])

            self.mainFrame.accountDetailFrame.lastNameTextField.delete('1.0', tkinter.END)
            self.mainFrame.accountDetailFrame.lastNameTextField.insert('1.0', rows[0][2])

            self.mainFrame.accountDetailFrame.accountNumTextField.config(state = tkinter.NORMAL)
            self.mainFrame.accountDetailFrame.accountNumTextField.delete('1.0', tkinter.END)
            self.mainFrame.accountDetailFrame.accountNumTextField.insert('1.0', rows[0][3])
            self.mainFrame.accountDetailFrame.accountNumTextField.config(state = tkinter.DISABLED)

            self.mainFrame.accountDetailFrame.accountBalanceVariable.set(rows[0][4])

        except Exception as e:
            print(e)

            #Payment Section 

    def applyPayment(self):

        
        try:
            print("Listbox Clicked!")
            clickedRecordNumber = self.mainFrame.accountListFrame.accountList.curselection()[0]
            print(type(clickedRecordNumber))
            selectedString = self.mainFrame.accountListFrame.accountList.get(clickedRecordNumber)
            recordValues = selectedString.split(" | ")
        
            print("Database Record Number:", recordValues[0])
            databaseRecord = self.cursor.execute("SELECT * FROM CUSTOMER WHERE id = ?", recordValues[0])
            rows = self.cursor.fetchall()
            print(rows)

            self.paymentWindow = tkinter.Toplevel()

            self.paymentWindow.accountNum = rows[0][3]
            self.paymentWindow.accountBalance = float(rows[0][4])
            self.paymentWindow.accountCID = rows[0][0]
            self.accountPaymentLabelframeText = 'Apply Payment to Account#:' + str(self.paymentWindow.accountNum)
            self.paymentWindow.paymentFrame = tkinter.LabelFrame(self.paymentWindow, text = self.accountPaymentLabelframeText)
            self.paymentWindow.paymentFrame.grid(row = 0, column = 0)

            self.paymentWindow.paymentFrame.paymentLabel = tkinter.Label(self.paymentWindow.paymentFrame, text = 'Payment Amount:')
            self.paymentWindow.paymentFrame.paymentLabel.grid(row = 0, column = 0, sticky = 'e')

            self.paymentWindow.paymentFrame.paymentText = tkinter.Text(self.paymentWindow.paymentFrame, width = 10, height = 1)
            self.paymentWindow.paymentFrame.paymentText.grid(row = 0, column = 1, sticky = 'w')

            self.paymentWindow.paymentFrame.submitButton = tkinter.Button(self.paymentWindow.paymentFrame, text = 'Submit', command = self.applyPamentSubmission)
            self.paymentWindow.paymentFrame.cancelButton = tkinter.Button(self.paymentWindow.paymentFrame, text = 'Cancel', command = self.paymentWindow.destroy)
            self.paymentWindow.paymentFrame.submitButton.grid(row = 1, column = 0, sticky = 'e')
            self.paymentWindow.paymentFrame.cancelButton.grid(row = 1, column = 1, sticky = 'w')
            
            
            
            self.paymentWindow.wm_title('Apply Payment')

        except Exception as e:
            print(e)

    def applyPamentSubmission(self):
        
        #Execute Payment Validation
        try:

            paymentFloatValue = float(self.paymentWindow.paymentFrame.paymentText.get("1.0", tkinter.END))
            print("Float Payment Value is ", paymentFloatValue)

        except Exception as e:
            messagebox.showwarning('Data Validation Error:','Invalid Payment Data Entered!')
            
            print(e)

        #Payment Submission Confirmation Check
        print("ARE YOU SURE!?")
        oldBal = self.paymentWindow.accountBalance
        newBal = oldBal - paymentFloatValue
        confirmationQuery = 'Are you sure you want to apply a payment of $' + str(paymentFloatValue) + ' to account ' + str(self.paymentWindow.accountNum) + '?\nNew Balance will be ' +str(newBal)
        
        confirmationQuestion = messagebox.askyesno('Confirmation', confirmationQuery)
        print(confirmationQuestion)
        if(confirmationQuestion == True):
            print('Applying payment!')
            self.cursor.execute('''UPDATE CUSTOMER SET balance = ? where id = ?''', (newBal, self.paymentWindow.accountCID))
            print('Update Applied')
            self.conn.commit()
            self.paymentWindow.destroy()
            self.updateMasterList()


    def newAccount(self):

        self.newAccountWindow = tkinter.Toplevel()
        self.newAccountWindow.wm_title('New Account')

        self.newAccountWindow.newAccountFrame = tkinter.LabelFrame(self.newAccountWindow, text = 'Add New Account to the Database:')
        self.newAccountWindow.newAccountFrame.grid(row = 0, column = 0)

        #First Name
        self.newAccountWindow.newAccountFrame.firstNameLabel = tkinter.Label(self.newAccountWindow.newAccountFrame, text = "First Name:")
        self.newAccountWindow.newAccountFrame.firstNameLabel.grid(row = 1, column = 0, sticky = "E")
        self.newAccountWindow.newAccountFrame.firstNameTextField = tkinter.Text(self.newAccountWindow.newAccountFrame, height = 1, width = 20)
        self.newAccountWindow.newAccountFrame.firstNameTextField.grid(row = 1, column = 1, sticky = "WE")

        #Last Name
        
        self.newAccountWindow.newAccountFrame.lastNameLabel = tkinter.Label(self.newAccountWindow.newAccountFrame, text = "Last Name:")
        self.newAccountWindow.newAccountFrame.lastNameLabel.grid(row = 2, column = 0, sticky = "E")
        self.newAccountWindow.newAccountFrame.lastNameTextField = tkinter.Text(self.newAccountWindow.newAccountFrame, height = 1, width = 20)
        self.newAccountWindow.newAccountFrame.lastNameTextField.grid(row = 2, column = 1, sticky = "WE")

        #Account Number
        self.newAccountWindow.newAccountFrame.NumLabel = tkinter.Label(self.newAccountWindow.newAccountFrame, text = "Account Number:")
        self.newAccountWindow.newAccountFrame.NumLabel.grid(row = 0, column = 0, sticky = "E")
        self.newAccountWindow.newAccountFrame.NumTextField = tkinter.Text(self.newAccountWindow.newAccountFrame, height = 1, width = 10)
        self.newAccountWindow.newAccountFrame.NumTextField.grid(row = 0, column = 1, sticky = "WE")

        #Balance
        self.newAccountWindow.newAccountFrame.accountBalanceLabel = tkinter.Label(self.newAccountWindow.newAccountFrame, text = "Balance:")
        self.newAccountWindow.newAccountFrame.accountBalanceLabel.grid(row = 3, column = 0, sticky = "E")
        self.newAccountWindow.newAccountFrame.accountBalanceTextField = tkinter.Text(self.newAccountWindow.newAccountFrame, height = 1, width = 10)
        self.newAccountWindow.newAccountFrame.accountBalanceTextField.grid(row = 3, column = 1, sticky = "WE")

        self.newAccountWindow.newAccountFrame.submitButton = tkinter.Button(self.newAccountWindow.newAccountFrame, text = 'Submit', command = self.newAccountSubmission)
        self.newAccountWindow.newAccountFrame.cancelButton = tkinter.Button(self.newAccountWindow.newAccountFrame, text = 'Cancel', command = self.newAccountWindow.destroy)
        self.newAccountWindow.newAccountFrame.submitButton.grid(row = 4, column = 0, sticky = 'E')
        self.newAccountWindow.newAccountFrame.cancelButton.grid(row = 4, column = 1, sticky = 'W')

    def newAccountSubmission(self):
        #Validation

        #Do Check if Sure
        confirmationCheck = messagebox.askyesno("Confirmation","Are you sure you want to add new account to database?")
        if confirmationCheck != True:
            return
    
        #Check if Data is Valid
        #Scrape Field Data
        firstName = self.newAccountWindow.newAccountFrame.firstNameTextField.get("1.0", tkinter.END).rstrip()
        lastName = self.newAccountWindow.newAccountFrame.lastNameTextField.get("1.0", tkinter.END).rstrip()
        accountNumber = self.newAccountWindow.newAccountFrame.NumTextField.get("1.0", tkinter.END)
        accountBalance = self.newAccountWindow.newAccountFrame.accountBalanceTextField.get("1.0", tkinter.END)

        print("New Name:", firstName, lastName)
        print("Acct #:", accountNumber)
        print("Balance:", accountBalance)

        #Double check to make sure the account number is an integer 
        try:
            
            accountNumInt = int(accountNumber)
        except Exception as e:
            print(e)
            messagebox.showwarning("Error", "Invaild account number detected!")
            return
        #Turning account Balance into a float

        try:
            accountBalanceF = float(accountBalance)
        except Exception as e:
            print(e)
            messagebox.showwarning("Error", "Invaild balance detected!")
            return

        #Check For Redundant Account Number Error
        accountNumberData = self.cursor.execute('''SELECT accountNumber from customer''')
        accountDataRows = [row for row in accountNumberData]
        #print("Account Data:",accountDataRows)

        for accountNum in accountDataRows:
            print(accountNum[0])
            if accountNum[0] == int(accountNumber):
                print("DUPE!")
                messagebox.showwarning("Error", "Account Number Already Exists!")
                return
        
        #Commit Change to DB
        self.cursor.execute('''INSERT into CUSTOMER(firstName, lastName, accountNumber, balance) VALUES (?, ?, ?, ?)''', (firstName, lastName, accountNumInt, accountBalanceF))
        self.conn.commit()
        self.newAccountWindow.destroy()
        self.updateMasterList()

        #Search Function

    def firstNameSearch(self):
        self.mainFrame.accountListFrame.accountList.delete(0, tkinter.END)
        firstName = self.mainFrame.accountListFrame.firstNameTextField.get("1.0", tkinter.END).rstrip()
        self.rows = self.cursor.execute('''SELECT * FROM CUSTOMER WHERE firstName = ?''',(firstName, ))
        self.rows = [row for row in self.rows]
        #print(self.rows)
        self.curID = len(self.rows)
        #print('real size:', self.curID)
        
        for eachRecord in self.rows:
            #print(eachRecord)
            recordString = ""
            
            for eachEntry in eachRecord:
                print(eachEntry)
                recordString = recordString + str(eachEntry) + " | "
        
            print(recordString)
            self.mainFrame.accountListFrame.accountList.insert(0, recordString)
        
    def lastNameSearch(self):
        self.mainFrame.accountListFrame.accountList.delete(0, tkinter.END)
        lastName = self.mainFrame.accountListFrame.lastNameTextField.get("1.0", tkinter.END).rstrip()
        self.rows = self.cursor.execute('''SELECT * FROM CUSTOMER WHERE lastName = ?''',(lastName, ))
        self.rows = [row for row in self.rows]
        #print(self.rows)
        self.curID = len(self.rows)
        #print('real size:', self.curID)
        
        for eachRecord in self.rows:
            #print(eachRecord)
            recordString = ""
            
            for eachEntry in eachRecord:
                print(eachEntry)
                recordString = recordString + str(eachEntry) + " | "
        
            print(recordString)
            self.mainFrame.accountListFrame.accountList.insert(0, recordString)

    def accountNumSearch(self):
        self.mainFrame.accountListFrame.accountList.delete(0, tkinter.END)
        accountNum = self.mainFrame.accountListFrame.accountNumTextField.get("1.0", tkinter.END).rstrip()
        self.rows = self.cursor.execute('''SELECT * FROM CUSTOMER WHERE accountNumber = ?''',(accountNum, ))
        self.rows = [row for row in self.rows]
        #print(self.rows)
        self.curID = len(self.rows)
        #print('real size:', self.curID)
        
        for eachRecord in self.rows:
            #print(eachRecord)
            recordString = ""
            
            for eachEntry in eachRecord:
                print(eachEntry)
                recordString = recordString + str(eachEntry) + " | "
        
            print(recordString)
            self.mainFrame.accountListFrame.accountList.insert(0, recordString)

    def clearSearchFilters(self):
        #Clears Out Search Parameters from Account List Frame
        self.mainFrame.accountListFrame.lastNameTextField.delete('1.0', tkinter.END)
        self.mainFrame.accountListFrame.firstNameTextField.delete('1.0', tkinter.END)
        self.mainFrame.accountListFrame.accountNumTextField.delete('1.0', tkinter.END)
        self.updateMasterList()
        

newWindow = tkinter.Tk()

accountingWindow(newWindow)
newWindow.wm_title("Accounts Software v0.01")
