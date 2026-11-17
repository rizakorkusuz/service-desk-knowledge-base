# KB-0031: Word, Excel or PowerPoint keeps crashing or "has stopped working" (Windows 11)

| Field | Value |
| --- | --- |
| Applies to | Microsoft 365 Apps / Office 2016 and later (Click-to-Run) on Windows 11: Word, Excel, PowerPoint. Classic Outlook: see References. |
| Audience | Service desk (line-of-business add-ins, reinstalls and packaged deployments: Tier 2 / app owner) |
| Last reviewed | 2026-11-17 |

## Symptom
- "Microsoft Excel has stopped working" / "Word has stopped working" when the app starts.
- The app closes a few seconds after opening, or freezes and shows "Not Responding".
- Office asks whether to disable an add-in or start in Safe Mode.

## Cause
- A faulty or outdated add-in (application add-in or COM add-in).
- Damaged Office installation files.
- Outdated device drivers (video, printer, mouse, keyboard, dock / DisplayLink).
- A damaged file, when only one document or workbook crashes.
- Office not up to date.

## Resolution
1. Record the exact error, which app, when it crashes (startup, opening a file, printing), whether a new blank file also crashes, and what changed recently.
2. Update Office: **File > Account > Update Options > Update Now** (select **Enable Updates** first if needed).
3. Start the app in Office Safe Mode: hold **Ctrl** while opening the shortcut, or **Windows + R** and run `winword /safe`, `excel /safe` or `powerpnt /safe`. Confirm "(Safe Mode)" in the title bar.
4. Opens in Safe Mode: go to **File > Options > Add-ins**, choose the app's add-ins (or **COM Add-ins**) under **Manage**, select **Go**, uncheck **one** add-in, restart normally. Repeat until the culprit is found.
5. Check **Manage: Disabled Items** for anything Office already turned off, and record it.
6. Doesn't open even in Safe Mode: close all Office apps, then **Start > Installed apps > Microsoft 365 > ... > Modify > Quick Repair**. If still failing, run **Online Repair** (needs internet, takes longer, repairs the whole suite). Restart if prompted.
7. Still failing: run Windows Update and confirm video, printer and dock drivers are current.
8. Collect evidence: `perfmon /rel` (Reliability Monitor) and Event Viewer **Windows Logs > Application**, Event ID 1000 (faulting application, faulting module, exception code, module path). Attach to the ticket.

## If this does not work
- Suspect add-in is a business application (CRM, e-signature, document management): leave it disabled for the test only, record name and version, escalate to Tier 2 / the app owner.
- Online Repair fails, or a reinstall is needed: Tier 2, with the Event ID 1000 details and Office version/build.
- Many users crash after the same update: notify the team lead and Tier 2 straight away.

## Do not
- Reinstall Office as the first step; Safe Mode and Quick Repair keep the user's settings.
- Disable antivirus or security add-ins to "test"; send evidence to the security team.
- Permanently remove a line-of-business add-in without the app owner.
- Edit Office registry keys on a managed PC; policy and packaging control them.

## How to verify
- The app opens normally (no "(Safe Mode)" in the title bar), the user opens and saves a real file, and no new Event ID 1000 for the app appears in the Application log.

## References
- I get a "stopped working" error when I start Office applications on my PC: https://support.microsoft.com/en-us/office/lifecycle/i-get-a-stopped-working-error-when-i-start-office-applications-on-my-pc
- Open Office apps in safe mode on a Windows PC: https://support.microsoft.com/en-us/office/lifecycle/open-office-apps-in-safe-mode-on-a-windows-pc
- Repair an Office application: https://support.microsoft.com/en-us/office/lifecycle/repair-an-office-application
- The application or service crashing behavior troubleshooting guidance: https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/troubleshoot-application-service-crashing-behavior
- Outlook crashes or stops responding when used with Office 365: https://support.microsoft.com/en-us/outlook/outlook-crashes-or-stops-responding-when-used-with-office-365

## See also

- [KB-0009: Computer is slow](kb-0009-slow-computer.md)
- [KB-0029: Microsoft 365 Apps shows "Unlicensed Product"](kb-0029-unlicensed-product-activation.md)
- [Microsoft 365 troubleshooting](https://rizakorkusuz.com/it-support/microsoft-365-troubleshooting/)
