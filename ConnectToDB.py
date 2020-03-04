import pyodbc
import os
import argparse
import logging
import logging.handlers as handlers
import re


# Configure Logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

# Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logHandler = handlers.TimedRotatingFileHandler('./Logs/smtp_app.log', when='midnight', interval=1, backupCount=2)
logHandler.setLevel(logging.INFO)

logHandler.suffix = "%Y%m%d"

#need to change the extMatch variable to match the suffix for it
logHandler.extMatch = re.compile(r"^\d{8}$")

# Here we set our logHandler's formatter
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)


##Command Line Args
parser = argparse.ArgumentParser(description='Execute SMTP Server')
parser.add_argument("-g", type=int, required=True, dest='groupID', help='Group ID for a group')
parser.add_argument("-q", "--quantity", type=int, dest="quantity", help="Number of emails to be generated", metavar="n", default=1)
parser.add_argument("-s", type=str, required=True, dest="server", help='SMTP Server for Mail Exchange')

args = parser.parse_args()

groupID = args.groupID

# Server Details
ServerName = 'zdns_archive01.prf01.evc,21433'
Database = 'ArchiveDB'
PortNumber = 25025
SMTPServer = args.server

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

logger.info("Group ID: " + str(groupID))
logger.info("Journal Address: " + str(journalAddress))
logger.info("Server: " + str(ServerName))
logger.info("Database: " + str(Database))
logger.info("SMTPServer: " + str(SMTPServer))

print("\n\n\n\n")

cursor = connec.cursor()
cursor.execute(queryAccounts)

# Write usernames to a file
f = open('./Content/SMTPemailaddresses_' + str(groupID) + '.txt', 'w', encoding='utf8')
for row in cursor:
    f.write(row[0] + '\n')


logger.info("Executing query: " + 'python SMTPTool.py -v -m "" "' + journalAddress + '" "' + SMTPServer + '" -n ' + str(PortNumber)+ ' -q ' + str(args.quantity) + ' -f ' +  './Content/SMTPemailaddresses_' + str(groupID) + '.txt')

# Start sending mails
os.system('python SMTPTool.py -v -m "" "' + journalAddress + '" "' + SMTPServer + '" -n ' + str(PortNumber)+ ' -q ' + str(args.quantity) + ' -f ' +  './Content/SMTPemailaddresses_' + str(groupID) + '.txt')