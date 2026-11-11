# KB-0029: Microsoft 365 Apps shows "Unlicensed Product" or "Product Deactivated"

| Field | Value |
| --- | --- |
| Applies to | Microsoft 365 Apps (Word, Excel, Outlook, PowerPoint) on Windows 11 with work or school accounts |
| Audience | Service desk (license assignment, licensing groups, proxy/firewall, shared computer activation: Microsoft 365 admin / network team) |
| Last reviewed | 2026-11-11 |

## Symptom
- Title bar shows **Unlicensed Product** or a bar reads **Product Deactivated**; files open and print but cannot be edited or created (reduced functionality mode).
- "We couldn't find any Office products" after sign-in, or a sign-in / activate prompt every time an app opens.

## Cause
- Identity: wrong account signed in or cached (personal Microsoft account, old school or employer account).
- License: no license, a license without the desktop apps, a removed or changed license (licensing group move, subscription switch), or the device signed out to stay within the sign-in limit.
- PC side: wrong date/time/time zone, two copies of Office installed, Office out of date or damaged.
- Connectivity: firewall, proxy, or antivirus blocking the Office Licensing Service (must be reached at least once every 30 days).

## Resolution
1. Record the exact message, who is affected (one user or many), and what changed. If many users at once show "Product Deactivated," escalate to the Microsoft 365 admin with the start time and department.
2. In any Office app, **File > Account**: note the signed-in account and product. Sign out, close all Office apps including Outlook, reopen one, and sign in with the work account.
3. Ask the user to sign in to the Microsoft 365 portal and check that desktop apps are offered for install. If not, escalate license assignment to the admin.
4. If the user has many devices, check their devices list on the account page and sign out unused ones (remote sign-out can take up to 72 hours).
5. Check **Set time automatically** / **Set time zone automatically**, confirm only one Office install, update Office, and run an Online Repair if needed.
6. **Credential Manager > Windows credentials**: remove **MicrosoftOffice16** entries. In **Settings > Accounts > Access work or school**, disconnect an Office account that is not the Windows sign-in account. Restart and sign in again.
7. Check license state (PowerShell): `cd "C:\Program Files\Microsoft Office\Office16"` then `./vnextdiag.ps1 -action list` (check the activating email, license state, and whether shared computer activation or device-based licensing is used).
8. With a technician account and after saving the user's work: `./vnextdiag.ps1 -action remove -LicenseId <EWW...>`, or reset fully with `OLicenseCleanup.vbs` (elevated) or `GetHelpCmd.exe -S ResetOfficeActivation -AcceptEula -CloseOffice`. Then sign in again.

## If this does not work
- Escalate to the Microsoft 365 admin with: exact message, signed-in account from **File > Account**, `vnextdiag.ps1 -action list` output, steps already tried, and whether other users are affected.
- For proxy or firewall blocks, escalate to the network team with the licensing URLs from the activation troubleshooting article.
- For shared computer activation or device-based licensing devices, escalate to whoever manages that deployment.

## Do not
- Reinstall Office before checking the signed-in account and license.
- Lower User Account Control or edit the Office Identity registry key on a managed PC without the IT team's procedure; escalate instead.
- Change proxy or firewall settings yourself; send the licensing URLs to the network team.

## How to verify
- **File > Account** shows the work account and the Microsoft 365 Apps product; the user can edit and save a document.

## References
- Unlicensed Product and activation errors in Office: https://support.microsoft.com/en-us/microsoft-365-activation-licensing/office-install/unlicensed-product-and-activation-errors-in-office
- Microsoft 365 Apps activation Unlicensed product error: https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/activation/unlicensed-product-error
- Overview of licensing and activation in Microsoft 365 Apps: https://learn.microsoft.com/en-us/microsoft-365-apps/licensing-activation/overview-licensing-activation-microsoft-365-apps
- Check the license and activation status for Microsoft 365 Apps (vnextdiag.ps1): https://learn.microsoft.com/en-us/microsoft-365-apps/licensing-activation/vnextdiag
- Reset activation state for Microsoft 365 Apps for enterprise: https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/activation/reset-activation-state
- Users might receive a Product Deactivated error in Microsoft 365 Office apps: https://support.microsoft.com/en-us/office/users-might-receive-a-product-deactivated-error-in-microsoft-365-office-apps-6ee29463-20bd-4fd9-afdc-caa550770f6a
- Troubleshoot issues when activating Office from Microsoft 365: https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/activation/issue-when-activate-office-from-office-365
