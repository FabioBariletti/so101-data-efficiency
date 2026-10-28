#!/usr/bin/env bash
set -euo pipefail

FOLLOWER_PORT="/dev/tty.usbmodem5B7B0090071"
LEADER_PORT="/dev/tty.usbmodem5B7B0157011"
CAM_TOP=0
CAM_FRONT=1
HF_USER="Fabyo04"
DATASET_ROOT="$HOME/robot_data/so101_cube_v3" 

lerobot-record \
--robot.type=so101_follower \
--robot.port="$FOLLOWER_PORT" \
--robot.id=follower_01 \
--robot.cameras="{ top: {type: opencv, index_or_path: $CAM_TOP, width: 640, height: 480, fps: 30}, front: {type: opencv, index_or_path: $CAM_FRONT, width: 640, height: 480, fps: 30} }" \
--teleop.type=so101_leader \
--teleop.port="$LEADER_PORT" \
--teleop.id=leader_01 \
--dataset.repo_id="$HF_USER/so101_cube_v3" \
--dataset.root="$DATASET_ROOT" \
--dataset.num_episodes=5 \
--dataset.no_stamp=true \
--dataset.episode_time_s=16 \
--dataset.reset_time_s=10 \
--dataset.streaming_encoding=true \
--dataset.encoder_threads=2 \
--dataset.rgb_encoder.vcodec=auto \
--dataset.single_task="Pick up the cube and place it in the bowl" \
--resume=true \