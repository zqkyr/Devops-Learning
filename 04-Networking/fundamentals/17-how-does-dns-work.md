# 17-how-does-dns-work

## DNS resolution

- Finding DNS information for a name, commonly an IP address.
- A recursive resolver does the lookup on the client's behalf.
- Cached answers can avoid repeating the full lookup.

## DNS hierarchy

- Root (`.`):
  - Directs resolvers to the relevant TLD name servers.
- TLD (Top-Level Domain), such as `.com` or `.org`:
  - Provides delegation information for domains beneath it.
- Domain's authoritative name servers:
  - Serve official records for the zones they manage.

## Example lookup: www.example.com

1. The client may check local sources, such as caches and `/etc/hosts`.
   - Lookup order depends on system and application configuration.
2. If needed, the client queries its configured recursive resolver.
3. The resolver checks its cache.
4. Without relevant cached information, it asks a root server.
   - Receives a referral to `.com` name servers.
5. It asks a `.com` name server.
   - Receives a referral to `example.com` name servers.
6. It asks an authoritative server for `www.example.com`.
   - Receives the requested record, or an alias requiring further resolution.
7. The resolver caches the result according to its TTL and returns it.
8. The client uses the address to connect to the destination service.

```text
Client -> Recursive resolver
              |
              +-> Root: where are the .com name servers?
              +-> .com: where are example.com's name servers?
              +-> Authoritative server: what is www.example.com's address?
              |
Client <- DNS answer
```

- The resolver contacts these servers; they do not pass the client's request along a chain.
- Cached records and referrals let it skip steps.
- DNS resolution and the subsequent application connection are separate.

## Domains, zones and servers

- Domain: a name and the namespace beneath it.
- Zone: the portion of that namespace managed together.
- A subdomain can be delegated into a separate zone.
- Authoritative servers serve zone data; a zone file is one way to store it.

## Registrar vs DNS hosting provider

- Registrar:
  - Registers and renews your domain.
  - Lets you configure its authoritative name server delegation.
- DNS hosting provider:
  - Operates authoritative name servers.
  - Lets you manage records in your DNS zone.
- One company can provide both roles, or you can use separate companies.

## Using separate providers

1. Create the zone with your DNS hosting provider.
2. Add the required DNS records.
3. Configure the provider's assigned name servers at your registrar.
4. Existing cached delegation and records may remain until their TTLs expire.

## What to remember

- Resolver searches; authoritative server supplies official zone data.
- Root -> TLD -> domain's authoritative servers.
- Registrar manages registration; DNS host manages DNS records.
- For troubleshooting, distinguish name-resolution failures from connection failures after resolution.
