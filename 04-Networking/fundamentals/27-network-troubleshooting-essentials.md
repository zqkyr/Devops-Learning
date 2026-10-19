# 27-network-troubleshooting-essentials

## Why troubleshoot?

- Identify the cause of connectivity and performance problems.
- Restore services and minimise downtime.
- Use evidence to narrow down the fault rather than guessing.

## Common issues

- Connectivity loss:
  - Cable faults, Wi-Fi problems, failed interfaces or incorrect routes.
- Slow performance:
  - Congestion, packet loss or high latency.
  - Slow applications can also result from server or application problems.
- IP address conflicts:
  - Two devices using the same IP on the same network can disrupt connectivity.
- DNS failures:
  - Names fail to resolve or resolve to incorrect addresses.

## A practical troubleshooting approach

1. Define the symptom and scope.
   - What fails, when did it start, and what changed?
   - Does it affect one device, one service or many systems?
2. Check basic connectivity.
   - Cables, Wi-Fi connection and interface status.
3. Check configuration.
   - IP address, subnet mask/prefix, default gateway and DNS resolver.
4. Test the relevant part of the connection.
   - Local gateway, remote IP, DNS lookup or application port.
5. Make a targeted change and retest.
   - Confirm the original problem is resolved.
   - Avoid restarting devices blindly; restarts can disrupt services and hide evidence.

## Testing with ping

```bash
# Test a remote IP without needing DNS
ping -c 4 1.1.1.1

# Test a hostname, which also requires name resolution
ping -c 4 google.com
```

- Ping uses ICMP Echo requests and replies.
- Replies show that ICMP communication worked with that destination at that time.
- They do not prove that a website or application port is working.
- No reply does not prove the destination is down; ICMP may be blocked or rate-limited.

## Separating DNS from connectivity

```bash
dig google.com
```

- If IP connectivity works but name lookup fails, investigate DNS.
- If DNS works but the application fails, check routing, firewall rules, ports and the service itself.

## What to remember

- Observe -> narrow the scope -> check configuration -> test -> fix -> retest.
- Distinguish DNS failures, connectivity failures and application failures.
- Use the OSI layers as a troubleshooting guide.
- Understand what each test proves and what it cannot prove.
