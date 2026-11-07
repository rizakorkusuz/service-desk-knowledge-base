# KB-0025: Account keeps getting locked out (repeated lockouts)

| Field | Value |
| --- | --- |
| Applies to | Active Directory domain accounts on Windows 10/11, and Microsoft 365 sign-ins protected by Microsoft Entra ID smart lockout |
| Audience | Service desk (domain controller logs, lockout policy, Netlogon logging and Entra sign-in logs: identity / server team; unknown sources: security) |
| Last reviewed | 2026-11-07 |

## Symptom
- User is locked out again shortly after being unlocked, often after a recent password change.
- Lockouts repeat on a rhythm (every few minutes, hourly, every morning).
- On a Microsoft 365 sign-in page: "Your account is temporarily locked to prevent unauthorized use."

## Cause
- A device or app still using the old password, such as a phone or tablet mail app, saved Credential Manager entry, mapped drive with saved credentials, second PC, disconnected RDP session, Wi-Fi profile using domain credentials.
- A scheduled task or service configured to run as the user's account.
- User retrying an old password after a change, or a password change that has not synced yet.
- Password guessing or spraying from an unknown source (security event).

## Resolution
1. Verify the user's identity per procedure. Note which sign-in fails: on-premises (Windows, share, VPN) or Microsoft 365.
2. Check state: `Get-ADUser <user> -Properties LockedOut, badPwdCount, lastBadPasswordAttempt, PasswordLastSet` or `Search-ADAccount -LockedOut`.
3. Unlock once: `Unlock-ADAccount -Identity <user>`. Do not unlock in a loop without finding the source.
4. Request (or, with rights, read) event 4740 on the PDC emulator and record the **Caller Computer Name** and times.
5. If the caller is a known user device: update or remove the stale password on that device (phone mail, Credential Manager entry, mapped drive, RDP session, Wi-Fi profile).
6. If the caller is blank or a server (Exchange, RADIUS, app server): escalate to the identity / server team; events 4771/4776 and Netlogon logging may be needed.
7. If the source is unknown or external, or several accounts lock together: escalate to security as a possible password spray.
8. Do not raise the lockout threshold, disable lockout, or clear all saved credentials on the PC.

## How to verify
- `LockedOut` stays false and `badPwdCount` does not climb over the next few hours, and the user confirms each device signs in with the new password.

## If this does not work
Escalate to the identity team with: user, verification method, lockout times, `Get-ADUser` lockout fields, 4740 Caller Computer Name (if known), devices and apps already updated, and whether other accounts are affected. Unknown or external sources go to security.

## References
- Microsoft Learn, 4740(S) A user account was locked out: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4740
- Microsoft Learn, Troubleshoot account lockout in Microsoft Entra Domain Services: https://learn.microsoft.com/en-us/entra/identity/domain-services/troubleshoot-account-lockout
- Microsoft Learn, Prevent attacks using smart lockout: https://learn.microsoft.com/en-us/entra/identity/authentication/howto-password-smart-lockout
- Microsoft Learn, Unlock-ADAccount: https://learn.microsoft.com/en-us/powershell/module/activedirectory/unlock-adaccount
- Microsoft Support, Credential Manager in Windows: https://support.microsoft.com/en-us/windows/credential-manager-in-windows-1b5c916a-6a16-889f-8581-fc16e8165ac0
