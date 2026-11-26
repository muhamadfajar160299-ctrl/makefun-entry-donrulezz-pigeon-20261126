import os

# One-line pitch: StatueShield sells statue-cleaning insurance, run by the pigeons.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = "We're StatueShield, raising $2M: $9.99 a month keeps your statue spotless — insurance sold by the very flock who'd otherwise be the claim."
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
