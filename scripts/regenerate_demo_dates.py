#!/usr/bin/env python3
"""
Regenerate demo documents with correct dates based on demo day.

Usage:
    python scripts/regenerate_demo_dates.py --scenario 2 --demo-day 2025-12-12
    python scripts/regenerate_demo_dates.py --scenario all --demo-day 2025-12-12
    python scripts/regenerate_demo_dates.py --scenario 4 --dry-run
"""

import argparse
from datetime import datetime, timedelta
from pathlib import Path


def get_week_start(date: datetime) -> datetime:
    """Get Monday of the week containing the given date."""
    days_since_monday = date.weekday()  # Monday=0, Sunday=6
    return date - timedelta(days=days_since_monday)


def calculate_dates(demo_day: datetime, scenario: int) -> dict:
    """
    Calculate all date placeholders based on demo day and scenario.

    Scenario 1-3: W1 = current week (demo day week)
    Scenario 4:   W9 = current week (demo day week)
    """
    placeholders = {}

    # Base week (week containing demo day)
    base_week_start = get_week_start(demo_day)

    # Year placeholder
    placeholders['YEAR'] = demo_day.strftime('%Y')

    if scenario in [1, 2]:
        # Scenarios 1-2: W1 = current week (just starting)
        w1_start = base_week_start
        w1_end = w1_start + timedelta(days=6)

        # W1 placeholders
        placeholders['W1_START'] = w1_start.strftime('%Y-%m-%d')
        placeholders['W1_START_DAY'] = w1_start.strftime('%A')
        placeholders['W1_START_FULL'] = w1_start.strftime('%A, %B %-d, %Y')
        placeholders['W1_START_DD'] = w1_start.strftime('%-d')
        placeholders['W1_END'] = w1_end.strftime('%Y-%m-%d')
        placeholders['W1_END_DD'] = w1_end.strftime('%-d')
        placeholders['W1_MONTH'] = w1_start.strftime('%B')
        placeholders['W1_YEAR'] = w1_start.strftime('%Y')

        # W1 specific days (D1=Mon, D3=Wed, D5=Fri)
        w1_d1 = w1_start  # Monday
        w1_d3 = w1_start + timedelta(days=2)  # Wednesday
        w1_d5 = w1_start + timedelta(days=4)  # Friday

        for label, date in [('W1_D1', w1_d1), ('W1_D3', w1_d3), ('W1_D5', w1_d5)]:
            placeholders[f'{label}_DATE'] = date.strftime('%Y-%m-%d')
            placeholders[f'{label}_DAY'] = date.strftime('%A')
            placeholders[f'{label}_FULL'] = date.strftime('%A, %B %-d, %Y')
            placeholders[f'{label}_DD'] = date.strftime('%-d')

        # W2 placeholders (for scenario 2 planning)
        w2_start = w1_start + timedelta(weeks=1)
        w2_end = w2_start + timedelta(days=6)
        placeholders['W2_START'] = w2_start.strftime('%Y-%m-%d')
        placeholders['W2_END'] = w2_end.strftime('%Y-%m-%d')
        placeholders['W2_END_DD'] = w2_end.strftime('%-d')
        placeholders['W2_YEAR'] = w2_start.strftime('%Y')

    elif scenario == 3:
        # Scenario 3: Monthly review - W1-W4 are the 4 weeks BEFORE demo day
        # Rob has COMPLETED 4 weeks and is looking back
        w4_start = base_week_start - timedelta(weeks=1)  # Last week
        w3_start = base_week_start - timedelta(weeks=2)
        w2_start = base_week_start - timedelta(weeks=3)
        w1_start = base_week_start - timedelta(weeks=4)

        # Generate W1-W4 placeholders
        for week_num, w_start in [(1, w1_start), (2, w2_start), (3, w3_start), (4, w4_start)]:
            w_end = w_start + timedelta(days=6)
            prefix = f'W{week_num}'

            placeholders[f'{prefix}_START'] = w_start.strftime('%Y-%m-%d')
            placeholders[f'{prefix}_START_DAY'] = w_start.strftime('%A')
            placeholders[f'{prefix}_START_FULL'] = w_start.strftime('%A, %B %-d, %Y')
            placeholders[f'{prefix}_START_DD'] = w_start.strftime('%-d')
            placeholders[f'{prefix}_END'] = w_end.strftime('%Y-%m-%d')
            placeholders[f'{prefix}_END_DD'] = w_end.strftime('%-d')
            placeholders[f'{prefix}_MONTH'] = w_start.strftime('%B')
            placeholders[f'{prefix}_YEAR'] = w_start.strftime('%Y')

        # W1 specific days (D1=Mon, D3=Wed, D5=Fri)
        for label, date in [('W1_D1', w1_start), ('W1_D3', w1_start + timedelta(days=2)), ('W1_D5', w1_start + timedelta(days=4))]:
            placeholders[f'{label}_DATE'] = date.strftime('%Y-%m-%d')
            placeholders[f'{label}_DAY'] = date.strftime('%A')
            placeholders[f'{label}_FULL'] = date.strftime('%A, %B %-d, %Y')
            placeholders[f'{label}_DD'] = date.strftime('%-d')

        # W4 D5 (Friday of Week 4 - most recent daily summary)
        w4_d5 = w4_start + timedelta(days=4)
        placeholders['W4_D5_DATE'] = w4_d5.strftime('%Y-%m-%d')
        placeholders['W4_D5_DAY'] = w4_d5.strftime('%A')
        placeholders['W4_D5_FULL'] = w4_d5.strftime('%A, %B %-d, %Y')

        # M1 = month containing W1-W4 (use W1's month for naming)
        m1_start = w1_start
        next_month = m1_start.replace(day=28) + timedelta(days=4)
        m1_end = next_month.replace(day=1) - timedelta(days=1)

        placeholders['M1_NAME'] = m1_start.strftime('%B')
        placeholders['M1_YEAR'] = m1_start.strftime('%Y')
        placeholders['M1_START_DD'] = m1_start.strftime('%-d')
        placeholders['M1_END_DD'] = m1_end.strftime('%-d')

    else:  # scenario == 4
        # Scenario 4: W9 = current week (original behavior)
        w9_start = base_week_start
        w9_end = w9_start + timedelta(days=6)

        # Calculate week starts for W8, W7, W6, W5
        w8_start = w9_start - timedelta(weeks=1)
        w7_start = w9_start - timedelta(weeks=2)
        w6_start = w9_start - timedelta(weeks=3)
        w5_start = w9_start - timedelta(weeks=4)

        # W9 placeholders (current week)
        placeholders['W9_START'] = w9_start.strftime('%Y-%m-%d')
        placeholders['W9_START_DAY'] = w9_start.strftime('%A')
        placeholders['W9_START_FULL'] = w9_start.strftime('%A, %B %-d, %Y')
        placeholders['W9_START_DD'] = w9_start.strftime('%-d')
        placeholders['W9_END'] = w9_end.strftime('%Y-%m-%d')
        placeholders['W9_END_DD'] = w9_end.strftime('%-d')
        placeholders['W9_MONTH'] = w9_start.strftime('%B')

        # W9 specific days
        w9_d1 = w9_start  # Monday
        w9_d2 = w9_start + timedelta(days=2)  # Wednesday
        w9_d5 = w9_start + timedelta(days=4)  # Friday

        for label, date in [('W9_D1', w9_d1), ('W9_D2', w9_d2), ('W9_D5', w9_d5)]:
            placeholders[f'{label}_DATE'] = date.strftime('%Y-%m-%d')
            placeholders[f'{label}_DAY'] = date.strftime('%A')
            placeholders[f'{label}_FULL'] = date.strftime('%A, %B %-d, %Y')
            placeholders[f'{label}_DD'] = date.strftime('%-d')

        # W8 placeholders
        w8_end = w8_start + timedelta(days=6)
        placeholders['W8_START'] = w8_start.strftime('%Y-%m-%d')
        placeholders['W8_END'] = w8_end.strftime('%Y-%m-%d')
        placeholders['W8_END_DD'] = w8_end.strftime('%-d')
        placeholders['W8_START_DD'] = w8_start.strftime('%-d')

        # W8 specific days
        w8_d1 = w8_start
        w8_d2 = w8_start + timedelta(days=2)
        w8_d3 = w8_start + timedelta(days=4)

        for label, date in [('W8_D1', w8_d1), ('W8_D2', w8_d2), ('W8_D3', w8_d3)]:
            placeholders[f'{label}_DATE'] = date.strftime('%Y-%m-%d')
            placeholders[f'{label}_DAY'] = date.strftime('%A')
            placeholders[f'{label}_FULL'] = date.strftime('%A, %B %-d, %Y')
            placeholders[f'{label}_DD'] = date.strftime('%-d')

        # W7, W6, W5 placeholders
        for week_num, w_start in [(7, w7_start), (6, w6_start), (5, w5_start)]:
            w_end = w_start + timedelta(days=6)
            prefix = f'W{week_num}'
            placeholders[f'{prefix}_START'] = w_start.strftime('%Y-%m-%d')
            placeholders[f'{prefix}_START_DD'] = w_start.strftime('%-d')
            placeholders[f'{prefix}_END'] = w_end.strftime('%Y-%m-%d')
            placeholders[f'{prefix}_END_DD'] = w_end.strftime('%-d')
            placeholders[f'{prefix}_MONTH'] = w_start.strftime('%B')

        # W4-W1 for monthly rollup
        w4_start = w9_start - timedelta(weeks=5)
        w1_start = w9_start - timedelta(weeks=8)
        w1_end = w1_start + timedelta(days=6)

        placeholders['W4_START'] = w4_start.strftime('%Y-%m-%d')
        placeholders['W4_END_DD'] = (w4_start + timedelta(days=6)).strftime('%-d')
        placeholders['W1_START'] = w1_start.strftime('%Y-%m-%d')
        placeholders['W1_END'] = w1_end.strftime('%Y-%m-%d')

        # M1 = month containing W1-W4 (the first month of the program)
        m1_start = w1_start
        next_month = m1_start.replace(day=28) + timedelta(days=4)
        m1_end = next_month.replace(day=1) - timedelta(days=1)

        placeholders['M1_NAME'] = m1_start.strftime('%B')
        placeholders['M1_YEAR'] = m1_start.strftime('%Y')
        placeholders['M1_START_DD'] = m1_start.strftime('%-d')
        placeholders['M1_END_DD'] = m1_end.strftime('%-d')

    return placeholders


