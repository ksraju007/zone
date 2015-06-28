#Basic DHCP and DNS Server on CentOS 7

This set of configuration files allows you to configure a basic DHCP and DNS server in CentOS 7. It assumes that your server is having IP 10.0.0.1 and your network is 10.0.0.0/24. If it is different, tweak the files before copying. DHCP server also has two machines with fixed IPs , server and client. These are also added in DNS to have names resolved to their IPs.

Checkout this into a temporary folder, and run these commands to get started. 

###Optional NAT
If you would like to allow machines in 10.0.0.0/24 access internet, add another network card for the DNS server which is connected directly to internet. 

Advice for virtual box user, please use internal network option for 10.0.0.0/24 NIC and Bridge/NAT for public NIC.

###Commands
```shell
yum install bind bind-utils net-tools dhcp
cp dhcpd.conf /etc/dhcp/
cp named.conf /etc/
cp example.com.* /var/named/
systemctl enable named.service
systemctl restart named.service
systemctl enable dhcpd.service
systemctl restart dhcpd.service
firewall-cmd --permanent --add-port=53/udp
firewall-cmd --permanent --add-port=53/tcp
firewall-cmd reload
```
###Optional NAT for LAN machines
```shell
firewall-cmd --add-masquerade --permanent
firewall-cmd reload
```

Hope it makes your life easier. 
