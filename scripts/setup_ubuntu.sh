#!/bin/sh

set -xue

sudo apt-get update
sudo apt-get install boinc-client boinc-manager

sudo systemctl start boinc-client
sudo usermod -a -G boinc $USER
sudo systemctl restart boinc-client

URL=http://89.169.171.76/myboinc
EMAIL=$(hostname)@mail.com
PASSWORD=password
NAME=$(hostname)

# sudo systemctl status boinc-client
sudo boinccmd --create_account $URL ${EMAIL} ${PASSWORD} ${NAME}
ACCOUNT_KEY=$(sudo boinccmd --lookup_account ${URL} ${EMAIL} ${PASSWORD} ${NAME})
sudo boinccmd --project_attach ${URL} ${ACCOUNT_KEY}
