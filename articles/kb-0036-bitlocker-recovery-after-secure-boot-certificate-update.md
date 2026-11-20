# KB-0036: BitLocker recovery after Secure Boot certificate update (one-time prompt or recovery loop)

| Field | Value |
| --- | --- |
| Applies to | Windows 10 (ESU) and Windows 11 23H2/24H2/25H2 devices with BitLocker and Secure Boot, during the 2023 Secure Boot certificate update |
| Audience | Service desk (firmware settings, Secure Boot policy, PXE and recovery media: Tier 2 / desktop engineering) |
| Last reviewed | 2026-11-20 |

## Symptom
- The BitLocker recovery screen appears after a Windows update or BIOS update, with no hardware change.
- After the recovery key is entered, Windows starts, but the prompt may return on every restart.
- **Windows Security > Device security > Secure Boot** says "Secure Boot is on, but your device is using an older boot trust configuration that should be updated."
- System log shows **TPM-WMI** Event ID 1801 (certificates not yet applied to firmware) or 1032 (update not applied because of the BitLocker configuration).
- Worst case: a firmware Secure Boot violation and Windows does not start.

## Cause
- Microsoft is replacing the 2011 Secure Boot certificates (expiring June 24, June 27 and October 19, 2026) with 2023 certificates. The change alters startup measurements the TPM checks.
- One-time recovery: on the first boot after the update the firmware has not yet reported the new values when BitLocker reseals.
- Recovery on every boot: network (PXE) boot is tried before the Windows disk, so 2011-signed and 2023-signed boot paths are measured in one boot.
- HP commercial PCs after BIOS updates released in early April 2026: the 2023 certificates fail to apply (`UEFICA2023Status` stays In Progress, `UEFICA2023Error` greater than 0).
- No boot after "reset Secure Boot to defaults": the reset removed the 2023 certificate the new boot manager needs.

## Resolution
1. Verify the caller per policy, record the device name and the first 8 characters of the Key ID, and provide the recovery key from Entra ID, Intune or Active Directory (never paste the key into the ticket).
2. Ask the user to restart once. If no prompt appears, record it as a one-time recovery after the Secure Boot update, check for an OEM firmware update, and follow the key rotation procedure.
3. If the prompt returns on every boot, check the firmware boot order: put **Windows Boot Manager** first and disable PXE boot if the team standard allows. If PXE is required, escalate (the PXE server needs a 2023-signed boot loader).
4. On HP commercial PCs: press **F10** at startup, open **Security > Secure Boot Configuration**, enable the four certificate settings listed in HP's document, then **Save Changes and Exit**. Suspend BitLocker first if the change is pushed remotely.
5. If Event 1032 is logged, from an elevated prompt run `manage-bde -protectors -disable %systemdrive% -RebootCount 2`, restart twice, then confirm with `manage-bde -protectors -enable %systemdrive%` (local admin and team change rules required).
6. Check status in elevated PowerShell: `Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\SecureBoot\Servicing" | Select UEFICA2023Status, UEFICA2023Error` and `Get-SecureBootUEFI -Name db -Decoded | Select Subject, ValidTo`.
7. Confirm the `\Microsoft\Windows\PI\Secure-Boot-Update` task is Ready: `schtasks.exe /Query /TN "\Microsoft\Windows\PI\Secure-Boot-Update" /FO LIST /V`.
8. Do not reset Secure Boot to factory defaults and do not edit `AvailableUpdates`; escalate instead.

## How to verify
- Two consecutive restarts complete without a BitLocker recovery prompt.
- `manage-bde -status C:` shows Protection On.
- `UEFICA2023Status` reads `Updated`, or Event ID 1808 is logged in the System log.

## If this does not work
Escalate to Tier 2 / desktop engineering with: device name, make, model and BIOS version, Key ID (first 8 characters, never the key), how often recovery occurs, boot order, `UEFICA2023Status` / `UEFICA2023Error` / `AvailableUpdates` values, recent TPM-WMI event IDs (1032, 1795, 1801, 1802, 1803, 1808) and the steps already tried. Escalate immediately if the device shows a Secure Boot violation, several devices of the same model are affected, or the recovery key cannot be found.

## References
- Secure Boot troubleshooting guide (KB5085046): https://support.microsoft.com/en-us/servicing/os/secure-boot/2026/03/secure-boot-troubleshooting-guide
- Secure Boot DB and DBX variable update events: https://support.microsoft.com/en-us/servicing/os/windows/2022/06/secure-boot-db-and-dbx-variable-update-events
- Windows Secure Boot certificate expiration and CA updates: https://support.microsoft.com/en-us/servicing/os/secure-boot/2025/06/windows-secure-boot-certificate-expiration-and-ca-updates
- Secure Boot certificate update status in the Windows Security app: https://support.microsoft.com/en-us/servicing/os/secure-boot/2026/03/secure-boot-certificate-update-status-in-the-windows-security-app
- HP: Computer stuck in BitLocker recovery loop after updating BIOS: https://support.hp.com/us-en/document/ish_14914515-14914500-16
- Find your BitLocker recovery key: https://support.microsoft.com/en-us/windows/find-your-bitlocker-recovery-key-6b71ad27-0b89-ea08-f143-056f5ab347d6
