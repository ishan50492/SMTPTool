# SMTPTool
A command-line based smtp client utility for email generation and email ingestion using random generated data based on Markov chain generator for building realistic/user-like data sets.

### SMTPTool Structure
```
SMTPTool
|    SMTPTool.py             - command-line interface for constructing and send emails
|    RandomEmailGenerator.py - generates random data for each email field
|    RandomTextGenerator.py  - generates sentences for email subject and body
|    email_object.py         - object for email structure
|    reading_file.py         - to read the text file used to generate text
|    readme.md
└───Content                  - directory for content that makes up generated emails
     |   Attachments/                   - directory with variety of files to use as email attachments
     |   Attachments_fr/                - directory with mix of French files to use as email attachments
     |   Attachments_de/                - directory with mix of German files to use as email attachments
     |   SMTPemailaddresses.txt         - contains list of email accounts to use for email sender and recipients fields to send emails via Mail Server
     |   Exchangeemailaddresses.text    - contains list of email accounts to use for email sender and recipients fields to send emails via Exchange Server
     |   news_articles.txt              - text document to use as model input for Markov chain to generate sentences
     |   Der Tod in Venedig.txt         - German text document for generating German content
     |   Le_Diable_au_corps.txt         - French text document for generating French context
```

Usage: SMTPTool.py [args] serveraddress

SMTPTool.py is the main script which is responsible for sending the data via the provided server

[args] contain all the different combinations of flags with their values

serveraddress is the address of either the SMTP or Mail Server

## Command line arguments
```
usage: SMTPTool.py [args] serveraddress

positional arguments:
  serveraddr            SMTP/Exchange Server

optional arguments:
  -h, --help                                            show this help message and exit
  -t, --usetls                                          Connect using TLS, default is false
  -s, --usessl                                          Connect using SSL, default is false
  -n nnn, --port nnn                                    SMTP server port
  -u username, --username username                      SMTP server auth username
  -p password, --password password                      SMTP server auth password
  -v, --verbose                                         Verbose message printing
  -l n, --debuglevel n                                  Set to 1 to print smtplib.send messages
  -q n, --quantity n                                    Number of emails to be generated
  -r, --dryrun                                          Execute script without sending email
  -i filepath, --jsoninput filepath                     Sends emails from json file
  -j, --jsonoutput                                      Copies emails to json file for email data ingestion
  -o filepath, --jsonoutputfile filepath                File path for emails copies to json file for email data ingestion
  -c n, --attachmentpercent n                           Int value for percentage of emails to include attachments
  -f filepath, --addressesfile filepath                 Email addresses to use for generated emails
  -a filepath, --attachmentsdir filepath                Attachments to use for generated emails
  -x filepath, --textmodelfile filepath                 Input text to use for generated subject and body of emails
  -d domainname, --domainname domainname                Adds/replaces domains of provided email addresses
  -m addresses addresses, --smtp addresses addresses    Use Mail Server for mail transfer
  -e, --exchange                                        Use Exchange for mail transfer
  -g language, --lang language                          language for generating body and subject of mail


```

### Remember
For [args], one out of -e or -m should be present. Rest all are optional.

### Command Examples
**Generate** and send one email to provided journal address and smtp host:<br />
Email addresses in case of smtp host will be read from SMTPemailaddresses.txt file
```sh
python SMTPTool.py -v -m "" "vttesting1217@journal.qa.archivecloud.net" "usw80cavsmtp01"
```

**Generate** and send one email to provided email address and exchange host:<br />
Email addresses in case of Exchange server will be read from Exchangeemailaddresses.txt file
```sh
python SMTPTool.py -v -e "usw81csv162ex01.162ex.local"
```

**Generate** 200 emails, send via Mail Server and create json output file with provided filename:
```sh
python SMTPTool.py -q 200 -j -o "50589_emails_200.json" -v -m "" "vttesting1217@journal.qa.archivecloud.net" "usw80cavsmtp01"
```

**Generate** 200 emails and create json output file without sending mails (dry run):
```sh
python SMTPTool.py -q 200 -j -r -v -m "" "vttesting1217@journal.qa.archivecloud.net" "usw80cavsmtp01"
```

