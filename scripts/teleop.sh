#!/usr/bin/env bash
set -euo pipefail

FOLLOWER_PORT="/dev/tty.usbmodem5B7B0090071"
LEADER_PORT="/dev/tty.usbmodem5B7B0157011"
CAM_TOP=0
CAM_FRONT=1

lerobot-teleoperate \
  --robot.type=so101_follower \
  --robot.port="$FOLLOWER_PORT" \
  --robot.id=follower_01 \
  --robot.cameras="{ top: {type: opencv, index_or_path: $CAM_TOP, width: 640, height: 480, fps: 30}, front: {type: opencv, index_or_path: $CAM_FRONT, width: 640, height: 480, fps: 30} }" \
  --teleop.type=so101_leader \
  --teleop.port="$LEADER_PORT" \
  --teleop.id=leader_01 \
  --display_data=true