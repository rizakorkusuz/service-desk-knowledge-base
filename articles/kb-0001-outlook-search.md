# KB-0001: Outlook search returns no or incomplete results

| Field | Value |
| --- | --- |
| Applies to | Classic Outlook for Windows (Microsoft 365 Apps) and new Outlook for Windows, Windows 10/11 |
| Audience | End users and service desk |
| Last reviewed | 2026-11-16 |

## Symptom
- Searching in Outlook shows "No results", or misses recent or older messages, while the messages are visible in Outlook on the web.
- Searching a shared mailbox returns nothing.

## Cause
- Classic Outlook: the local Windows Search index is incomplete, not running, or not including Outlook; or only part of the mailbox is cached on the PC.
- New Outlook: search scope, filters, the Deleted Items setting, or the "Days of email to save" offline setting.
- Shared mailbox in classic Outlook: the **All Mailboxes** scope does not return shared mailbox results (Microsoft design limitation).

## Resolution
1. Confirm the message exists in Outlook on the web. If it does not, stop: this is a missing-mail ticket, not a search ticket.
2. Identify the client: **Settings** on the ribbon = new Outlook; no Settings = classic Outlook.
3. Classic Outlook, no results:
   - Windows 11: **Settings > Privacy & security > Searching Windows > Indexer troubleshooter**.
   - **Search Tools > Indexing Status**: note items remaining, wait 5 minutes, check again.
   - **Search Tools > Locations to Search**: all data files selected.
   - `services.msc` > **Windows Search**: Running, startup type **Automatic (Delayed Start)**.
   - Control Panel > **Indexing Options**: **Microsoft Outlook** under Included Locations; **Advanced > File Types > msg** = Index Properties and File Contents, filter **Office Outlook MSG IFilter**.
4. Classic Outlook, only after step 3: close Outlook, **Indexing Options > Advanced > Rebuild**. Tell the user it can take up to 24 hours.
5. Classic Outlook, older mail missing: **File > Account Settings > Account Settings > Change**, move **Download email for the past** further right (check free disk space first). For Deleted Items: **File > Options > Search**, include the Deleted items folder.
6. New Outlook: **Settings > General > Search** (scope, **Include deleted items**) and **Settings > General > Offline > Days of email to save**. Search each account separately (multi-account search is not supported).
7. Shared mailbox (classic): select the shared mailbox and use the **Current Folder** scope.
8. Still failing in classic Outlook: test a new Outlook profile, then Quick Repair / Online Repair of Microsoft 365 Apps.

## How to verify
- A search for a known message (sender + subject word) returns it, and classic Outlook's Indexing Status shows no items remaining.

## If this does not work
- Index stuck after step 3, MSG IFilter missing, or the Windows Search service will not stay running (may be policy-managed): Tier 2.
- Search also fails in Outlook on the web, or for several users: messaging team; check Microsoft 365 service health.
- Very large mailbox or many PST files: Tier 2 before rebuilding again.
- Escalate with: Outlook version (classic/new) and build, Indexing Status before/after, checks done, new-profile test result, exact search terms.

## Do not
- Rebuild the index as the first step or right before the user's deadline.
- Add a shared mailbox as a separate account without following the team's profile standard.

## References
- Troubleshooting Outlook search issues: https://support.microsoft.com/en-us/outlook/troubleshooting-outlook-search-issues
- Troubleshoot Windows Search performance: https://learn.microsoft.com/en-us/troubleshoot/windows-client/shell-experience/windows-search-performance-issues
- Feature comparison between new Outlook and classic Outlook: https://support.microsoft.com/en-us/outlook/getstarted/feature-comparison-between-new-outlook-and-classic-outlook

## See also

- [KB-0006: OneDrive is not syncing](kb-0006-onedrive-sync.md)
- [KB-0029: Microsoft 365 Apps shows "Unlicensed Product" or "Product Deactivated"](kb-0029-unlicensed-product-activation.md)
- [Microsoft 365, Outlook, Teams and OneDrive troubleshooting](https://rizakorkusuz.com/it-support/microsoft-365-troubleshooting/)
