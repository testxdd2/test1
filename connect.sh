iptables -A OUTPUT -p tcp --dport 9050 -j ACCEPT
iptables -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-ports 9050
