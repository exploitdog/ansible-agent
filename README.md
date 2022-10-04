# Ansible Role: exploitdog agent

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) and are listed in the table
below.

| Name                                   | Default Value            | Description                                                                                                    |
|----------------------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------|
| `exploitdog_agent_url`                 | "https://exploitdog.com" | Url Address                                                                                                    |
| `exploitdog_agent_token`               | ""                       | Agent token                                                                                                    |
| `exploitdog_agent_proxy`               | ""                       | Url proxy, must be supported [http connect](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/CONNECT) |
| `exploitdog_agent_duration`            | "8h"                     | Frequency of data collection, '4h', '8h', '16h', '24h'                                                         |
| `exploitdog_agent_enabled_collectors`  | []                       | List of additionally enabled collectors. It adds collectors to those enabled by default                        |
| `exploitdog_agent_disabled_collectors` | []                       | List of disabled collectors.                                                                                   |

## Collectors

| Name          | Default Enabled | Description                          |
|---------------|-----------------|--------------------------------------|
| host-info     | ✔               | Host info, not recommended to unlock |
| cpu           | ✔               | CPU info                             |
| disk          | ✔               | Disk info                            |
| memory        | ✔               | Memory info                          |
| net-interface | ✔               | Information about network interfaces |
| net-port      | ✔               | information about open ports         |
| package       | ✔               | Information about installed packages |

## Example

### Playbook

Use it in a playbook as follows:

```yaml
- hosts: all
  roles:
    - exploitdog.exploitdog_agent
```

## Local Testing

The preferred way of locally testing the role is to use Docker
and [molecule](https://github.com/ansible-community/molecule) (v3.x). You will have to install Docker on your system.
See "Get started" for a Docker package suitable for your system. Running your tests is as simple as
executing `molecule test`.