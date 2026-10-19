# Deploying NGINX on AWS EC2 with a Custom Domain

## Project Overview

This project connected networking theory to a working cloud deployment. I launched an Amazon Linux EC2 instance, connected to it through SSH, ran NGINX and configured DNS in Cloudflare for my domain, `zqkyr.co.uk`.

The main goal was to understand how a domain name, public IP address, firewall and web server work together.

## Technologies Used

- AWS EC2: virtual Linux server.
- Amazon Linux 2023: server operating system.
- NGINX: web-server software.
- Cloudflare: DNS management.
- SSH: secure remote terminal access.
- Git and GitHub: version control and project documentation.
- macOS and VS Code: local development environment.

## Architecture

```text
Visitor enters the domain
          |
          v
DNS resolves the hostname
          |
          v
Cloudflare proxy
          |
          v
EC2 public IPv4 address
          |
          v
Security group allows HTTP on port 80
          |
          v
NGINX returns the default web page
```

Cloudflare proxying was enabled on the DNS record, so DNS could return Cloudflare addresses rather than the EC2 address directly.

## 1. Creating the EC2 Instance

I launched an instance named `networking-nginx-lab` with:

- Amazon Linux 2023.
- A `t3.micro` instance type.
- The Europe (Stockholm) region, `eu-north-1`.
- A public IPv4 address.
- An SSH key pair named `networking-lab`.

I configured the security group to allow:

| Traffic | Port | Source | Purpose |
|---|---|---|---|
| SSH | TCP 22 | My IP | Remote terminal access |
| HTTP | TCP 80 | Internet | Access to the web server |

HTTPS was outside the initial setup. Allowing port 443 alone would not configure HTTPS; NGINX would also need TLS configuration and a suitable certificate.

## 2. Managing the SSH Private Key

I moved the downloaded key into my local assignments directory:

```bash
mv ~/Downloads/networking-lab.pem \
  /Users/zakahmed/Devops-Learning/04-Networking/assignments/
```

I restricted the key's permissions:

```bash
chmod 400 networking-lab.pem
ls -la
```

`chmod 400` makes the file readable only by its owner. The resulting permissions were:

```text
-r--------
```

I also learned that local file permissions and Git tracking are separate. A read-only file can still be committed unless it is excluded from Git.

### Preventing accidental commits

From the repository root, I created a `.gitignore` file and added a rule for PEM files:

```bash
touch .gitignore
echo '*.pem' >> .gitignore
```

I verified the rule:

```bash
git check-ignore -v 04-Networking/assignments/networking-lab.pem
```

The output confirmed the matching rule:

```text
.gitignore:1:*.pem  04-Networking/assignments/networking-lab.pem
```

I used `git status` to inspect the repository before committing.

### Security lesson

A private key was accidentally included in a screenshot during the project. Such a key must be treated as exposed: adding it to `.gitignore` does not revoke it or undo exposure.

The corrective action is to replace the key and remove the old public key from the instance's authorised keys. Screenshots containing private keys must not be included in the repository.

## 3. Connecting Through SSH

From my Mac, I connected using the private key, the Amazon Linux username and the instance's public DNS hostname:

```bash
ssh -i "networking-lab.pem" ec2-user@<EC2_PUBLIC_DNS>
```

After connecting, the terminal displayed the Amazon Linux banner and a prompt beginning with:

```text
[ec2-user@... ~]$
```

This confirmed that commands in that terminal were running on EC2.

My VS Code editor still showed local Mac files. Running SSH inside its terminal did not automatically make the entire editor a remote workspace.

## 4. Running NGINX

NGINX ran on the EC2 instance and served its default page over HTTP.

For reference, the standard Amazon Linux 2023 commands for installing, starting and checking NGINX are below. These are reference commands rather than a verified transcript of my installation:

```bash
sudo dnf install nginx -y
sudo systemctl start nginx
sudo systemctl status nginx
```

To enable automatic startup after a reboot:

```bash
sudo systemctl enable nginx
```

A running EC2 instance alone does not provide a website. NGINX must also be running, listening on the required port and reachable through the network's security controls.

## 5. Testing the Public IP

