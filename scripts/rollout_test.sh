#!/usr/bin/env bash
set -euo pipefail

lerobot-rollout \
--robot.type=so101_follower \
--robot.port=/dev/tty.usbmodem5B7B0090071 \
--robot.id=follower_01 \
--robot.cameras="{ top: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}, front: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30} }" \
--policy.path=Fabyo04/act_so101_cube_v3_050 \
--policy.n_action_steps=100 \
--device=mps \
--fps=30 \
--task="Pick up the cube and place it in the bowl" \
--duration=45