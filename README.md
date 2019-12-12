# DAPNagios

## Reason
The main reason for this script is the fact I've noticed there wasn't any decent, easy way to push out pager messages via DAPNET using Nagios. Therefore I've written a short Python script which:
- connects to DAPNET via the REST API
- has its main configuration in a separate file
- gets its content via arguments
- has the ability to log for troubleshooting

Although this script has been written for the sake of Nagios it can be used for any CLI application in conjunction with DAPNET.

## Word of caution!
Sending automated messages via the CLI should be well evaluated as it can cause a flood of unwanted data if a process gets out of control. If you are automating transmission of DAPNET messages please:
- always choose the smallest possible TX group (it doesn't make sense to send messages for a local public via all transmitters on all continents);
- have a safety catch: 
  - transmissing should be hold back in case any error in your script has occurred;
  - limit the number of sent messages over time;
  - don't loop based on the answer of the API (if sending fails something is wrong in your settings, so don't loop).

## Dependencies
- Python 3.x
- modules configparser, argparse, logging, requests, json, sys

## Installation
Clone the repository to your local disk
```
git clone https://github.com/pe2kmv/DAPNagios.git
```
Copy 'DAPNagios.py' and 'functions.py' to /usr/local/bin
```
sudo cp ~/DAPNagios/*.py /usr/local/bin
```
Create a copy of the default configuration in /usr/local/etc
```
sudo cp ~/DAPNagios/DAPNagios.config /usr/local/etc/DAPNagios.cfg
```
Change the settings in /usr/local/etc/DAPNagios.cfg to match your needs. It's mandatory to add your DAPNET username and password. This should be the DAPNET account login, not the transmitter login! Raise a ticket for the DAPNET support team to obtain a login if you don't already have one (logins are limited to licensed radio amateurs).
```
sudo nano /usr/local/etc/DAPNagios.cfg
```
Also adjust the settings for logging:
- log_path: this is the absolute path to your log file
- log_level: what kind of issues are to be logged:
  - 1: DEBUG - most details are logged, good for troubleshooting
  - 2: INFO - some lines can be logged as FYI
  - 3: WARNING - this logs topics which can be of (future) importance
  - 4: ERROR - errors are to be logged
  - 5: CRITICAL - only critical errors are logged
- log_on: 'yes' or 'no'. 'yes' logging function is enabled, 'no' logging function is disabled  

Initiate the log file (default as /var/log/DAPNagios.log). Make sure the path to the log file is set correctly as described above.
```
sudo touch /var/log/DAPNagios.log
sudo chmod 666 /var/log/DAPNagios.log
```

## Usage
Run the script with these attributes:
- -r --recepient [call sign]
- -t --txgroup [tx group as defined by DAPNET]
- -m --message "message to send, enclosed by quotes"

Messages can be sent to multiple recepients by comma separating the call signs and putting everything between quotes.
Transmission via multiple TX groups is possible by comma separating the TX groups and putting everything between quotes.

Examples:
```
python3 DAPNagios.py -r pa0abc -t pa-all -m "Testmessage via DAPNET"

python3 DAPNagios.py -r "pa0abc,pb1def" -t pa-all -m "Testmessage via DAPNET"

python3 DAPNagios.py -r pa0abc -t "pa-all,dl-nw" -m "Testmessage via DAPNET"

python3 DAPNagios.py -r "pa0abc,pb1def" -t "pa-all,dl_bw" -m "Testmessage via DAPNET"
```

