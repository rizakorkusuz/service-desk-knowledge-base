# KB-0005: Password reset and account unlock (service desk procedure)

| Field | Value |
| --- | --- |
| Applies to | Active Directory and Microsoft 365 accounts |
| Audience | Service desk |
| Last reviewed | 2026-10-15 |

## Symptom
A user cannot sign in because they forgot their password, it expired, or the account is locked.

## Cause
Forgotten or expired password, repeated failed sign-ins, or an old saved password on another device or app.

## Resolution
1. **Verify identity first** using the department's procedure, for example a call-back to the number in the directory, or manager approval. Never rely on an email request alone.
2. Check the account is enabled and not locked for another reason. If it is disabled, stop and find out why.
3. Reset the password with a unique temporary value and tick **User must change password at next logon**. Unlock the account if needed.
4. Give the temporary password only through the approved channel. Never write it in the ticket.
5. Tell the user to update saved credentials on other devices: phone email, Wi-Fi, mapped drives, VPN and Teams.
6. If lockouts repeat, look for the source (old phone, mapped drive, scheduled task) and escalate to security if the source is unknown.
7. Record who was verified, how, and the time. Do not record the password.

## How to verify
The user signs in and is prompted to set a new password.

## If this does not work
Escalate to the identity team with the username, the lockout source (if known) and the verification record.
