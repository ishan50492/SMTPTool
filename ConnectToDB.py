import pyodbc
import os
import argparse


parser = argparse.ArgumentParser(description='Execute SMTP Server')
parser.add_argument("-g", type=int, required=True, dest='groupID', help='Group ID for a group')
parser.add_argument("-q", "--quantity", type=int, dest="quantity", help="Number of emails to be generated", metavar="n", default=1)
args = parser.parse_args()

groupID = args.groupID


# Server Details
ServerName = 'zdns_archive01.prf01.evc,21433'
Database = 'ArchiveDB'
SMTPServer = "prf01cavsmtp01"

# Queries
queryAccounts= "SELECT UserName FROM Acct WHERE GrouPID = " + str(groupID) + " and IsArchive = 1 and IsActive = 1 and RoleID = 1 and FName NOT LIKE '%Unassigned%'"
queryJournalAddress = "SELECT Address FROM JournalAddress WHERE GroupID = " + str(groupID) + " and IsActive = 1"


connec = pyodbc.connect('Driver={SQL Server};'
                      'Server=' + ServerName + ';'
                      'Database=' + Database + ';'
                      'Trusted_Connection=yes;')

cursor = connec.cursor()
cursor.execute(queryJournalAddress)

journalAddress = ''
for row in cursor:
    journalAddress = row[0]

# Print details
print("GroupID: ", groupID)
print("Journal Address: ", journalAddress)
print("Server: ", ServerName)
print("Database: ", Database)
print("SMTPServer: ", SMTPServer)

print("\n\n\n\n")

cursor = connec.cursor()
cursor.execute(queryAccounts)

# Write usernames to a file
f = open('./Content/SMTPemailaddresses.txt', 'w', encoding='utf8')
for row in cursor:
    f.write(row[0] + '\n')


# Start sending mails
os.system('python SMTPTool.py -v -m "" "' + journalAddress + '" "' + SMTPServer + '" -n 25025 -q ' + str(args.quantity))