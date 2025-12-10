#!/usr/bin/env python3
"""
Demo Teleprompter - Walk through Claude.ai demos step by step.

Reduces cognitive load by showing one step at a time and copying to clipboard.

Usage:
    python scripts/demo_teleprompter.py                    # Scenario 1 (default)
    python scripts/demo_teleprompter.py --scenario 1       # Explicit scenario
    python scripts/demo_teleprompter.py --list             # List available scenarios
"""

import argparse
import sys

try:
    import pyperclip
    HAS_CLIPBOARD = True
except ImportError:
    HAS_CLIPBOARD = False
    print("Note: pyperclip not installed. Clipboard copy disabled.")
    print("Install with: pip install pyperclip\n")


# ============================================================================
# Scenario Data
# ============================================================================

SCENARIO_1_STEPS = [
    {
        "phase": "Setup Context",
        "action": "SAY TO AUDIENCE",
        "content": """Rob is a 39-year-old accountant who just started a couch-to-5K program.
He got winded playing tag with his kids and decided to make a change.
Today is his first day using Claude as his coach.""",
        "talk": "Set the scene - relatable starting point",
        "expect": None,
    },
    {
        "phase": "Morning Update",
        "action": "PASTE TO CLAUDE",
        "content": """Just finished my first run. "Run" is generous - it was more like shuffling with occasional walking.

The couch-to-5K app said: Walk 2 min / Run 1 min x 8 reps. I made it through all 8 reps but barely.

After just the first 1-minute run interval I was already breathing hard. By the third interval I wasn't sure I'd make it. My calves are on fire. My shins hurt. Even my lungs feel weird.

Total time: about 24 minutes (including warmup walk)
Distance: maybe 1.5 miles? The app doesn't track distance, just time.
How I feel: 3/10. Everything hurts.""",
        "talk": "Raw, honest first-day experience",
        "expect": "Claude encourages, maybe asks follow-up questions",
    },
    {
        "phase": "Midday Reflection",
        "action": "PASTE TO CLAUDE",
        "content": """Sitting at my desk thinking about this morning. I'm 39 years old and I couldn't run for ONE MINUTE without gasping.

The realization that got me here: Playing tag with my kids (6 and 8) last weekend, I was winded after 10 minutes. They wanted to keep going. I needed to sit down.

When did I get this out of shape? I used to play pickup basketball in my 20s. Now I'm the dad who can't keep up with elementary schoolers.

I want to be able to play with my kids without needing to rest. That's the goal. The 5K is just the milestone.""",
        "talk": "The WHY - kids motivation, not the 5K itself",
        "expect": "Claude connects to deeper motivation",
    },
    {
        "phase": "Evening Update",
        "action": "PASTE TO CLAUDE",
        "content": """Wife asked how my first run went. I told her it was rough.

She said: "That's normal. Just try it for two weeks before you decide anything."

She's right. I signed up for 8 weeks. It's been one day. One terrible day, but one day.

Tomorrow is a rest day (the program is Mon/Wed/Fri). I'm already dreading Wednesday.

Sleep plan: Try to get 7+ hours. Apparently recovery matters for this running thing.

Did I mention my calves still hurt? Because they do.""",
        "talk": "Support system (wife), realistic mindset",
        "expect": "Claude acknowledges the journey, maybe sleep/recovery",
    },
    {
        "phase": "Trigger Summary",
        "action": "TYPE IN CLAUDE",
        "content": "daily summary",
        "talk": "Now we capture the day with the skill",
        "expect": "Skill triggers, asks which date",
    },
    {
        "phase": "Confirm Date",
        "action": "TYPE IN CLAUDE",
        "content": "today",
        "talk": "Skill verifies date to avoid mistakes",
        "expect": "Asks to confirm the specific date",
    },
    {
        "phase": "Confirm Date (2)",
        "action": "TYPE IN CLAUDE",
        "content": "yes",
        "talk": None,
        "expect": "Asks for context tag",
    },
    {
        "phase": "Context Tag",
        "action": "TYPE IN CLAUDE",
        "content": "W1-D1",
        "talk": "Week 1, Day 1 - helps track progress over time",
        "expect": "Generates structured summary with TL;DR, Key Numbers, etc.",
    },
    {
        "phase": "Wrap Up",
        "action": "SAY TO AUDIENCE",
        "content": """That's Rob's first day captured!

Key points:
• No prior documents needed - system works from day 1
• Natural conversation → structured data
• Base skill does the heavy lifting (no customization needed)
• This summary becomes context for tomorrow's morning routine""",
        "talk": "Emphasize low barrier to entry",
        "expect": None,
    },
]

