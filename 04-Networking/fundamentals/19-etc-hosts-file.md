# 19-etc-hosts-file

## What is /etc/hosts?

- A local file on Linux and macOS that maps hostnames to IP addresses.
- Correct path: `/etc/hosts`, not `/etc/host`.
- Useful for development, testing and troubleshooting without changing public DNS.
- Entries affect only the machine where the file is edited.
- System lookup configuration and application behaviour determine whether it is consulted; it is not always checked first.

## Entry format

```text
IP_ADDRESS  HOSTNAME  OPTIONAL_ALIASES
```

```text
127.0.0.1  example.com
192.168.1.50  dev.test
```

- `127.0.0.1`: your own machine, also called the loopback address.
- `192.168.1.50`: an example local server address; replace it with your actual server's IP.
- `.test` is intended for testing; avoid `.local`, which is used by multicast DNS (mDNS).

## Editing the file

- Normally requires administrator privileges.

```bash
sudo nano /etc/hosts
```

- Add the required mappings and save.
- Remove your test entries when finished.
- Leave existing system entries intact.
- Cached results may delay changes taking effect.

## Testing a mapping

- Use an application that uses the system's hostname lookup.

```bash
ping -c 1 dev.test
```

- Check the IP shown in the output.
- A missing ping reply does not necessarily mean the mapping failed; ICMP may be blocked.
- `dig` and `nslookup` query DNS and normally do not read `/etc/hosts`.

## Important corrections

- The `Server` shown by `nslookup` is your DNS resolver, not necessarily a web server or your intended test server.
- Use the actual IP of the server you want to reach.
- A hosts entry only changes name-to-IP mapping:
  - It does not start a web server.
  - It does not open ports or bypass firewalls.
  - It does not configure HTTPS certificates.
- Mapping a hostname to `127.0.0.1` requires a local service if you want to access a website through it.

## What to remember

- `/etc/hosts` = local hostname-to-IP mappings.
- It changes local lookup behaviour, not public DNS.
- Use it to test a hostname against a chosen server, then remove temporary entries.
