# 29-cloud-networking

## What is cloud networking?

- Configuring and managing networks in cloud environments using software.
- Applies familiar concepts: IP addresses, subnets, routing, DNS and firewalls.
- DevOps relevance: connect applications and infrastructure while controlling access.
- This lesson introduces AWS networking; detailed configuration comes later.

## VPC - Virtual Private Cloud

- A logically isolated virtual network in AWS.
- You configure its IP address ranges, subnets, route tables and connectivity.
- A VPC does not automatically make resources internet-accessible.

## Subnets

- Subdivisions of a VPC's IP address range.
- Group resources into network segments, such as application and database tiers.
- In AWS, each subnet belongs to one Availability Zone.
- Routes and security controls determine connectivity; separate subnets alone do not enforce access restrictions.

## Route tables

- Contain rules determining where traffic is directed.
- Each subnet uses an associated route table.
- Routes specify destination ranges and targets, such as gateways.

## Gateways

- Provide connectivity beyond the VPC.
- Different gateway types serve different purposes:
  - Internet gateway: enables internet connectivity when addressing, routes and security rules also permit it.
  - NAT gateway: commonly enables outbound IPv4 internet access for resources in private subnets.
- A NAT gateway does not allow unsolicited inbound internet connections to those resources.

## DNS - Route 53

- AWS service for DNS hosting and other domain-related functions.
- Supports public and private hosted zones.
- Private zones provide DNS information within associated VPCs.

## Traffic filtering

- Security groups:
  - Apply to supported resources through network interfaces.
  - Stateful: response traffic for allowed connections is automatically permitted.
- Network ACLs (NACLs):
  - Apply at subnet boundaries.
  - Stateless: inbound and outbound rules are evaluated separately, including return traffic.

## Coming next

- Container networking.
- More detail on VPCs, subnets, routes and security controls.

## What to remember

- VPC = virtual network.
- Subnet = segment of that network.
- Route table = where traffic goes.
- Gateway = connection to another network.
- Security controls = which traffic is permitted.
- Recognise the components now; detailed AWS setup comes later.
