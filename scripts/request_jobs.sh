#!/bin/sh

set -xue

for host in $(cat hosts.txt); do
    ssh ${host} "boinccmd --project http://89.169.171.76/myboinc update"
done

boinccmd --project http://89.169.171.76/myboinc update
