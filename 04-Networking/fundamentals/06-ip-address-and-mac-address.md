# 06-ip-address-and-mac-address

## IP addresses

- IP = Internet Protocol.
- A logical address assigned to a network interface.
- Used to identify sources and destinations and route packets between networks.
- An interface can have multiple IP addresses, and addresses can change.
- Addresses must be unique within their relevant network scope; private IP addresses can be reused in separate networks.

### IPv4

- 32-bit address space: approximately 4.3 billion addresses.
- Written as four decimal numbers separated by dots.
- Each number ranges from 0 to 255.
- Example: `192.168.0.5`.
- Limited address space drove the development of IPv6.

### IPv6

- 128-bit address space: approximately 3.4 x 10^38 addresses.
- Full notation uses eight groups of four hexadecimal digits, separated by colons.
- Hexadecimal uses `0-9` and `a-f`.
- Example: `2001:db8:0:0:0:0:0:5`.
- Compressed form: `2001:db8::5`.
- Provides a much larger address space and supports automatic address configuration.
- IPv6 is not automatically more secure; security still requires correct configuration.

## MAC addresses

- MAC = Media Access Control.
- A link-layer address used by Ethernet and Wi-Fi interfaces for local communication.
- Typically 48 bits, displayed as six pairs of hexadecimal digits.
- Example: `00:18:2b:3c:4d:5e`.
- Operates at OSI Layer 2, the data link layer.
- A laptop's Wi-Fi and Ethernet interfaces normally have different MAC addresses.
- MAC addresses can be changed, spoofed or randomized; they are not reliable proof of identity.

## IP vs MAC

- IP address: used to route packets across networks.
- MAC address: used to deliver frames on the local network link.
- Switches typically forward frames using MAC addresses.
- Routers forward packets using destination IP addresses.
- For a remote destination, your device sends the local frame to its gateway's MAC address, while the packet targets the remote IP address.
- Choosing the correct Wi-Fi network involves the network name and authentication; MAC addresses alone do not ensure this.

## What to remember

- IPv4 = 32 bits; IPv6 = 128 bits.
- Typical Ethernet/Wi-Fi MAC address = 48 bits.
- Understand the different roles of IP and MAC addresses.
- Exact IPv6 address counts and detailed notation rules can be looked up.
