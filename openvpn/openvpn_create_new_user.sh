
echo ""
CLIENT=$1
echo $CLIENT
PASS=$2
echo $PASS
echo "Creating VPN configuration for username = $CLIENT"



CLIENTEXISTS=$(tail -n +2 /etc/openvpn/easy-rsa/pki/index.txt | grep -c -E "/CN=$CLIENT\$")
echo $CLIENTEXISTS
if [ $CLIENTEXISTS = '1' ]; then
	echo ""
	echo "The specified client CN was already found in easy-rsa, please choose another name."
	exit
else
	cd /etc/openvpn/easy-rsa/ || return
	./easyrsa --batch build-client-full "$CLIENT"

	# ;;
	# esac
	echo "Client $CLIENT added."
fi

# Home directory of the user, where the client configuration will be written
if [ -e "/home/${CLIENT}" ]; then
	# if $1 is a user name
	homeDir="/home/${CLIENT}"
elif [ "${SUDO_USER}" ]; then
	# if not, use SUDO_USER
	if [ "${SUDO_USER}" = "root" ]; then
		# If running sudo as root
		homeDir="/root"
	else
		homeDir="/home/${SUDO_USER}"
	fi
else
	# if not SUDO_USER, use /root
	homeDir="/root"
fi

# Determine if we use tls-auth or tls-crypt
if grep -qs "^tls-crypt" /etc/openvpn/server.conf; then
	TLS_SIG="1"
elif grep -qs "^tls-auth" /etc/openvpn/server.conf; then
	TLS_SIG="2"
fi

# Generates the custom client.ovpn
cp /etc/openvpn/client-template.txt "$homeDir/$CLIENT.ovpn"
{
	echo "<ca>"
	cat "/etc/openvpn/easy-rsa/pki/ca.crt"
	echo "</ca>"

	echo "<cert>"
	awk '/BEGIN/,/END CERTIFICATE/' "/etc/openvpn/easy-rsa/pki/issued/$CLIENT.crt"
	echo "</cert>"

	echo "<key>"
	cat "/etc/openvpn/easy-rsa/pki/private/$CLIENT.key"
	echo "</key>"

	case $TLS_SIG in
	1)
		echo "<tls-crypt>"
		cat /etc/openvpn/tls-crypt.key
		echo "</tls-crypt>"
		;;
	2)
		echo "key-direction 1"
		echo "<tls-auth>"
		cat /etc/openvpn/tls-auth.key
		echo "</tls-auth>"
		;;
	esac
	sed -i 's/^setenv opt block-outside-dns # Prevent Windows 10 DNS leak/#&/' "$homeDir/$CLIENT.ovpn"
} >>"$homeDir/$CLIENT.ovpn"

echo ""
echo "The configuration file has been written to $homeDir/$CLIENT.ovpn."
echo "Download the .ovpn file and import it in your OpenVPN client."

exit 0
