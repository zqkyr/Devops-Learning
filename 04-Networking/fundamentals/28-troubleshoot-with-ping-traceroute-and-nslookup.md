# 28-troubleshoot-with-ping-traceroute-and-nslookup

## ping - Test ICMP connectivity

```bash
ping -c 4 1.1.1.1
ping -c 4 example.com
```

- Sends ICMP Echo requests and reports replies, round-trip times and packet loss.
- An IP address tests without requiring DNS.
- A hostname also requires name resolution.
- Success does not prove the whole network or website is working.
- Failure may mean ICMP is blocked or rate-limited, not that the destination is down.

## traceroute - Investigate network hops

```bash
traceroute example.com
```

- Uses probes with increasing TTL/hop limits to discover responding routers along a path.
- Displays hop numbers, responding addresses and round-trip times.
- `*` means no response arrived before the timeout.
- Missing replies do not necessarily indicate a broken hop; routers may filter or rate-limit probes.
- Routes can change, and application traffic may take a different path.
- May require installation.

## nslookup - Query DNS

```bash
nslookup example.com
```

- Shows the DNS server queried and the returned DNS answer.
- Helps identify missing or unexpected address records.
- A successful lookup does not prove the address is correct or the website is reachable.
- Normally does not check `/etc/hosts`.

## Example: a website will not load

1. Identify the scope and error.
   - One website or all websites?
   - One device or multiple devices?
   - Name-resolution error, timeout or HTTP error?
2. Check local connectivity and configuration.
   - Wi-Fi/cable, IP address and default gateway.
3. Check DNS for the affected hostname.
   - Use `nslookup` or `dig`.
   - Check `/etc/hosts` for unintended mappings.
4. Test the actual web service.

```bash
curl -I --connect-timeout 5 https://example.com
```

- Requests HTTP response headers.
- Can expose resolution, connection, TLS or HTTP errors.
- An HTTP error response still shows that a server answered.
- Some services reject HEAD requests; this alone does not prove the site is unavailable.

5. Use traceroute if a path problem is suspected.
6. Check relevant firewall rules, service status and logs.
7. Make a targeted change and retest.

## What to remember

- Ping: can this destination exchange ICMP traffic?
- Traceroute: which hops respond along the probe path?
- Nslookup/dig: what does DNS return?
- Curl: can the web service respond?
- Clear caches or restart applications when evidence supports doing so.
- Test the affected destination; reaching Google does not prove another website is reachable.
