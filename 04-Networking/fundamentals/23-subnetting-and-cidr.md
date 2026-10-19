# 23-subnetting-and-cidr

## Subnetting

- Dividing a larger IP network into smaller subnetworks (subnets).
- Helps organise address allocation and separate network segments.
- Communication between different subnets requires routing.
- Subnetting alone does not enforce security; firewall rules and other controls determine permitted traffic.

## CIDR notation

- CIDR = Classless Inter-Domain Routing.
- Represents an IP address with a prefix length:

```text
IP_ADDRESS/PREFIX_LENGTH
```

- The prefix length specifies how many bits identify the network.
- Remaining bits identify addresses within that network.
- IPv4 addresses contain 32 bits; IPv4 prefixes range from `/0` to `/32`.

## Example: 192.168.1.0/24

- Network address: `192.168.1.0`.
- Network bits: 24.
- Host bits: `32 - 24 = 8`.
- Total addresses: `2^8 = 256`.
- Address range: `192.168.1.0` to `192.168.1.255`.
- Equivalent subnet mask: `255.255.255.0`.
- In a conventional IPv4 /24 subnet:
  - Network address: `192.168.1.0`.
  - Broadcast address: `192.168.1.255`.
  - Usable host range: `192.168.1.1` to `192.168.1.254`.

## Important distinction

- An address written with a prefix is not always the network address.
- `192.168.1.10/24` identifies a host address within `192.168.1.0/24`.

## What to remember

- Larger prefix number -> smaller address block.
- Smaller prefix number -> larger address block.
- IPv4 host bits = `32 - prefix length`.
- Total addresses = `2^(host bits)`.
- DevOps relevance: plan subnet ranges and recognise overlapping networks in cloud environments.

## Coming next

- Subnet masks and binary basics.
- Calculating subnet boundaries and host ranges.
- NAT (Network Address Translation): a separate concept that changes IP addressing information in traffic.
