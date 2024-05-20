iptables -t nat -A OUTPUT -m owner --uid-owner debian-tor -j RETURN
iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 53
iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports 9040

# Permitir tráfico de Tor
iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m owner --uid-owner debian-tor -j ACCEPT
iptables -A OUTPUT -j REJECT
