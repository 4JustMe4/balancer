#!/bin/sh

set -xue

sudo apt-get update
sudo apt-get install boinc-client boinc-manager

sudo systemctl start boinc-client
sudo usermod -a -G boinc $USER
sudo systemctl restart boinc-client
sudo usermod -a -G boinc $USER

URL=http://89.169.171.76/myboinc
EMAIL=$(hostname)@mail.com
PASSWORD=password
NAME=$(hostname)

# sudo systemctl status boinc-client
boinccmd --create_account $URL ${EMAIL} ${PASSWORD} ${NAME}
ACCOUNT_KEY=$(boinccmd --lookup_account ${URL} ${EMAIL} ${PASSWORD} ${NAME})
boinccmd --project_attach ${URL} ${ACCOUNT_KEY}
