# 26-nat-network-address-translation

## What is NAT?

- NAT = Network Address Translation.
- Changes IP addresses in packets as they pass through a router or other network device.
- Common use: letting devices with private IPv4 addresses access the internet.
- Private IPv4 addresses are not routed on the public internet.
- Sharing one public IPv4 address between many devices normally uses PAT, a type of NAT.

## How outbound NAT works

Example: a laptop with private IP `192.168.1.10` accesses a website.

1. The laptop sends traffic through its router.
2. The router replaces the packet's private source IP with a public IP.
3. It records the translation.
4. The website replies to the public IP.
5. The router uses the translation information to send the reply to the laptop.

- The website sees the translated public source IP.
- The laptop keeps its private IP; NAT changes packet addressing, not the laptop's configured address.

## Static NAT

- A fixed one-to-one mapping between an internal and an external IP address.

```text
192.168.1.10 <-> 203.0.113.10
```

- Useful when a device needs a consistent external address.
- Incoming access still requires suitable routing and firewall rules.

## Dynamic NAT

- Temporarily maps an internal IP to an available public IP from a pool.
- Each active mapping is still one-to-one.
- Mappings expire, allowing public addresses to be reused.
- Without PAT, simultaneous mappings are limited by the available public addresses.

## PAT - Port Address Translation

- Also called NAT overload.
- Allows multiple devices and connections to share a public IP.
- Uses IP addresses, transport protocols and port mappings to distinguish traffic.

```text
Internal connection       Translated source
192.168.1.10:50000   ->    203.0.113.10:61001
192.168.1.11:50000   ->    203.0.113.10:61002
```

- The router tracks which connection each reply belongs to.
- Ports identify connections, not permanent identities for devices.
- Common on home routers.

## Why NAT matters

- PAT conserves public IPv4 addresses.
- Allows private addressing inside homes, offices and cloud networks.
- DevOps relevance: enables outbound connectivity from private networks, such as downloading packages or accessing external APIs.

## Important distinctions

- NAT is not encryption or a replacement for a firewall.
- Hiding private addresses does not by itself secure a network.
- New inbound connections generally need an explicit mapping, such as port forwarding, plus firewall permission.
- IPv6 generally allows internet connectivity without address-sharing NAT.

## What to remember

- Static NAT: fixed one-to-one mapping.
- Dynamic NAT: temporary one-to-one mapping from a pool.
- PAT: many connections share a public IP using port translations.
- Understand the outbound request and return path; detailed configuration can be looked up.
