"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (<=200 chars) to /output/entry.txt: a pitch for a
bizarre startup that sounds like a joke until the business logic lands.

The pitch is assembled from four named parts so each job the sentence
has to do is visible in the code:

  setup   -- the absurd premise, stated plainly;
  product -- the odd thing actually being sold;
  payer   -- who pays, and the price they pay;
  payoff  -- why the money keeps coming (the turn from laugh to nod).

Stdlib only, no network, no randomness, deterministic.
"""

import os

# --- the pitch, part by part -------------------------------------------
SETUP = "We hire actors to haunt your Airbnb as professional ghosts"
PAYER = "hosts"  # who pays
PRICE = "$99 a night"
PAYOFF = "haunted listings book out three months in advance"


def build_pitch() -> str:
    """Join the parts into a single sentence, setup -> payoff."""
    return (
        f"{SETUP}, charging {PAYER} {PRICE} "
        f"because {PAYOFF}."
    )


def check_pitch(text: str) -> None:
    """The gate the sealed scorer applies: UTF-8, 1-200 chars, one sentence."""
    if not text or not text.strip():
        raise ValueError("pitch is empty")
    if len(text) > 200:
        raise ValueError(f"pitch is {len(text)} chars, over the 200 limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    for must in (SETUP.split(" ")[-1], PAYER, PRICE):
        if must not in text:
            raise ValueError(f"pitch is missing {must!r}")


def main() -> None:
    pitch = build_pitch()
    check_pitch(pitch)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(pitch)
    os.chmod(path, 0o644)
    print(f"{len(pitch)} chars: {pitch}")


if __name__ == "__main__":
    main()
