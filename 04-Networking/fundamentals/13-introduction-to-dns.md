# 13-introduction-to-dns

## Chapter overview

- DNS = Domain Name System.
- Resolves domain names to IP addresses and provides other information about domains.
- Helps applications locate services without users needing to remember IP addresses.

## Topics covered

- DNS fundamentals and its role in networking.
- Core components:
  - Resolvers.
  - Name servers.
  - Zones and zone files.
- DNS records: entries containing information about names and services.
- How DNS resolution works, step by step.
- Command-line tools for DNS troubleshooting.
- A practical lab using `/etc/hosts`.

## Important distinction

- `/etc/hosts` provides local hostname-to-IP mappings; it is not a DNS server or zone file.
- Applications using the system resolver can consult it according to the system's lookup configuration.
- Editing it affects lookups on that machine, not public DNS.

## What to remember

- DNS helps translate names into information applications need to connect.
- Resolving a name does not guarantee the destination service is reachable.
- This lesson introduces the chapter; detailed records and lookup behaviour come later.
