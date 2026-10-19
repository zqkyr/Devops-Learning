# Networking Assignments

This folder contains my practical networking projects and exercises from the DevOps curriculum.

Each assignment includes its objectives, configuration, useful commands, screenshots, troubleshooting steps and lessons learned.

Projects include deploying NGINX on AWS EC2, configuring DNS through Cloudflare and troubleshooting connectivity between a custom domain and a web server.

## Useful Resources

- [AWS EC2 SSH Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) — connecting to a Linux instance.
- [NGINX Beginner’s Guide](https://nginx.org/en/docs/beginners_guide.html) — web-server configuration and operation.
- [Cloudflare DNS Documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) — creating and managing DNS records.

## Command Reference

Replace example hostnames, addresses and filenames with the values for your environment.

### SSH Access — Run Locally

```bash
# Restrict private-key permissions
chmod 400 networking-lab.pem

# Connect to an Amazon Linux instance
ssh -i networking-lab.pem ec2-user@<EC2_PUBLIC_DNS>
```

### NGINX — Run on Amazon Linux 2023

```bash
# Install NGINX
sudo dnf install nginx -y

# Start NGINX and enable startup after reboot
sudo systemctl enable --now nginx

# Check service status
sudo systemctl status nginx

# Validate configuration before reloading
sudo nginx -t

# Reload configuration after a successful validation
sudo systemctl reload nginx
```

### DNS and Connectivity

```bash
# Query DNS using the configured resolver
nslookup example.com

# Compare with a specific resolver
nslookup example.com 1.1.1.1

# Inspect A records
dig A example.com

# Find authoritative name servers
dig +short NS example.com

# Test ICMP connectivity
ping -c 4 example.com

# Investigate responding network hops
traceroute example.com

# Request web-server response headers
curl -I --connect-timeout 5 http://example.com
```

- DNS tools check name resolution.
- Ping checks ICMP responses, not whether a website works.
- Curl checks the web service.
- Testing a public IP directly can help separate DNS problems from web-server problems.

## Repository Security

Private keys, credentials and sensitive screenshots must not be committed.

Add this rule to the repository’s root `.gitignore`:

```gitignore
*.pem
```

Verify the rule from the repository root:

```bash
git check-ignore -v 04-Networking/assignments/networking-lab.pem
```

## Lab Cleanup

After each assignment, review cloud resources and remove those no longer needed. Stopping EC2 makes the website unavailable, and its automatically assigned public IPv4 address may change when restarted.