def process_template(template_content: str, placeholders: dict) -> str:
    """Replace all {{PLACEHOLDER}} markers with actual values."""
    result = template_content
    for key, value in placeholders.items():
        result = result.replace(f'{{{{{key}}}}}', value)
    return result


def get_output_filename(template_name: str, placeholders: dict) -> str:
    """Convert template filename to output filename."""
    base_name = template_name.replace('.tmpl', '')
    result = process_template(base_name, placeholders)
    return result


def regenerate_scenario(
    scenario: int,
    demo_day: datetime,
    repo_root: Path,
    dry_run: bool = False
) -> list:
    """Regenerate documents for a specific scenario."""
    scenario_dirs = {
        1: 'scenario-1-startup',
        2: 'scenario-2-weekly',
        3: 'scenario-3-monthly',
        4: 'scenario-4-established'
    }

    scenario_dir = scenario_dirs.get(scenario)
    if not scenario_dir:
        print(f"Unknown scenario: {scenario}")
        return []

    templates_dir = repo_root / 'examples' / 'rob-the-runner' / scenario_dir / 'templates'
    output_dir = repo_root / 'examples' / 'rob-the-runner' / scenario_dir / 'documents-generated'

    # Scenario 1 has no templates (generates from scratch during demo)
    if scenario == 1:
        print(f"Scenario 1: No templates to generate (starts empty)")
        output_dir.mkdir(parents=True, exist_ok=True)
        return []

    placeholders = calculate_dates(demo_day, scenario)
    generated = []

    if not templates_dir.exists():
        print(f"Templates directory not found: {templates_dir}")
        return generated

    print(f"Scenario {scenario}: {scenario_dir}")
    print(f"  Templates: {templates_dir}")
    print(f"  Output:    {output_dir}")

    for template_path in sorted(templates_dir.glob('*.tmpl')):
        template_content = template_path.read_text()
        output_content = process_template(template_content, placeholders)
        output_filename = get_output_filename(template_path.name, placeholders)
        output_path = output_dir / output_filename

        if dry_run:
            print(f"  Would generate: {output_filename}")
        else:
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path.write_text(output_content)
            print(f"  Generated: {output_filename}")

        generated.append((template_path, output_path))

    return generated


