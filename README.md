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
