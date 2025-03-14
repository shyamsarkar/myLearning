# Check if username is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

USERNAME=$1

# Check if the user exists in the index.txt file
if ! grep -q "^R.*$USERNAME\|^V.*$USERNAME" /etc/openvpn/easy-rsa/pki/index.txt; then
    echo "User $USERNAME not found!"
    exit 1
fi

# Revoke the user certificate
cd /etc/openvpn/easy-rsa/ || exit 1
./easyrsa --batch revoke "$USERNAME"
EASYRSA_CRL_DAYS=3650 ./easyrsa gen-crl
rm -f /etc/openvpn/crl.pem
cp /etc/openvpn/easy-rsa/pki/crl.pem /etc/openvpn/crl.pem
chmod 644 /etc/openvpn/crl.pem

# Delete user's .ovpn file
find /home/ -maxdepth 2 -name "$USERNAME.ovpn" -delete
rm -f "/root/$USERNAME.ovpn"

# Remove user from ipp.txt
sed -i "/^$USERNAME,.*/d" /etc/openvpn/ipp.txt

if [ -f "/etc/openvpn/easy-rsa/pki/reqs/$USERNAME.req" ] || \
   [ -f "/etc/openvpn/easy-rsa/pki/private/$USERNAME.key" ] || \
   [ -f "/etc/openvpn/easy-rsa/pki/issued/$USERNAME.crt" ]; then
    echo "Certificate, key, or CSR file exists for user $USERNAME. Skipping sed command."
else
    # Run sed command to remove user from EasyRSA index.txt
    sudo sed -i "/^R.*$USERNAME\|^V.*$USERNAME/d" /etc/openvpn/easy-rsa/pki/index.txt
fi

# Backup index.txt
cp /etc/openvpn/easy-rsa/pki/index.txt{,.bk}

echo ""
echo "Certificate for client $USERNAME revoked."

exit 0
