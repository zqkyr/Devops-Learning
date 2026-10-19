# 20-what-is-routing

## What is routing?

- Selecting paths for packets to travel between networks.
- Routers use destination IP addresses and routing tables to decide where to forward packets next.
- Operates at OSI Layer 3, the network layer.
- "Best" means preferred according to routing rules and metrics, not necessarily the fastest path.

## Routing tables

- Contain routes to destination networks.
- Routes specify a next hop or an outgoing interface.
- The most specific matching route is preferred: longest-prefix matching.
- A default route is used when no more specific route matches.
- Without a matching route, a packet cannot be forwarded and is normally dropped.

## How packets travel

1. Your computer checks its own routing table.
2. For a destination on the local network, it normally sends directly.
3. For a remote destination, it commonly sends to its default gateway.
4. Each router checks its own routing table and forwards the packet to the next hop.
5. This continues until the packet reaches the destination network and host.

```text
Your computer -> Default gateway -> Other routers -> Destination
```

- Routers normally choose the next hop, not the entire end-to-end path.
- The return traffic may follow a different path.
- Routing does not guarantee delivery, low latency or permission through a firewall.

## Why routing matters in DevOps

- Enables communication between servers, subnets and cloud networks.
- Route tables help control connectivity in cloud environments.
- Missing or incorrect routes can make running services unreachable.
- Troubleshooting requires checking both the outgoing and return paths.

## Coming next

- Static routing: manually configured routes.
- Dynamic routing: routers learn routes using routing protocols.
- Protocol examples: OSPF and BGP.

## What to remember

- Router = device forwarding packets between networks.
- Routing table = information used to choose the next hop.
- Check routing when a destination on another network is unreachable.
- Detailed route-selection rules and protocol configuration can be looked up.
