# KB-0004: Microsoft Teams microphone or camera not working

| Field | Value |
| --- | --- |
| Applies to | Teams (work or school) desktop app and Teams on the web, Windows 10/11 and macOS |
| Audience | End users, service desk, conference-room support (managed privacy settings, driver pushes, Teams meeting policy: endpoint / desktop support / Microsoft 365 admins) |
| Last reviewed | 2026-11-13 |

## Symptom
- In a Teams call others cannot hear you or see you, or your video is black.
- Teams says no microphone or camera was found, or **Settings > Devices** shows no camera preview.

## Cause
- Muted in the meeting or on the hardware (headset boom raised, mute button, camera shutter or function key).
- Wrong speaker, microphone or camera selected in Teams (common with docks and monitors that have their own mic or speakers).
- Operating system privacy permission blocked. On Windows, Teams is a desktop app, so **Let desktop apps access your camera / microphone** must be on; some Windows 11 updates remove default camera access for some apps.
- Another app holding the device; Bluetooth device connected to another device or out of battery; loose cable.
- Mic disabled or muted in Windows sound settings; device disabled or in error in Device Manager; driver problem.
- Teams meeting policy (IP audio / IP video) or blocked network ports, when the device works everywhere else.

## Resolution
1. Record: mic, camera or both; desktop app or web; built-in, USB or Bluetooth; when it started (after an update, a new headset or dock?).
2. Check the physical device: not muted in the meeting controls or on the headset, cable seated, headset charged and not paired to a phone, camera shutter open. Unplug and replug.
3. Close other apps that may hold the device (other meeting apps, browser tabs, recording tools).
4. In Teams choose **Settings and more > Settings > Devices** and select the correct speaker, microphone and camera. During a meeting: dropdown next to **Mic > More audio settings**.
5. Use **Make a test call** (Settings > Devices; not available in Teams on the web).
6. Windows: **Settings > Privacy & security > Camera** and **> Microphone**: Camera / Microphone access, Let apps access, Microsoft Teams (work or school), and **Let desktop apps access** all on. If already on, toggle off and on, close apps, restart. macOS: **System Settings > Privacy & Security > Microphone / Camera** and enable Teams, then restart Teams.
7. Windows mic: **Settings > System > Sound > Input**: correct mic selected and volume not muted. **Advanced > More sound settings > Recording**: right-click the mic, **Enable**.
8. Open the Windows **Camera** app. Works there but not in Teams: Teams settings. Fails everywhere: device or driver. Try another USB port, and test the device on another computer.
9. Restart the computer (a restart, not wake from sleep).
10. Device Manager (if your role allows): **Cameras** / **Sound, video and game controllers**. Enable a disabled device; for a device in error, remove it and scan for hardware changes; roll back a recently updated driver.

## How to verify
The test call plays back your recording clearly, the microphone level moves, and the camera preview shows video.

## If this does not work
- Privacy toggle greyed out or "managed by your organization": endpoint management team.
- Device missing or in error after restart and replug: desktop support (hardware swap or driver push), with the device model, OS version and Teams version.
- Test call works but real meetings fail, or a whole group or room is affected: Microsoft 365 / Teams admins (meeting policy, network ports), with meeting time and user.

## Do not
- Try to bypass a managed (greyed-out) privacy setting through the registry or local policy.
- Reinstall Teams or swap hardware before checking mute, device selection and privacy toggles.
- Install drivers from unofficial download sites.

## Sources
- Microsoft Support, My microphone isn't working in Microsoft Teams: https://support.microsoft.com/en-us/teams/meetings/my-microphone-isn-t-working-in-microsoft-teams
- Microsoft Support, My camera isn't working in Microsoft Teams: https://support.microsoft.com/en-us/teams/meetings/my-camera-isn-t-working-in-microsoft-teams
- Microsoft Support, Camera doesn't work in Windows: https://support.microsoft.com/en-us/windows/hardware/camera/camera-doesn-t-work-in-windows
- Microsoft Learn, Troubleshoot audio and video devices: https://learn.microsoft.com/en-us/training/modules/configure-troubleshoot-microsoft-teams-clients-services/4-troubleshoot-audio-video-devices
