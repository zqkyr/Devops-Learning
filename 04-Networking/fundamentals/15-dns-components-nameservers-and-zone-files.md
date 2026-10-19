# 15-dns-components-nameservers-and-zone-files

## Authoritative name servers

- Serve the official DNS records for a zone.
- Answer queries using the zone data they manage.
- Can also return authoritative answers that a name or record does not exist.
- Hosting a domain's DNS does not mean hosting its website.

## Recursive resolvers

- Find DNS answers on behalf of clients.
- Return a cached answer when available and valid.
- Otherwise, query other DNS servers, following referrals as needed.
- Cache results according to their TTL (Time To Live).
- Examples: resolvers provided by your ISP, organisation or a public DNS service.

## Finding a domain's name servers

- Query NS records using `dig`:

```bash
dig NS google.com
```

- Show only the returned record values:

```bash
dig +short NS google.com
```

- NS records identify the authoritative name servers for a zone.
- By default, these commands ask your configured resolver.
- `dig` may need to be installed; it is not available by default on every Unix-like system.

## Zones and zone files

- A zone is a portion of the DNS namespace managed by an authority.
- A zone file is a text representation of that zone's DNS records.
- Authoritative servers can load zone files to answer queries.
- Records can include:
  - SOA: zone authority and administrative information.
  - NS: authoritative name servers.
  - A: IPv4 addresses.
  - AAAA: IPv6 addresses.
  - MX: mail servers.
- Some DNS services store records in databases rather than local text files.
- Zone files store authoritative data; they are not instructions for recursively finding unknown answers.

## What to remember

- Authoritative server: serves records for its zones.
- Recursive resolver: looks up answers for clients and caches them.
- Zone file: stores a zone's DNS records in text form.
- Understand these roles; detailed zone-file syntax can be looked up.
