# Ansible Role: exploitdog agent

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) and are listed in the table
below.

| Name                                   | Default Value            | Description                                                                                                    |
|----------------------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------|
| `exploitdog_agent_url`                 | "https://exploitdog.com" | Url Address                                                                                                    |
| `exploitdog_agent_token`               | ""                       | Agent token                                                                                                    |
| `exploitdog_agent_version`             | "1.7.0"                  | Agent version to download from the update center                                                               |
| `exploitdog_agent_build`               | ""                       | Optional: select a build by its build number instead of `exploitdog_agent_version`                             |
| `exploitdog_sa_client_id`              | ""                       | Required: service account client id used to obtain the download token                                          |
| `exploitdog_sa_client_secret`          | ""                       | Required: service account client secret used to obtain the download token                                      |
| `exploitdog_agent_proxy`               | ""                       | Url proxy, must be supported [http connect](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/CONNECT) |
| `exploitdog_agent_duration`            | "8h"                     | Frequency of data collection, '4h', '8h', '16h', '24h'                                                         |
| `exploitdog_agent_enabled_collectors`  | []                       | List of additionally enabled collectors. It adds collectors to those enabled by default                        |
| `exploitdog_agent_disabled_collectors` | []                       | List of disabled collectors.                                                                                   |
| `exploitdog_agent_log_type`            | "file"                   | Log type: "stdout", "file"                                                                                     |
| `exploitdog_agent_log_level`           | "info"                   | Log level: "debug", "info", "warning", "error"                                                                 |
| `exploitdog_agent_root_privileges`     | false                    | Start exploitdog_agent with root privileges (required for audit collector)                                     |


# Log:

## stdout:
 * `systemd` written in stdout > syslog in `SyslogIdentifier=exploitdog_agent`

## file:

Location: `/var/log/exploitdog_agent`.
Default size of log file rotation is 5mb, directory can contain maximum 10 log files

## Collectors

| Name          | Default Enabled | Description                                                |
|---------------|-----------------|------------------------------------------------------------|
| host-info     | ✔               | Host info, locked to disable                               |
| cpu           | ✔               | CPU info                                                   |
| disk          | ✔               | Disk info                                                  |
| memory        | ✔               | Memory info                                                |
| net-interface | ✔               | Information about network interfaces                       |
| net-port      | ✔               | information about open ports                               |
| package       | ✔               | Information about installed packages                       |
| audit         |                 | Audit, configuration assessment (requires root privileges) |
| baseboard     |                 | Information about baseboard (requires root privileges)     |
| bios          |                 | Information about BIOS  (requires root privileges)         |
| imginspect    |                 | Container images (requires access to the runtime socket)   |

### imginspect

The collector reads images through the docker, containerd and podman sockets. When `imginspect` is listed in
`exploitdog_agent_enabled_collectors` and `exploitdog_agent_root_privileges` is `false`, the role checks which of
`/var/run/docker.sock`, `/run/containerd/containerd.sock` and `/run/podman/podman.sock` exist on the host and adds the
agent user to the group owning each socket (for example `docker`; note that the `docker` group is equivalent to root on
that host). Sockets owned by group `root` (containerd and rootful
podman by default) cannot be granted this way: the role prints a warning, and you need either
`exploitdog_agent_root_privileges: true` or a socket group configured on the host.

## Example

### Playbook

Use it in a playbook as follows:

```yaml
- hosts: all
  roles:
    - exploitdog.exploitdog_agent
```

### Uninstall agent

```bash
ansible-playbook -i ./inventory ./agent.yaml --extra-vars='uninstall=true'
```
