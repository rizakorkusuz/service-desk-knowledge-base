# KB-0003: Wi-Fi shows connected but there is no internet

| Field | Value |
| --- | --- |
| Applies to | Windows 10/11 and macOS on wireless networks |
| Audience | End users and service desk |
| Last reviewed | 2026-10-15 |

## Symptom
The Wi-Fi icon shows connected, but web pages and applications do not load.

## Cause
The device may have no valid DHCP lease, a wrong DNS server, a captive portal that needs sign-in, or a weak signal.

## Resolution
1. Check whether other devices on the same network work. If none do, report a network outage with the location and time.
2. Turn Wi-Fi off and on, then reconnect. Move closer to the access point.
3. Windows: run `ipconfig /all`. An address starting `169.254` means no lease: run `ipconfig /release` then `ipconfig /renew`.
4. Run `ping 1.1.1.1`. If it works but websites fail, DNS is the problem: run `nslookup example.com` and check the DNS servers, then `ipconfig /flushdns`.
5. Open a browser to a plain HTTP page to trigger any captive portal sign-in.
6. Forget the network and join it again with the correct credentials.
7. Update the Wi-Fi driver, and test with a wired connection to separate the device from the wireless network.

## How to verify
Websites and the user's applications load.

## If this does not work
Escalate to the network team with the SSID, location, `ipconfig /all` output, ping and nslookup results, and which other devices are affected.
