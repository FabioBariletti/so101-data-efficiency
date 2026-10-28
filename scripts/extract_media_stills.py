"""Extract the photos and video stills used by the report into Report/media/.

The original phone recordings are not published; this script is run once on them and its
output (a few JPEGs) is committed, so that make_report_figures.py works from the repository alone.

Usage:
    python scripts/extract_media_stills.py --media "<Photo&Video dir>" [--ffmpeg <path>]

Needs: ffmpeg on PATH (or --ffmpeg) and macOS `sips` for the HEIC photos.
"""
import argparse
import subprocess
from pathlib import Path

MEDIA = Path(__file__).resolve().parent.parent / "Report" / "media"
GRADE = "eq=contrast=1.08:saturation=1.15"

# per recording: crop to the arm, then (timestamp in s, output name)
SUCCESS = "crop=iw*0.55:ih*0.55:iw*0.38:ih*0.18"
NEARMISS = "crop=iw*0.5:ih*0.5:iw*0.42:ih*0.22"
RETRY = "crop=iw*0.6:ih*0.6:iw*0.35:ih*0.15"
FRAMES = [
    ("mod100_pos5_succ.MOV", SUCCESS, 900, [(7, "rollout_success_1"), (9, "rollout_success_2"),
                                            (11, "rollout_success_3"), (13, "rollout_success_4")]),
    ("fail_backPros.MOV", NEARMISS, 900, [(6, "rollout_nearmiss_1"), (8, "rollout_nearmiss_2"),
                                          (10, "rollout_nearmiss_3"), (12, "rollout_nearmiss_4")]),
    ("firstFail_thenSucc.MOV", RETRY, 900, [(8, "retry_1"), (10, "retry_2"), (13, "retry_3"),
                                            (16, "retry_4"), (19, "retry_5")]),
    ("teleop_example.MOV", None, 1200, [(8, "thumb_teleop")]),
    ("mod100_pos5_succ.MOV", SUCCESS, 1200, [(11, "thumb_success")]),
    ("fail_backPros.MOV", NEARMISS, 1200, [(10, "thumb_failure")]),
    ("firstFail_thenSucc.MOV", RETRY, 1200, [(13, "thumb_retry")]),
]
# HEIC photo -> (output name, longest side); the setup photos carry hand-drawn camera arrows
PHOTOS = [
    ("SetUp2.HEIC", "setup2_photo", 1400),
    ("setup3.HEIC", "setup3_photo", 1400),
    ("setUp3_02.HEIC", "setup3_cube", 900),
    ("setup3_03.HEIC", "setup3_tips", 900),
    ("IMG_3624.HEIC", "workspace", 1800),
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--media", required=True, type=Path)
    p.add_argument("--ffmpeg", default="ffmpeg")
    a = p.parse_args()
    MEDIA.mkdir(parents=True, exist_ok=True)

    for video, crop, width, shots in FRAMES:
        vf = ",".join(x for x in [crop, f"scale={width}:-2", GRADE] if x)
        for t, name in shots:
            subprocess.run([a.ffmpeg, "-loglevel", "error", "-y", "-ss", str(t), "-i", str(a.media / video),
                            "-frames:v", "1", "-vf", vf, "-q:v", "3", str(MEDIA / f"{name}.jpg")], check=True)

    for photo, name, size in PHOTOS:
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "85", "-Z", str(size),
                        str(a.media / photo), "--out", str(MEDIA / f"{name}.jpg")],
                       check=True, capture_output=True)


if __name__ == "__main__":
    main()
