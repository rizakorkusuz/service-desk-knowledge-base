# KB-0038: Teams status stuck on Out of Office (or Away, Offline, In a meeting)

| Field | Value |
| --- | --- |
| Applies to | Microsoft Teams (new Teams desktop, web and mobile) with Microsoft 365 work or school accounts; Exchange Online mailboxes, with notes for on-premises (hybrid) mailboxes |
| Audience | Service desk (automatic-reply changes on other users' mailboxes, Graph calendar reads and hybrid presence checks: Exchange / M365 admins) |
| Last reviewed | 2026-11-22 |

## Symptom
- Teams shows **Out of Office** or **Available, Out of Office** after the user is back at work; colleagues still see the out of office message.
- Choosing **Available** manually does not stick.
- Related: stuck on **Away** while working, **Offline** while signed in, or **In a meeting** with no meeting running.

## Cause
- Automatic replies are still on (Teams and Outlook share one setting; a schedule may still be running).
- A calendar event covering today has **Show as: Out of Office**, often an accepted invite from someone else (vacation, offsite, holiday) or the event created by "Block my calendar for this period" (`CreateOOFEvent`).
- A manual status that has not expired (no duration: Appear offline = indefinitely, Busy/Do not disturb = 1 day, others = 7 days).
- Another signed-in device (phone, second PC) is the most recently active device and sets presence.
- Users can only choose a status less available than the calculated one, so a calendar or automatic-reply signal blocks Available.
- Damaged Teams client cache on one PC (status wrong only in that desktop app).
- Calendar-based presence cannot read the mailbox (on-premises/hybrid Exchange REST API, EWS blocked by policy).

## Resolution
1. Turn off automatic replies in Teams: profile picture > **Set status message** > **Schedule out of office** > turn off **Turn on automatic replies** > **Save**.
2. Confirm in Outlook: new Outlook **View > View settings > Accounts > Automatic replies**; Outlook on the web **Settings > Accounts > Automatic replies**; classic Outlook **File > Automatic Replies**.
3. Check the calendar for any current event with **Show as: Out of Office** (look at all-day and multi-day items and accepted invites). Change it to **Free** or **Tentative**, or decline/delete it.
4. In Teams: profile picture > current status > **Reset status**. Quit Teams from the notification area and reopen. Allow a few minutes (up to one hour for on-premises mailboxes).
5. Ask which devices are signed in to Teams; sign out of unused ones. For Teams on the web, consider **Settings > Notifications and activity > Presence > Keep my current status when I'm active outside of Teams on the web**.
6. If only one desktop app is wrong: **Settings > Apps > Installed apps > Microsoft Teams > Advanced options > Reset** (deletes app data and personalization; tell the user first).
7. Admin read-only check: `Get-MailboxAutoReplyConfiguration -Identity <user> | Format-List AutoReplyState, StartTime, EndTime`. Turning it off for the user (`Set-MailboxAutoReplyConfiguration -Identity <user> -AutoReplyState Disabled`, or M365 admin center **Users > Active users > Mail > Automatic replies**) is an admin change with the user's request on the ticket.
8. If the user cannot find the event, an admin with approved `Calendars.ReadBasic` access can list events where `ShowAs -eq 'oof'` with `Get-MgUserCalendarView` for a date range.
9. Run the **Teams Presence Based on Calendar Events** test in the Microsoft Remote Connectivity Analyzer (signed in as the user) and record the result.

## How to verify
- Teams shows **Available** (or the expected calculated status) on desktop, web and mobile within a few minutes.
- `Get-MailboxAutoReplyConfiguration` shows `AutoReplyState : Disabled` (or a schedule that has ended).
- A colleague confirms the out of office message no longer appears when they start a chat.

## If this does not work
Escalate to the M365 / messaging team with: user, devices signed in, status shown on each client, automatic-reply state and dates, any Out of Office events found (subject, dates, organizer), whether the mailbox is Exchange Online or on-premises, the Teams Presence Based on Calendar Events test result, and steps already tried (Reset status, restart, cache reset). Escalate as a possible service issue if several users report wrong presence at the same time.

## References
- User presence in Teams: https://learn.microsoft.com/en-us/microsoftteams/presence-admins
- The correct presence status isn't reflected in Teams: https://learn.microsoft.com/en-us/troubleshoot/microsoftteams/teams-im-presence/presence-not-show-actual-status
- Resolve interaction issues between Teams and Exchange Server: https://learn.microsoft.com/en-us/troubleshoot/microsoftteams/exchange-integration/teams-exchange-interaction-issue
- Change your status in Microsoft Teams: https://support.microsoft.com/en-us/office/change-your-status-in-microsoft-teams-ce36ed14-6bc9-4775-a33e-6629ba4ff78e
- Schedule an out of office status in Microsoft Teams: https://support.microsoft.com/en-us/teams/notifications-settings/schedule-an-out-of-office-status-in-microsoft-teams
- Clear the Teams client cache: https://learn.microsoft.com/en-us/troubleshoot/microsoftteams/teams-administration/clear-teams-cache
- Set-MailboxAutoReplyConfiguration: https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/set-mailboxautoreplyconfiguration
- Get-MgUserCalendarView: https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.calendar/get-mgusercalendarview
