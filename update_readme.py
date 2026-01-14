#!/usr/bin/env python3
"""
Update README.md with dynamic values calculated from start dates
"""

from datetime import datetime
from pathlib import Path


BIRTH_DATE = datetime(1993, 3, 22)
EXPERIENCE_START = datetime(2017, 12, 1)


def _calculate_years_from(start_date: datetime) -> int:
    today = datetime.now()
    years = today.year - start_date.year

    if (today.month, today.day) < (start_date.month, start_date.day):
        years -= 1

    return years


def main() -> int:
    template_file = Path("README.template.md")
    output_file = Path("README.md")

    if not template_file.exists():
        print(f"Error: {template_file} not found!")
        return 1

    today = datetime.now()
    age = _calculate_years_from(BIRTH_DATE)
    experience = _calculate_years_from(EXPERIENCE_START)
    current_date = today.strftime("%Y-%m-%d")

    template_content = template_file.read_text()

    output_content = template_content.format(
        EXPERIENCE_YEARS=experience,
        LEVEL=age,
        CURRENT_DATE=current_date,
    )

    output_file.write_text(output_content)

    print(f"✓ README.md updated successfully!")
    print(f"  - Age (Level): {age}")
    print(f"  - Experience years: {experience}")
    print(f"  - Date: {current_date}")

    return 0


if __name__ == "__main__":
    exit(main())
