# 22-common-routing-protocols

## What routing protocols do

- Let routers exchange information and automatically learn routes.
- Select preferred routes using protocol metrics and routing policies.
- Update routes when network changes are detected.
- Can provide failover if an alternative path exists.
- Do not necessarily choose the fastest path or automatically avoid congestion.

## OSPF - Open Shortest Path First

- An interior gateway protocol: used within an autonomous system.
- Common in organisational networks.
- Uses link-state information to build a view of network topology.
- Calculates the lowest-total-cost path.
- Cost is commonly based on interface bandwidth, but can be configured.
- "Shortest" means lowest cost, not necessarily fewest routers or lowest latency.
- Can converge quickly after network changes.
  - Convergence: routers updating their routing information to reflect the changed network.

## BGP - Border Gateway Protocol

- Used to exchange routes between autonomous systems.
- Fundamental to routing on the internet.
- An autonomous system (AS) is a network or group of networks under a common routing administration and policy.
- Uses a path-vector approach:
  - Routes include attributes such as the AS path.
  - The AS path identifies the autonomous systems a route has passed through.
- Selects routes using policies and path attributes, not simply speed or distance.
- Also operates within an AS as internal BGP (iBGP).

## What to remember

- OSPF: routing within an AS, using link states and costs.
- BGP: routing between autonomous systems, with strong policy control.
- Both support dynamic routing.
- DevOps relevance: recognise these when working with enterprise networks, cloud connectivity and advertised routes.
- Detailed algorithms, attributes and configuration can be looked up.
