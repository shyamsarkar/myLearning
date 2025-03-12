#!/bin/bash

INDEX_FILE="/etc/openvpn/easy-rsa/pki/index.txt"
#LINES_TO_PROCESS=3  # Change this to the desired number of lines

echo "test"

# Check if the file exists
if [ ! -f "$INDEX_FILE" ]; then
    echo "Error: $INDEX_FILE not found!"
    exit 1
fi

# Counter to keep track of processed lines
#counter=0

while IFS= read -r LINE; do
    USERNAME=$(echo "$LINE" | awk -F'[/=]' '{print $NF}')
    echo "Processing user: $USERNAME"

    #if [ -n "$USERNAME" ]; then
    # Revoke the user certificate
    #cd /etc/openvpn/easy-rsa/ || exit 1
    #./easyrsa --batch revoke "$USERNAME"
    #EASYRSA_CRL_DAYS=3650 ./easyrsa gen-crl
    #rm -f /etc/openvpn/crl.pem
    #cp /etc/openvpn/easy-rsa/pki/crl.pem /etc/openvpn/crl.pem
    #chmod 644 /etc/openvpn/crl.pem

    # Delete user's .ovpn file
    #find /home/ -maxdepth 2 -name "$USERNAME.ovpn" -delete
    #rm -f "/root/$USERNAME.ovpn"

    # Remove user from ipp.txt
    #sed -i "/^$USERNAME,.*/d" /etc/openvpn/ipp.txt

    # Remove user from EasyRSA index.txt
    #sudo sed -i "/^R.*$USERNAME\|^V.*$USERNAME/d" /etc/openvpn/easy-rsa/pki/index.txt

    # Backup index.txt
    #cp /etc/openvpn/easy-rsa/pki/index.txt{,.bk}

    #echo ""
    #echo "Certificate for client $USERNAME revoked."

    #exit 0
    #else
     #   echo "Skipping processing for empty username."
    #fi

    # Increment the counter
    #((counter++))

    # Check if we reached the desired number of lines
    #if [ "$counter" -eq "$LINES_TO_PROCESS" ]; then
     #   break
    #fi
done < "$INDEX_FILE"
