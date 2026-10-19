# 16-dns-components-records

## Resource records

- Individual entries containing DNS information.
- A zone contains multiple records; a zone file represents them as text.
- Main fields:
  - Name: the name the record belongs to.
  - TTL (Time To Live): how long a resolver can cache the record, in seconds.
  - Class: usually `IN`, meaning Internet.
  - Type: what kind of information the record contains.
  - Data: the value, such as an IP address or hostname.
- TTL expiry means the cached answer needs refreshing; it does not delete the authoritative record.

## A - IPv4 address

- Maps a name to an IPv4 address.

```text
app.example.com.  300  IN  A  192.0.2.10
```

## AAAA - IPv6 address

- Pronounced "quad A".
- Maps a name to an IPv6 address.

```text
app.example.com.  300  IN  AAAA  2001:db8::10
```

## CNAME - Canonical Name

- Maps an alias to another hostname, not directly to an IP address.
- The target name can then resolve through A or AAAA records.
- Useful when several names should follow one target's address changes.

```text
www.example.com.  300  IN  CNAME  app.example.com.
```

- Here, `www.example.com` follows the DNS information for `app.example.com`.
- Does not redirect the browser to a different URL.

## NS - Name Server

- Identifies an authoritative name server for a zone.
- Points to a hostname, not directly to an IP address.

```text
example.com.  3600  IN  NS  ns1.example.com.
```

## MX - Mail Exchange

- Identifies servers that receive email for a domain.
- Contains a preference number and a mail server hostname.
- Lower numbers are preferred.

```text
example.com.  3600  IN  MX  10 mail1.example.com.
example.com.  3600  IN  MX  20 mail2.example.com.
```

- Sending servers normally try `mail1` first, then `mail2` if needed.

## TXT - Text

- Stores text associated with a DNS name.
- Commonly used for:
  - Domain ownership verification.
  - Email authentication, including SPF, DKIM and DMARC.
- TXT records are widely used.

```text
example.com.  3600  IN  TXT  "verification=example-token"
```

## Useful queries

```bash
dig +short A example.com
dig +short AAAA example.com
dig +short CNAME www.example.com
dig +short NS example.com
dig +short MX example.com
dig +short TXT example.com
```

## What to remember

- A -> IPv4 address.
- AAAA -> IPv6 address.
- CNAME -> another hostname.
- NS -> authoritative name server.
- MX -> receiving mail server, with a preference number.
- TXT -> text used for verification and other policies.
- Understand record purposes; exact record syntax can be looked up.
