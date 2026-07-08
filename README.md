Edit the claude_desktop_config.json to this: 

```
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "<path to weather.py>",
        "run",
        "weather.py"
      ]
    }
  },
  "coworkUserFilesPath": "<path to cowork user files>",
  "preferences": {
    "coworkScheduledTasksEnabled": false,
    "coworkHipaaRestricted": false,
    "ccdScheduledTasksEnabled": false,
    "bypassPermissionsGateByAccount": {
      "ff1b0752-8d25-40b0-a5d0-d05dd613446d": false
    },
    "coworkWebSearchEnabled": true,
    "coworkModelAutoFallbackByAccount": {
      "ff1b0752-8d25-40b0-a5d0-d05dd613446d": true
    },
    "remoteToolsDeviceName": "<device name>",
    "epitaxyPrefs": {
      "starred-local-code-sessions": [],
      "starred-cowork-spaces": [],
      "starred-session-groups": [],
      "dframe-local-slice": {
        "pinnedOrder": [],
        "customGroupAssignments": {},
        "customGroupOrder": {}
      },
      "ccd-sessions-filter": {
        "state": {
          "selectedProjects": []
        },
        "version": 0
      },
      "desktop-frame.paneStore.v1": {
        "state": {
          "extraPanesByMode": {},
          "colWeightsByMode": {},
          "rowSplit": 0.5,
          "draftNonce": 0
        },
        "version": 4
      }
    }
  }
}
```
