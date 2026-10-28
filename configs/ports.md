# Porte seriali

| Ruolo    | Porta                        | ID          | Alimentatore |
|----------|------------------------------|-----------  |--------------|
| Leader   | /dev/tty.usbmodem5B7B0157011 | leader_01   | 5V           |
| Follower | /dev/tty.usbmodem5B7B0090071 | follower_01 | 12V          |


Cameras:
front: 0
top: 1


  --robot.cameras="{ top: {type: opencv, index_or_path: $CAM_TOP, width: 640, height: 480, fps: 30, fourcc: MJPG}, front: {type: opencv, index_or_path: $CAM_FRONT, width: 640, height: 480, fps: 30, fourcc: MJPG} }" \