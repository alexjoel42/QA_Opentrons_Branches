#!/bin/bash

# Disable compliance-ready software.

die() {
    echo "Failed: ${1}"
    exit 1
}
# We need to ask for the password to disable the compliance-ready software.
echo -n 'Password: '
read -rs password

# This is using the "cat" command to read the serial number from the file "/var/serial".
# Note: We can simply edit the file to change the serial number. 
serial=$(cat /var/serial)
## This password should be same as the pin FLXA1020240402002-0000. 
[ "${password}" = "${serial}-0000" ] || die "Incorrect password"

echo "Exiting CRS"
# This is removing the compliance server 
rm -rf /var/lib/opentrons-auth-server
echo "Rebooting"
reboot