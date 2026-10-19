# 24-binary-1s-and-0s

## Binary basics

- Binary is base 2: each digit is either `0` or `1`.
- Each digit is one bit.
- Place values double from right to left.
- An IPv4 address has 32 bits, split into four 8-bit octets.
- Each octet represents a decimal value from 0 to 255.

## Octet place values

```text
128  64  32  16   8   4   2   1
```

- `1`: include that place value.
- `0`: do not include it.
- Add the included values to get the decimal number.

## Binary to decimal

```text
Binary:       00101010
Place values: 128 64 32 16 8 4 2 1
Included:            32    8   2

32 + 8 + 2 = 42
```

- Leading zeros do not change the value.
- `101010` and `00101010` both represent 42.
- Use eight bits per octet when writing IPv4 addresses in binary.

## Decimal to binary

- Work through the place values from 128 down to 1.
- If a value fits into the remaining number, write `1` and subtract it.
- Otherwise, write `0`.

```text
192 = 128 + 64
192 = 11000000

168 = 128 + 32 + 8
168 = 10101000

1 = 00000001
```

- Alternative: repeatedly divide by 2 using whole-number division, note the remainders, then read them from bottom to top.

## IPv4 example

```text
Decimal: 192.168.1.1
Binary:  11000000.10101000.00000001.00000001
```

## Subnet mask connection

- A subnet mask uses consecutive `1` bits for the network portion, followed by `0` bits for the host portion.

```text
/24: 11111111.11111111.11111111.00000000
     255.255.255.0
```

## Practice

- Convert these to binary:
  - IP address: `10.0.0.1`.
  - Subnet mask: `255.0.0.0`.
- Use the eight place values and convert each octet separately.

## What to remember

- Octet values: `128 64 32 16 8 4 2 1`.
- Add the values where the bits are `1`.
- Understand how bits relate to subnet prefixes; conversion tools can handle routine calculations.
