# 14-what-is-dns

## What DNS does

- DNS = Domain Name System.
- Resolves human-readable domain names into IP addresses.
- Example: resolving `www.google.com` lets your browser find an IP address to connect to.
- Think of a contacts list: look up a name to find the corresponding number.
- DNS also stores other information, such as mail server details.

## Names vs IP addresses

- Humans use names because they are easier to remember.
- IP networking uses IP addresses to deliver packets.
- DNS provides the mapping between names and addresses.
- A name can resolve to multiple IP addresses.
- Multiple names can point to the same IP address.

## Why DNS matters

- Applications can use stable names even when server IP addresses change.
- DevOps uses DNS for websites, APIs, databases and other services.
- DNS problems can prevent connections even when the destination server is running.

## What to remember

- DNS finds address information; it does not carry the subsequent web traffic.
- DNS is not the only way to map names: `/etc/hosts` can provide local mappings.
- Entering an IP directly is not always equivalent to using a website's name; hosting and HTTPS can depend on the hostname.