**Generate** and send 500 emails via SMTP Server with provided SMTPemailaddresses.txt file:<br />
Since we are using Mail Server to send mails, this external file should contain SMTP Mail addresses
```sh
python SMTPTool.py -q 500 -f "./Content/testcompany_addresses.txt" -v -m "" "vttesting1217@journal.qa.archivecloud.net" "usw80cavsmtp01"
```

**Generate** and send 500 emails via Exchange with provided Exchangeemailaddresses.txt file:<br />
Since we are using Exchange to send mails, this external file should contain Exchange Mail addresses
```sh
python SMTPTool.py -q 500 -f "./Content/testcompany_addresses.txt" -v -m "" "vttesting1217@journal.qa.archivecloud.net" "usw80cavsmtp01"
```

**Generate** and send 500 emails via Exchange Server with provided emailaddresses file:
```sh
python SMTPTool.py -q 500 -f "./Content/testcompany_addresses.txt" -v -e "usw81csv162ex01.162ex.local"
```

**Generate** 500 emails with 30 percent of emails to have attachments, replace domain name of email addresses and send via Mail Server:
```sh
python SMTPTool.py -q 500 -c 30 -f "./Content/testcompany_addresses.txt" -d "testcompany2.com" -o "50540_emails_500.json" -v -m "" "testcompany2@journal.us80.archivecloud.net" "usw80cavsmtp01"
```

**Generate** 200 emails in French using the users/accounts we’ve created for the group with 30% of the emails with French attachments and output to a json file for ingestion:
```sh
python SMTPTool.py -q 200 -c 30 -j -o "50599_emails_200.json" -f "./Content/50599_addresses.txt" -a "./Content/Attachments_fr/" -x "./Content/Le_Diable_au_corps.txt" -m "" "es6french@journal.us80.archivecloud.net" "usw80cavsmtp01"
```

**Ingest** emails from json file and send:
```sh
python SMTPTool.py -i "50589_emails_200.json" -v -m "" "testcompany@journal.us80.archivecloud.net" "usw80cavsmtp01"
```

**Ingest** emails from json file, replacing the domain name of the email addresses in the json payloads and send:
```sh
python SMTPTool.py -i "50540_emails_500.json" -d "companytest.com" -v -m "" "companytest@journal.us80.archivecloud.net" "usw80cavsmtp01"
```

**Ingest** emails from json file with different directory source for attachments
```sh
python SMTPTool.py -v -i "50599_emails_200.json" -a "./Content/Attachments_fr/" -m "" "es6french@journal.us80.archivecloud.net" "usw80cavsmtp01"
```

**Generate** and send emails using SMTP Mail Server and setting the debug output level to 1<br />
A true value for level results in debug messages for connection and for all messages sent to and received from the server
```sh
python SMTPTool.py -v -l 1 -m "" "es6french@journal.us80.archivecloud.net" "usw80cavsmtp01"
```

**Ingest** emails from json file using Mail Server in the japanese language<br />
Currently, the language flag has been configured for the following languages: English(by default), Japanese, French, German
```sh
python SMTPTool.py -v -i "50589_emails_200.json" -m "" "vttesting1217@journal.qa.archivecloud.net" -g "japanese" "usw80cavsmtp01"
```

### Future Work

- Based upon the number of emails to be generated, a text file containing random words with random characters will be generated, which will be used to generate subject and body of mails

### Deploying SMTPTool (requires Python 3.6.x) dependencies:

   - Install python
   - copy files to destination folder
   - cd to destination folder
   - pip install markovify
   - pip install textblob
   - pip install tzlocal
```

Check Package installations by executing

python ConnectToDB.py -g 50064 -s "prf01cavsmtp01" -q 1
```
Or deploy into a virtualenv
https://docs.python-guide.org/dev/virtualenvs/


### Connect to the DB and send mails
     
Arguments

```
-h, --help                                             show this help message and exit
-g                                                     GroupID
-s                                                     SMTPServer to be used to exchange mail
-q                                                     Quantity of mails to be exchanged

python ConnectToDB.py -g 50064 -s "prf01cavsmtp01" -q 1
 ```