SCENARIOS = {
    1: {
        "name": "Getting Started",
        "description": "Rob's first day - conversation snippets → daily summary",
        "steps": SCENARIO_1_STEPS,
    },
    # TODO: Add scenarios 2, 3, 4
}


# ============================================================================
# Display Functions
# ============================================================================

def clear_screen():
    """Clear terminal screen."""
    print("\033[2J\033[H", end="")


def display_step(scenario_num: int, scenario_name: str, step_num: int, total_steps: int, step: dict):
    """Display a single step in teleprompter format."""
    clear_screen()

    # Header
    print("═" * 60)
    print(f"  SCENARIO {scenario_num}: {scenario_name}")
    print(f"  Step {step_num}/{total_steps} • {step['phase']}")
    print("═" * 60)
    print()

    # Action type
    action = step["action"]
    if action == "PASTE TO CLAUDE":
        print(f"  📋 {action}:")
    elif action == "TYPE IN CLAUDE":
        print(f"  ⌨️  {action}:")
    else:
        print(f"  🎤 {action}:")

    print("  ┌" + "─" * 56 + "┐")

    # Content (with wrapping)
    content_lines = step["content"].strip().split("\n")
    for line in content_lines:
        # Wrap long lines
        while len(line) > 54:
            print(f"  │ {line[:54]} │")
            line = line[54:]
        print(f"  │ {line:<54} │")

    print("  └" + "─" * 56 + "┘")
    print()

    # Talking point
    if step.get("talk"):
        print(f"  💬 TALK: {step['talk']}")
        print()

    # Expected response
    if step.get("expect"):
        print(f"  ⏭️  EXPECT: {step['expect']}")
        print()

    # Footer
    print("─" * 60)
    if step["action"] in ["PASTE TO CLAUDE", "TYPE IN CLAUDE"]:
        if HAS_CLIPBOARD:
            print("  [Enter] Copy & Next    [b] Back    [q] Quit")
        else:
            print("  [Enter] Next    [b] Back    [q] Quit")
    else:
        print("  [Enter] Next    [b] Back    [q] Quit")
    print("─" * 60)


def copy_to_clipboard(text: str) -> bool:
    """Copy text to clipboard if available."""
    if HAS_CLIPBOARD:
        try:
            pyperclip.copy(text)
            return True
        except Exception:
            return False
    return False


# ============================================================================
# Main Loop
# ============================================================================

def run_teleprompter(scenario_num: int):
    """Run the teleprompter for a scenario."""
    if scenario_num not in SCENARIOS:
        print(f"Scenario {scenario_num} not found.")
        print("Available scenarios:")
        for num, data in SCENARIOS.items():
            print(f"  {num}: {data['name']} - {data['description']}")
        return

    scenario = SCENARIOS[scenario_num]
    steps = scenario["steps"]
    current_step = 0

    while True:
        step = steps[current_step]
        display_step(
            scenario_num=scenario_num,
            scenario_name=scenario["name"],
            step_num=current_step + 1,
            total_steps=len(steps),
            step=step,
        )

        try:
            key = input("\n  > ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\n\nDemo ended.")
            break

        if key == "q":
            print("\nDemo ended.")
            break
        elif key == "b":
            if current_step > 0:
                current_step -= 1
        else:  # Enter or any other key advances
            # Copy to clipboard if it's a paste/type action
            if step["action"] in ["PASTE TO CLAUDE", "TYPE IN CLAUDE"]:
                if copy_to_clipboard(step["content"]):
                    print("  ✓ Copied to clipboard!")

            # Advance
            current_step += 1
            if current_step >= len(steps):
                clear_screen()
                print("\n  🎉 Demo complete!\n")
                break


def list_scenarios():
    """List available scenarios."""
    print("\nAvailable Scenarios:")
    print("─" * 40)
    for num, data in SCENARIOS.items():
        print(f"  {num}: {data['name']}")
        print(f"     {data['description']}")
        print(f"     Steps: {len(data['steps'])}")
        print()


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Demo Teleprompter - Walk through Claude.ai demos step by step"
    )
    parser.add_argument(
        "--scenario", "-s",
        type=int,
        default=1,
        help="Scenario number to run (default: 1)"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List available scenarios"
    )

    args = parser.parse_args()

    if args.list:
        list_scenarios()
        return

    run_teleprompter(args.scenario)


if __name__ == "__main__":
    main()
