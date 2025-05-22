#!/bin/sh

set -xue

sudo apt-get update
echo 'Y' | sudo apt-get install boinc-client boinc-manager

sudo systemctl start boinc-client
sudo usermod -a -G boinc $USER
sudo systemctl restart boinc-client

export URL=http://89.169.171.76/myboinc
export EMAIL=$(hostname)-retry@mail.com
export PASSWORD=password
export NAME=$(hostname)-retry

# waiting for local boinc
sudo boinccmd --create_account ${URL} ${EMAIL} ${PASSWORD} ${NAME} || sleep 10 && sudo boinccmd --create_account ${URL} ${EMAIL} ${PASSWORD} ${NAME}
export ACCOUNT_KEY=$(boinccmd --lookup_account ${URL} ${EMAIL} ${PASSWORD} ${NAME} | grep -oP 'account key: \K.*')
sudo boinccmd --project_attach ${URL} ${ACCOUNT_KEY}
