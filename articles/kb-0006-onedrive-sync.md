# KB-0006: OneDrive is not syncing

| Field | Value |
| --- | --- |
| Applies to | OneDrive sync client on Windows 10/11 |
| Audience | End users and service desk |
| Last reviewed | 2026-10-15 |

## Symptom
The OneDrive icon shows a red X, a paused or sync-pending state, or files do not appear on other devices.

## Cause
Account signed out, storage full, file open in an app, invalid characters or a very long path, or a stale local state.

## Resolution
1. Click the OneDrive cloud icon and read the message. Open **View sync problems** for the failing files.
2. Confirm sign-in with the work account and that storage is not full.
3. Close apps that have the file open. Rename files with invalid characters (`" * : < > ? / \ |`) or shorten long paths.
4. Pause and resume sync.
5. If it still fails, reset OneDrive: press Windows+R and run `%localappdata%\Microsoft\OneDrive\onedrive.exe /reset`. Files are not deleted, but a full re-sync follows.
6. Compare with the OneDrive web site to confirm the files are safe in the cloud.

## How to verify
The icon shows a green check, and a test file appears on the web and on another device.

## If this does not work
Escalate with the OneDrive version, the exact sync error, and the file path.
