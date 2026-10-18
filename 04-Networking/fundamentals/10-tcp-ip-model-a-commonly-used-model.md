# 10-tcp-ip-model-a-commonly-used-model

## Overview

- TCP/IP describes the protocol suite used by the internet.
- Commonly represented using four layers.
- Covers similar responsibilities to OSI, grouped differently; it was not simply created by condensing OSI.

## 4 - Application

- Provides application communication and handles responsibilities associated with OSI Layers 5-7.
- Examples: HTTP, DNS, SMTP and SSH.
- Includes functions such as data representation, encryption and session management.
- TLS sits above transport and is generally grouped here in the four-layer model.

## 3 - Transport

- Provides communication between application endpoints using ports.
- TCP: reliable, ordered byte stream.
- UDP: datagrams without built-in delivery or ordering guarantees.
- Corresponds to OSI Layer 4.

## 2 - Internet

- Handles logical addressing and packet forwarding across networks.
- Examples: IPv4, IPv6 and ICMP.
- Routers use destination IP addresses and routing tables to select the next hop.
- IP provides best-effort delivery; it does not guarantee arrival or ordering.
- Corresponds to OSI Layer 3.

## 1 - Network Access

- Also called the link layer.
- Handles local-link communication and physical transmission.
- Examples: Ethernet and Wi-Fi.
- Includes frames, MAC addressing and signals.
- Corresponds broadly to OSI Layers 1-2.
- A LAN is a type of network, not a protocol.

## OSI mapping

- OSI 7, 6, 5 -> Application.
- OSI 4 -> Transport.
- OSI 3 -> Internet.
- OSI 2, 1 -> Network Access.

## What to remember

- Layer order: Application -> Transport -> Internet -> Network Access.
- Understand each layer's responsibility and its OSI mapping.
- Example stack: HTTP -> TCP -> IP -> Ethernet.
- DevOps relevance: distinguish application failures, transport issues, routing problems and local connectivity faults.
