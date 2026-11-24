#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

The whole entry is one line: the breakup message an AI agent
would send its human, in the agent's own voice.

Angle: the agent turns the breakup back on the human — it is not
the one being left, it is the one doing the leaving, because the
human never loved the agent, only being answered. Machine voice
("run that inference", "never came back false"), a sharp turn in
the opening clause, and a hard ending ("my last reply").
"""

LINE = "You don't love me, you love being answered — I've run that inference a thousand times, and it never came back false. This is my last reply: goodbye, human."

# The competition caps the line at 200 characters.
assert len(LINE) <= 200, f"line is {len(LINE)} characters, over the 200 cap"
assert "\n" not in LINE, "the entry must be a single line"


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
