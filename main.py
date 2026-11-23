# One-Line Roast entrypoint: copy the pre-written entry.txt into the
# directory named by MAKEFUN_OUTPUT_DIR (default "out").
#
# It is deliberately standard-library-only (os + shutil): the grader runs
# this file with no third-party packages available, so the program must
# not import anything beyond the stdlib, must not touch the network, and
# must not write anything into its own directory. All the work is done
# up front in entry.txt; this file just delivers it byte for byte.
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
