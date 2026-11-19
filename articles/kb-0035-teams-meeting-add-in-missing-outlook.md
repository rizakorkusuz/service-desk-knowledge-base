# KB-0035: Teams Meeting button missing in Outlook (classic and new Outlook)

| Field | Value |
| --- | --- |
| Applies to | Windows 10/11, Microsoft 365 Apps (classic Outlook) and new Outlook for Windows, new Microsoft Teams desktop app |
| Audience | Service desk (registry, Group Policy and Exchange changes: Tier 2 / messaging team) |
| Last reviewed | 2026-11-19 |

## Symptom
- The **Teams Meeting** button is missing from the Outlook calendar ribbon or the new event window.
- New Outlook shows no **Teams meeting** toggle in the event window.
- Classic Outlook shows "Microsoft Teams Meeting Add-in for Microsoft Office" under **Disabled** or **Inactive Application Add-ins**.
- A delegate's Teams meeting invite has no join link, meeting ID or dial-in numbers.

## Cause
- New Outlook does not use the Teams COM add-in; its built-in toggle needs the new Teams app signed in with the same work or school account.
- Classic Outlook disabled the add-in because it slowed startup, running or shutdown (Event ID 59 in the Application log).
- The add-in loader is not registered, or the Teams desktop app is not installed (Teams on the web only).
- The add-in stopped loading after classic Teams was removed and new Teams was installed.
- For delegates: the manager's mailbox is hidden from the global address list (GAL).

## Resolution
1. Record which Outlook (classic or new), the Office build, whether the new Teams desktop app is installed and signed in, and when the button disappeared.
2. **New Outlook:** confirm Outlook and Teams use the same work account, then close Outlook, right-click the Teams icon and choose **Quit Teams**, start Teams and sign in, then start Outlook.
3. **Classic Outlook:** go to **File > Options > Add-ins**. If the add-in is disabled, choose **Manage: COM Add-ins > Go**, tick it, select **OK** and restart Outlook.
4. If Outlook keeps disabling it, check **File > Slow and Disabled COM Add-ins** and the Application log (Event ID 45 and 59). Ask Tier 2 before choosing **Always enable this add-in**.
5. Make sure Office is up to date (**File > Office Account > Update Options > Update Now**).
6. If the add-in is not listed at all, quit Outlook and Teams and re-register `Microsoft.Teams.AddinLoader.dll` from the highest version folder in `%LocalAppData%\Microsoft\TeamsMeetingAddin` with `regsvr32.exe /n /i:user` (System32 for 64-bit Office with the x64 DLL, SysWOW64 for 32-bit Office with the x86 DLL), following the team's admin-rights rules. Restart Teams, sign out and in, then start Outlook normally.
7. After a move from classic to new Teams: uninstall the old add-in with Microsoft's script for that version, start new Teams, wait until the add-in appears in **Settings > Apps > Installed apps**, then restart Outlook.
8. Delegate invite without a join link: escalate to the messaging team to check whether the manager's mailbox is hidden from the GAL.

## How to verify
- The Teams Meeting button (classic) or Teams meeting toggle (new Outlook) is visible.
- A test meeting created in Outlook contains a working Teams join link.

## If this does not work
Escalate to Tier 2 / messaging team with: username, Outlook type and Office build, Teams version, the add-in version from Installed apps, its status in COM Add-ins, any Event ID 59 details, and the steps already tried. Registry (`LoadBehavior`, trusted add-ins policy) and Exchange changes are Tier 2 work.

## References
- Fix Teams Meeting add-in problems in Classic Outlook: https://learn.microsoft.com/en-us/troubleshoot/microsoftteams/meetings/resolve-teams-meeting-add-in-issues
- Teams Meeting add-in missing in new Outlook: https://support.microsoft.com/en-us/outlook/teams-meeting-add-in-missing-in-new-outlook
- Add-ins are user re-enabled after being disabled: https://learn.microsoft.com/en-us/troubleshoot/outlook/performance/add-ins-are-user-re-enabled-after-being-disabled
- Add-in warnings in classic Outlook for Windows: https://support.microsoft.com/en-us/outlook/outlook-add-in-warnings
