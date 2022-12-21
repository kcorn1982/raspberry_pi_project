# Local Network Setup

## Index

- [Setting up your network](#setting-up-your-network-for-a-static-ip)
  - [Finding your Mac address](#finding-your-mac-address)
  - [Setting up your dhcpcd.conf](#setting-up-your-dhcpcdconf)
  - [Setting up your router](#setting-up-your-router)

## Pre-requisites

The following steps take into account that:

- you are using a Linux or Mac - I'll look into windows instructions at a later date

- you have installed a desktop server such as Raspios (bullseye verions at the time of writing this guide) on a Raspberry Pi

- Have gone through the basic setup and have connected to the internet through WiFi or Ethernet

## Setting up your network for a static IP

I always set up static IP addresses to prevent any headaches from changing addresses form the DHCP if rebuilding Raspberry Pi's etc.

### Finding your Mac address

I always manually setup my router on a new build of a machine so first thing I do is get the mac address of the machine.

looking at you `ifconfig <network interface>` i.e.:

- `ifconfig eth0` - if ethernet connected
- `ifconfig wlan0` - if connected wirelessly

Or you can simply find it by using `ifconfig`, just look for the `ether` address i.e. `ether rf:d9:7t:pj:42`

## Setting up your dhcpcd.conf

If you head into your `dhcpcd.conf` file with `sudo nano /etc/dhcpcd.conf`.

Once in the file if you scroll down you will find an example configuration:

```bash
# Example static IP configuration:
# interface eth0
# static ip_address=192.168.0.10/24
# static ip6_address=fd51:42f8:caae:d92e::ff/64
# static routers=192.168.0.1
# static domain_name_servers=192.168.0.1
```

You can create your own as below:

### Ethernet

```bash
interface eth0
static ip_address=192.168.0.10/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
```

### Wifi

```bash
interface wlan0
static ip_address=192.168.0.10/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
```

Or create both if you intend to switch between the two.

## Setting up your router

You will need to log into your router and head to the`LAN` section of your routers config. This will of course be different on every router but should be easy enough to find.

Once in the `LAN` menu you will need to find the `DHCP` or `DHCP server` section.

You will be looking for a section that has the title `Manually Assigned IP around the DHCP list` or something similar.

The sections are likely to be:

- Client Name (MAC Address)
- IP Address
- DNS Server (Optional)
- Host Name (Optional)

You will only need to input the Mac address and IP Address:

- Mac -> `rf:d9:7t:pj:42` (example)
- IP -> `192.168.1.10`

### NOTE -> Choosing your IP

 -> Your router may have limits in the number of connections under the default gateway. There will likely be a start and an end range under your DHCP settings. In the case of the ASUS router in question it support 253 connections with a pool starting address of `192.168.1.2` pool ending address of `192.168.1.254`. You will want to ensure that the IP address you use is within that boundary and not already used by another device.
