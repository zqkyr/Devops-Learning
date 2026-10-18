# 07-ports-and-protocols-tcp-and-udp

## Ports

- Logical numbers used by TCP and UDP to direct traffic to the correct application or service.
- Range: `0-65535`.
- Servers usually listen on a known port; clients typically use temporary source ports.
- Common examples:
  - SSH: TCP port 22.
  - HTTP: TCP port 80.
  - HTTPS: TCP port 443; HTTP/3 uses UDP port 443.
  - DNS: UDP and TCP port 53.
- These are defaults; services can be configured to use other ports.
- TCP and UDP have separate port spaces: TCP port 53 and UDP port 53 are distinct.

## Protocols

- Rules defining how systems format, exchange and interpret data.
- Examples:
  - HTTP: web requests and responses.
  - FTP: file transfers.
  - SMTP: sending email.
  - TCP and UDP: transport protocols used by applications.

## TCP (Transmission Control Protocol)

- Connection-oriented: normally establishes a connection using a three-way handshake.
  - `SYN -> SYN-ACK -> ACK`.
- Provides reliable, ordered delivery of a byte stream.
- Uses acknowledgements and retransmissions to recover from lost data.
- Detects corruption using a checksum.
- Flow control: prevents overwhelming the receiver.
- Congestion control: adjusts sending rate to network conditions.
- Supports bidirectional communication.
- Common uses: SSH, email, file transfers and HTTP/1.1 or HTTP/2.
- Reliability does not guarantee success: a connection can still fail.

## UDP (User Datagram Protocol)

- Connectionless: no transport handshake before sending.
- Sends individual messages called datagrams.
- Has lower transport overhead than TCP.
- Does not provide built-in:
  - Guaranteed delivery.
  - Ordering or duplicate suppression.
  - Retransmissions.
  - Flow or congestion control.
- Has a checksum for error detection; it does not repair or retransmit corrupted data.
- Applications can implement reliability or congestion control on top of UDP.
- Common uses: DNS queries, real-time calls, online games and some VPN protocols.

## Important distinctions

- UDP is not always faster; performance depends on the application and network.
- DNS commonly uses UDP, but also uses TCP.
- Video streaming can use TCP or UDP-based protocols; watching a video does not prove UDP is being used.
- Both TCP and UDP support communication in both directions.
- TCP reliability does not provide encryption.

## What to remember

- IP address: identifies the network destination.
- Port: helps identify the destination service.
- Protocol: defines the communication rules.
- TCP: reliable, ordered byte stream.
- UDP: independent datagrams with fewer built-in delivery guarantees.

## DevOps relevance

- Check the destination IP, port and transport protocol when troubleshooting.
- A service must be listening and relevant firewall rules must allow the traffic.
- Allowing a TCP port does not automatically allow the same UDP port.
