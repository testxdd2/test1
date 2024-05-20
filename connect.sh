# Configurar el tráfico TCP para redirigirlo a Tor
sudo iptables -t nat -A OUTPUT -m owner --uid-owner <tu_usuario> -p tcp --syn -j REDIRECT --to-ports 9040

# Configurar el tráfico DNS para redirigirlo a Tor
sudo iptables -t nat -A OUTPUT -m owner --uid-owner <tu_usuario> -p udp --dport 53 -j REDIRECT --to-ports 5353

# Configurar la cadena OUTPUT para que no afecte al propio Tor
sudo iptables -t nat -A OUTPUT -m owner --uid-owner debian-tor -j RETURN
sudo iptables -t nat -A OUTPUT -p tcp --dport 9040 -j RETURN
sudo iptables -t nat -A OUTPUT -p udp --dport 5353 -j RETURN
