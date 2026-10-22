# KB-0010: BitLocker recovery screen asks for a recovery key at startup

| Field | Value |
| --- | --- |
| Applies to | Windows 10/11 devices with BitLocker, keys stored in Microsoft Entra ID, Intune or Active Directory |
| Audience | Service desk |
| Last reviewed | 2026-10-21 |

## Symptom
At startup the device shows a blue **BitLocker recovery** screen asking for a 48-digit recovery key instead of the Windows sign-in screen. The screen shows a **Key ID**.

## Cause
The TPM did not release the key because something in the startup chain changed. Common triggers: a BIOS/UEFI firmware update without BitLocker suspended, Secure Boot or TPM setting changes, booting from USB, a dock or the network, a hardware repair, or too many wrong startup PIN attempts.

## Resolution
1. **Verify the caller's identity** with the same procedure used for password resets. Confirm the device belongs to them.
2. Record the device name and the first eight characters of the Key ID in the ticket.
3. Look up the recovery key by device name or Key ID: Microsoft Entra admin center (device > BitLocker keys), Intune admin center (device > Recovery keys), or Active Directory Users and Computers (BitLocker Recovery tab, requires RSAT).
4. Ask what changed before the restart (update, dock, USB boot, repair) and note the likely trigger.
5. Read the key to the user one 6-digit block at a time and let them confirm each block. **Never write the key in the ticket, chat or email.**
6. After Windows starts, run `manage-bde -status C:` from an admin prompt and confirm protection is on.
7. Rotate the used key (automatic rotation, or a device action in Intune) or flag the ticket so the team can rotate it.

## How to verify
The device restarts to the normal Windows sign-in screen without asking for a key, and `manage-bde -status C:` shows Protection On.

## If this does not work
If the key is not found, or the recovery screen returns after every restart, escalate to the endpoint or security team with the device name, Key ID, verification record, likely trigger and the `manage-bde -status` output. Do not reinstall Windows; that erases the user's data.

## Prevention
Before a planned firmware update, suspend protection for one restart: `manage-bde -protectors -disable C: -RebootCount 1` or `Suspend-BitLocker -MountPoint "C:" -RebootCount 1`.

## References
- https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/recovery-process
- https://support.microsoft.com/en-us/windows/find-your-bitlocker-recovery-key-6b71ad27-0b89-ea08-f143-056f5ab347d6
