# KB-0001: Outlook search returns no or incomplete results

| Field | Value |
| --- | --- |
| Applies to | Outlook for Windows (Microsoft 365 Apps), Windows 10/11 |
| Audience | End users and service desk |
| Last reviewed | 2026-10-15 |

## Symptom
Searching in Outlook shows "No results" or misses recent messages, while the messages are visible in Outlook on the web.

## Cause
The local Windows Search index is incomplete or corrupted, or Outlook is set to keep only a short window of mail offline.

## Resolution
1. Confirm the messages appear in Outlook on the web. If they do not, stop and escalate: this is not an index problem.
2. In Outlook choose **File > Options > Search > Indexing Options**.
3. Choose **Advanced > Rebuild**. Indexing can take minutes to hours on large mailboxes.
4. Confirm the **Windows Search** service is running (`services.msc`).
5. Under **File > Account Settings > Account Settings > Change**, raise **Mail to keep offline** if needed.
6. Restart Outlook and test again after indexing finishes.

## How to verify
A search for a known recent message returns it, and Indexing Status shows 0 items remaining.

## If this does not work
Create a new Outlook profile and test. Escalate to Tier 2 with the Outlook build, the profile test result and the indexing status.
