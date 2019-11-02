# DAPNagios

## Reason
The main reason for this script is the fact I've noticed there wasn't any decent, easy way to push out pager messages via DAPNET using Nagios. Therefore I've written a short Python script which:
- connects to DAPNET via the REST API
- has its main configuration in a separate file
- gets its content via arguments
- has the ability to log for troubleshooting

Although this script has been written for the sake of Nagios it can be used for any CLI application in conjunction with DAPNET.

## Dependencies
- Python 3.x
- modules configparser, argparse

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
 
```
python3 DAPNagios.py -r pa0abc -t pa-all -m "Testmessage via DAPNET"
```

