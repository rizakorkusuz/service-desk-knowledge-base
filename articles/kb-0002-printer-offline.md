# KB-0002: Network printer shows Offline or will not print

| Field | Value |
| --- | --- |
| Applies to | Windows 10/11 with network printers |
| Audience | Service desk and deskside support |
| Last reviewed | 2026-10-15 |

## Symptom
A printer shows **Offline**, or jobs stay in the queue and nothing prints.

## Cause
Common causes: the printer is off or has moved to a new IP address, the port or driver on the PC is wrong, the queue is stuck, or the network path is blocked.

## Resolution
1. Check the printer panel for errors (paper, jam, toner) and print a configuration page from the printer. Note its IP address.
2. From the PC, `ping <printer IP>`. No reply means a network or power problem: check the cable and port, and ask whether others can print.
3. In **Printer properties > Ports**, confirm the port points to the correct IP address. Printers should have a static or reserved address.
4. Open the print queue and cancel stuck jobs. If they will not clear, restart the Print Spooler service (with approval for the machine).
5. Confirm the approved driver is installed. Remove and re-add the printer if the port or driver is wrong.
6. Print a test page, then ask the user to print the real document.

## How to verify
The printer shows Ready and the user's document prints.

## If this does not work
Escalate with the printer name, IP, test results (ping, test page), number of affected users and the steps tried. Secure-print or print-server problems go to the print server owner.
