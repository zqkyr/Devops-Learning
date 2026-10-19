# 25-calculating-subnets

## Subnet masks

- Identify the network and host portions of an IPv4 address.
- In binary:
  - Consecutive `1` bits identify the network portion.
  - Remaining `0` bits identify the host portion.
- The CIDR prefix counts the network bits.

```text
Mask:   255.255.255.0
Binary: 11111111.11111111.11111111.00000000
Prefix: /24
```

## Calculating an IPv4 subnet

- Host bits = `32 - prefix length`.
- Total addresses = `2^(host bits)`.
- Network address: all host bits set to `0`.
- Broadcast address: all host bits set to `1`.
- For conventional subnets from /30 and larger address blocks:
  - Usable hosts = total addresses minus 2.
  - First usable address = network address + 1.
  - Last usable address = broadcast address - 1.
- /31 and /32 have different rules.
- Cloud platforms may reserve additional addresses.

## Finding subnet boundaries

- For a mask octet that is neither 255 nor 0:
  - Block size = `256 - mask value`.
  - Subnets begin at multiples of that block size in that octet.

```text
/26 mask: 255.255.255.192
Block size: 256 - 192 = 64

Boundaries within 192.168.1.0/24:
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

- Each block ends immediately before the next boundary.

## Practice: 192.168.1.0/26

- Calculate:
  1. Network address.
  2. Broadcast address.
  3. First and last usable host addresses.
  4. Number of usable host addresses.
- Hint: there are `32 - 26 = 6` host bits.

## What to remember

- The prefix determines the size and boundaries of the subnet.
- Network and broadcast addresses are normally unavailable to hosts in conventional IPv4 subnets.
- Understand the method; use a subnet calculator to verify real configurations.