I visited the instance's public IPv4 address directly:

```text
http://16.171.197.250
```

The NGINX default page loaded.

This confirmed that the web server was reachable over HTTP through that address at the time of testing. It also gave me a useful baseline before troubleshooting DNS.

The address above was used during the lab. An automatically assigned EC2 public IPv4 address can change after the instance is stopped and started.

## 6. Configuring DNS in Cloudflare

I created an A record intended to point my domain to the EC2 public IPv4 address.

The intended configuration was:

| Field | Value |
|---|---|
| Type | A |
| Name | @ |
| IPv4 address | 16.171.197.250 |
| Proxy status | Proxied |

The `@` symbol represents the root domain, `zqkyr.co.uk`.

### Incorrect hostname

My first record created:

```text
zqkyr.zqkyr.co.uk
```

However, I was visiting:

```text
zqkyr.co.uk
```

These are different DNS names. I corrected the record's Name field to `@`.

This showed why the record name matters just as much as its type and value.

## 7. Troubleshooting DNS

The website loaded through the public IP but failed through the domain.

The browser displayed:

```text
DNS_PROBE_FINISHED_NXDOMAIN
```

I checked the domain using:

```bash
nslookup zqkyr.co.uk
```

The output identified my configured resolver:

```text
Server:  194.168.4.100
Address: 194.168.4.100#53
```

It then reported:

```text
Non-authoritative answer:
*** Can't find zqkyr.co.uk: No answer
```

The `Server` address was the DNS resolver being queried, not my EC2 instance or the domain's destination address.

Also, “No answer” and `NXDOMAIN` are not identical DNS results: a name can exist without having the requested address record.

### Comparing resolvers

I queried Cloudflare's public resolver explicitly:

```bash
nslookup zqkyr.co.uk 1.1.1.1
```

After the record correction, this returned addresses while my usual resolver still returned no address answer.

The difference was consistent with cached DNS information at my usual resolver. Comparing resolvers helped narrow the problem instead of repeatedly changing a working web-server configuration.

### Why the IP worked while the domain failed

Using the public IP directly skipped DNS:

```text
Public IP -> EC2 -> NGINX
```

Using the domain required successful resolution first:

```text
Domain -> DNS lookup -> Destination -> NGINX
```

The successful IP test showed that HTTP access worked. The domain failure pointed the investigation towards DNS.

## 8. Git and Documentation

I created an assignment README and used Git to commit and push it:

```bash
touch README.md
git add README.md
git commit -m "Assignment overview"
git push
```

I learned that:

- `git add` stages selected changes.
- `git commit` records them locally.
- `git push` uploads commits to GitHub.
- Ignoring an untracked key prevents accidental staging, but does not remove a key already committed.

The `.gitignore` file should also be committed so its rules are preserved in the repository.

## Results and Remaining Verification

Confirmed during the project:

- EC2 was running.
- SSH access succeeded.
- The NGINX default page loaded through the public IPv4 address.
- The incorrect DNS hostname was identified and corrected.
- A lookup through `1.1.1.1` returned addresses after the correction.
- Git correctly ignored the PEM file.

Still to document:

- Final successful browser access through `http://zqkyr.co.uk`.
- Replacement of the exposed SSH key and removal of its old access.
- Screenshots of the final DNS configuration and working domain.

## Key Lessons

- EC2 is the computer; NGINX is software running on it.
- DNS resolution and web-server availability are separate.
- Public and private IP addresses serve different network purposes.
- Security groups control permitted traffic; they do not start services.
- An A record points a hostname to an IPv4 address.
- Cloudflare-proxied records may resolve to Cloudflare addresses.
- DNS caching can make different resolvers temporarily return different results.
- Testing the public IP directly can help separate DNS issues from HTTP connectivity issues.
- Private keys must remain private and excluded from version control.

## Resource Cleanup

After the lab, resources should be reviewed to avoid unnecessary usage.

Stopping EC2 makes the website unavailable, and starting it again may assign a different public IPv4 address. If that happens, the A record must be updated.

Stopping an instance does not necessarily remove all associated costs, such as retained storage. Resources no longer needed should be deleted after saving the required documentation.
