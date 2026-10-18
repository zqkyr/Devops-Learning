# 05-switches-routers-and-firewalls

## Switches

- Connect devices within a LAN, such as computers, printers and servers.
- A typical Layer 2 switch uses MAC addresses to forward Ethernet frames to the appropriate port.
- Improves traffic flow, but does not guarantee that congestion cannot occur.

## Routers

- Connect different networks and forward packets between them.
- Use destination IP addresses and a routing table to select where to send packets next.
- Example: your home router forwards traffic between your LAN and your internet provider's network.

## Firewalls

- Allow or block network traffic according to security rules.
- Rules can consider source/destination IP addresses, ports and protocols.
- Help prevent unauthorized access; protection depends on correct configuration.
- Can run as software or as dedicated network devices.

## What to remember

- Switch: connects devices within a network.
- Router: connects different networks.
- Firewall: controls which traffic is allowed.
- One device can perform multiple roles; home routers often include a switch, firewall and Wi-Fi access point.

## DevOps relevance

- When troubleshooting connectivity, check:
  - Local network connectivity.
  - Routing to the destination network.
  - Whether firewall rules allow the required traffic.
