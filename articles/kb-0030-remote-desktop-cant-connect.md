# KB-0030: Remote Desktop can't connect to the remote computer (Windows 11)

| Field | Value |
| --- | --- |
| Applies to | Remote Desktop Connection (mstsc) to Windows 11 Pro / Enterprise / Education PCs |
| Audience | Service desk (firewall, DNS, Group Policy, listener and group membership changes: network / systems / access management) |
| Last reviewed | 2026-11-12 |

## Symptom
- "Remote Desktop can't connect to the remote computer for one of these reasons: remote access is not enabled, the remote computer is turned off, or it is not available on the network."
- "This computer can't connect to the remote computer."
- Or the connection reaches the PC but is refused: "Access is denied" / "The connection was denied because the user account is not authorized for remote login."

## Cause
- Target PC: powered off or asleep, Windows Home edition (can't host Remote Desktop), Remote Desktop disabled locally or by policy.
- Path: user not on VPN / office network, wrong computer name or stale DNS, non-default port, firewall rules (Remote Desktop - User Mode TCP-In / UDP-In) disabled or blocked.
- Listener: rdp-tcp not listening, TermService or UmRdpService stopped, another process holding port 3389.
- Permissions: user not in Administrators or Remote Desktop Users, or missing the "Allow log on through Remote Desktop Services" right.

## Resolution
1. Record the exact message, who is affected (one user or many), where the user is connecting from, and the name or IP they type.
2. Remote user: confirm VPN is connected first.
3. Confirm the target PC is on and awake, and is a Pro / Enterprise / Education edition with Remote Desktop enabled (**Settings > System > Remote Desktop**). If it's off by policy, escalate.
4. From a machine on the same network: `Test-NetConnection -ComputerName <PC> -Port 3389 -InformationLevel Detailed`. Note `TcpTestSucceeded`.
5. Try the IP address instead of the name. IP works but name fails: DNS issue, escalate to systems team.
6. Confirm the port (default 3389). If different, connect as `name:port`.
7. On the PC (admin): `qwinsta` and look for `rdp-tcp ... Listen`. Check that TermService and UmRdpService are running. Attach output to the ticket.
8. "Not authorized" errors: check (read-only) whether the user is in Remote Desktop Users (AD Builtin or local `lusrmgr.msc`) and whether they can sign in to the PC locally. Domain controllers allow only Domain Admins.

## If this does not work
- Port test fails on the office network: network team, with the `Test-NetConnection` output.
- Listener missing, services won't start, Remote Desktop disabled by policy, or another process on port 3389 (`tasklist /svc | findstr TermService`, `netstat -anob | findstr 3389`): systems team.
- User should have remote access but doesn't: access management, with the manager's approval.

## Do not
- Turn off the Windows Firewall or uninstall antivirus on a managed PC to "test"; hand the evidence to the network or security team.
- Edit `fDenyTSConnections` / `fEnableWinStation` in the registry on a domain PC; policy overrides it, so escalate.
- Disable Network Level Authentication or open port 3389 to the internet.
- Add users to Remote Desktop Users without approval.

## How to verify
- The user connects with Remote Desktop Connection, signs in, and sees their desktop; `Test-NetConnection` shows `TcpTestSucceeded : True`.

## References
- Remote Desktop can't connect to the remote computer: https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/remote-desktop-cannot-connect-remote-computer
- Enable Remote Desktop on your PC: https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-access
- Troubleshooting access denied and user not authorized issues in RDS: https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/troubleshooting-access-denied-and-user-not-authorized-rds-issues
