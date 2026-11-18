# KB-0034: Password expired while working remotely (VPN, SSPR and cached credentials)

| Field | Value |
| --- | --- |
| Applies to | Windows 10/11 laptops joined to on-premises Active Directory or Microsoft Entra hybrid joined, hybrid accounts synchronized to Microsoft Entra ID, remote users with a VPN client |
| Audience | Service desk (password writeback, VPN and password policy changes: Tier 2 / identity team) |
| Last reviewed | 2026-11-18 |

## Symptom
- The user can still sign in to the laptop with the old password, but the VPN, Outlook, Teams or the web portal rejects it.
- "Your password has expired and must be changed" on the web sign-in page or VPN client.
- After resetting the password on the web, the new password does not work at the Windows sign-in screen.
- Windows shows "You've been logged on using cached account information".

## Cause
- The laptop signs in with cached credentials when no domain controller can be reached, and the cached copy still holds the old password.
- The password expiry warning appears only when the user logs on to the domain, so a user who has been off the network may never see it.
- A new password set in the cloud (SSPR) reaches the laptop only after the laptop can contact a domain controller (internal network or VPN).
- For hybrid accounts, self-service reset requires password writeback; without it the user is told to contact the administrator.

## Resolution
1. Record which sign-in fails (Windows, VPN, Outlook, web), the exact error text, where the user is, and whether they already changed the password anywhere.
2. Check the account in Active Directory: expired, locked, or both. Unlock if needed, following the account unlock procedure.
3. **Not yet expired:** have the user connect to the VPN, press **Ctrl + Alt + Delete > Change a password**, then lock (**Windows + L**) and unlock with the new password while still connected.
4. **Expired, user registered for SSPR:** the user resets the password at https://aka.ms/sspr from any browser and verifies with a registered method.
5. **SSPR not available** ("not enabled", "could not verify your account", or "not managed by Microsoft"): verify identity with the approved method, reset the password, and give the temporary value only through the approved channel. Never record it in the ticket. Check the team's procedure before ticking "User must change password at next logon" for a user who cannot reach a domain controller.
6. Sync the laptop: sign in to Windows with the **old** password, connect the VPN with the **new** password (if the VPN uses the same account), lock and unlock with the new password, then restart and test while connected.
7. Ask the user to update every saved copy of the old password, including phone mail and Teams apps, work Wi-Fi profiles, Windows Credential Manager entries, and other devices.
8. If the user is not registered for SSPR, ask them to register at https://aka.ms/mysecurityinfo once signed in.

## How to verify
- The new password works at the Windows sign-in screen, on the VPN, and in Outlook and Teams.
- The account shows no new lockouts for at least 30 minutes after the change.

## If this does not work
Escalate to Tier 2 / identity team with: username, account status (expired/locked), the time and method of the reset (SSPR or service desk), any SSPR error text, the VPN client error, and the lockout source if the account keeps locking. Do not include the password.

## References
- Self-service password reset for Windows devices: https://learn.microsoft.com/en-us/entra/identity/authentication/howto-sspr-windows
- Self-service password reset deep dive: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks
- On-premises password writeback with self-service password reset: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-writeback
- Interactive logon: Number of previous logons to cache: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/interactive-logon-number-of-previous-logons-to-cache-in-case-domain-controller-is-not-available
- Interactive logon: Prompt user to change password before expiration: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/interactive-logon-prompt-user-to-change-password-before-expiration
- Register the password reset verification method for a work or school account: https://support.microsoft.com/en-us/accounts-billing/work-school/register-the-password-reset-verification-method-for-a-work-or-school-account

## See also

- [KB-0005: Password reset and account unlock](kb-0005-password-reset.md)
- [KB-0025: Account keeps getting locked out](kb-0025-repeated-account-lockouts.md)
- [Password expired while working remotely (full guide)](https://rizakorkusuz.com/articles/password-expired-remote-user-sspr-vpn-cached-credentials-service-desk/)
