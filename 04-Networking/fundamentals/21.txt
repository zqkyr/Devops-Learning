# 21-static-vs-dynamic-routing

## Static routing

- Routes are explicitly configured by an administrator or automation.
- Usually specifies a destination network and a next hop or outgoing interface, not the entire end-to-end path.
- Does not use a routing protocol to learn alternative routes.

### Benefits

- Simple for small, stable networks.
- Predictable and gives direct control over routes.
- No routing-protocol traffic between routers.

### Limitations

- Changes usually require configuration updates.
- Maintaining many routes increases effort and the risk of mistakes.
- Does not automatically discover an alternative path after a failure.
- Tracking and backup static routes can provide failover when explicitly configured.

### Common uses

- Default routes.
- Small networks.
- Specific routes to known networks.

## Dynamic routing

- Routers exchange reachability information using routing protocols.
- Automatically learn, select and update routes.
- Examples:
  - OSPF: Open Shortest Path First.
  - BGP: Border Gateway Protocol.
- Administrators still configure the protocol, neighbours and routing policies.

### Benefits

- Adapts to advertised network changes and detected failures.
- Can select an alternative route if one is available.
- Scales better for many large or changing networks.

### Limitations

- More complex to configure and troubleshoot.
- Uses processing, memory and protocol traffic.
- Changes take time to propagate and settle; this is called convergence.
- Does not necessarily detect congestion or select the lowest-latency path.
- Route selection depends on protocol metrics and policies.

## What to remember

- Static: explicitly configured routes.
- Dynamic: routes learned and updated through routing protocols.
- Both can be used in the same network.
- Neither guarantees delivery or creates an alternative path where none exists.
- DevOps relevance: understand whether a route is configured or learned when troubleshooting connectivity.
- Detailed OSPF and BGP configuration can be looked up.
