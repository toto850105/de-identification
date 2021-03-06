# Quick Start

For convenience, we have pack the project into Docker image, which is now public on DockerHub.
In this document, we brieftly introduce the deployment model and the required parameters for launching application.

## Overview
We firstly give the intuitive deployment model by the figure below.
<img src="figures/overview.png" alt="overview" width='600'/>

## Useful management commands

### The required options
| Options    | Description |
| ------------- | ------------- |
| `-p`      | The port forwarding setting. Inside container, the application is listening on 8080 port. To visit the GUI page, one should specify his own setting to route the traffics from host into container. For example, ```-p 8888:8080``` means routing the traffics to 8888 port on host into 8080 port on the container.  |
| `-v`      | The volume attachment setting. The application can only find datasets under the directory `/opt/de-identification/static/test/` inside the container. To read the user's data, you could specify your own directory to be attached to the one in container. For example, launching container with the option ```-v /user/data/:/opt/de-identification/static/test/```, the Docker will create the directory of path `/user/data` if not existed, and attach it to the directory `/opt/de-identification/static/test/` in container for application to read. |

### The launch command
With the super user privilege of the host. Using the following command to run the application.
```
docker run -itd [Options...] robinlin/de-identification /bin/bash
```
**Note**: 
1. Replace the `[Options...]` with the *Port Forwarding* and *Volume attachment* settings.
2. After the container being launched, the system would return you the container ID.

**Example**:
```
root@ubuntu:~# docker run -itd -p 8888:8080 -v /user/data/:/opt/de-identification/static/test/ robinlin/de-identification /bin/bash
4f67c7ddff1d7a1b536b0d59b94494469d5a478d2c1c3575ec9af971276e8327
```

### The list command
After the application/coontainer being launched, you can find it's status by following command.
```
docker ps -a
```

**Note**: You could retrieve the container ID by this way.

**Example**:
```
root@ubuntu:~# docker ps -a
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS               NAMES
4f67c7ddff1d        robinlin/de-identification   "/bin/sh -c /opt/d..."   17 minutes ago      Up 17 minutes       8080/tcp            competent_chandrasekhar
8c258a74488b        ubuntu:14.04                 "/bin/bash"              2 weeks ago         Up 2 weeks                              quizzical_shaw
```

### The restart command
The Docker container would teriminate/stop when the operating system is shut down. Using the following command to restart the application.
```
docker restart [CONTAINER ID]
```


### The terminate command
To terminate the application, using the `kill` command of Docker.
```
docker kill [CONTAINER ID]
```

### The update command
To update the application, using Docker image update command and then launching another new container.

```
docker pull robinlin/de-identification
docker run -itd [Options...] robinlin/de-identification /bin/bash
```

## Next Step
After the container/application being launched, using the web browser to visit the dashboard.

**Example**:
Suppose the IP address of host machine is 140.112.42.26, and the container is spcified to listen on 8888 port, then the URL should be `http://140.112.42.26:8888`.

And read the [user guide](user_guide.md) for the tutorial of generating de-identified dataset.