def main():
    parser = argparse.ArgumentParser(
        description='Regenerate demo documents with correct dates'
    )
    parser.add_argument(
        '--scenario',
        type=str,
        default='all',
        help='Scenario to generate: 1, 2, 3, 4, or all (default: all)'
    )
    parser.add_argument(
        '--demo-day',
        type=str,
        help='Demo day in YYYY-MM-DD format (default: today)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be generated without writing files'
    )
    parser.add_argument(
        '--show-placeholders',
        action='store_true',
        help='Show all calculated placeholder values'
    )

    args = parser.parse_args()

    # Parse demo day
    if args.demo_day:
        demo_day = datetime.strptime(args.demo_day, '%Y-%m-%d')
    else:
        demo_day = datetime.now()

    print(f"Demo day: {demo_day.strftime('%A, %B %-d, %Y')}")
    print()

    # Determine which scenarios to run
    if args.scenario == 'all':
        scenarios = [1, 2, 3, 4]
    else:
        try:
            scenarios = [int(args.scenario)]
        except ValueError:
            print(f"Invalid scenario: {args.scenario}")
            print("Use 1, 2, 3, 4, or 'all'")
            return

    # Show placeholders if requested
    if args.show_placeholders:
        for scenario in scenarios:
            placeholders = calculate_dates(demo_day, scenario)
            print(f"Placeholders for scenario {scenario}:")
            print("-" * 40)
            for key in sorted(placeholders.keys()):
                print(f"  {{{{{key}}}}} = {placeholders[key]}")
            print()

    # Find repo root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    # Regenerate documents
    total_generated = 0
    for scenario in scenarios:
        generated = regenerate_scenario(
            scenario=scenario,
            demo_day=demo_day,
            repo_root=repo_root,
            dry_run=args.dry_run
        )
        total_generated += len(generated)
        print()

    print(f"{'Would generate' if args.dry_run else 'Generated'} {total_generated} total documents")


if __name__ == '__main__':
    main()
