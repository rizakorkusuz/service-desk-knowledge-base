# KB-0009: Computer is slow

| Field | Value |
| --- | --- |
| Applies to | Windows 10/11 desktops and laptops |
| Audience | Service desk and deskside support |
| Last reviewed | 2026-10-15 |

## Symptom
The computer is slow to start, open applications or respond.

## Cause
Common causes: low free disk space, too many startup programs, pending updates, a runaway process, low memory or a failing drive.

## Resolution
1. Restart the computer (not a shutdown, because Fast Startup keeps the session).
2. Open Task Manager and sort by CPU, Memory and Disk to find a process using most of the resources.
3. Check free disk space. Under about 10% free causes trouble. Run Storage Sense. Do not delete user files without permission.
4. Review **Startup apps** in Task Manager and disable unneeded entries with the user's agreement.
5. Check for pending Windows updates or an active antivirus scan.
6. Run `Get-PhysicalDisk | Select FriendlyName,HealthStatus` to check drive health. If the drive is unhealthy, back up data and request a replacement.
7. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` if system files may be damaged.

## How to verify
Startup time and application launch time return to normal, and Task Manager shows no sustained 100% usage.

## If this does not work
Escalate for a hardware check or reimage, with Task Manager screenshots, disk space and health output, and the time the slowness started.
