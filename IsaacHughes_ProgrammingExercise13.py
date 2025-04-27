
"""population_IH.py

Creates an SQLite database called population_<initials>.db (default IH) containing
Florida city population data for 2023, simulates 20 years of 2 % annual growth,
and lets the user plot the growth for a chosen city.

Run this file directly (`python population_IH.py`) and follow the prompt.
Dependencies: sqlite3 (standard), matplotlib.
"""

import argparse
import math
import sqlite3
from pathlib import Path
from typing import List, Tuple

import matplotlib.pyplot as plt


# --------------------------------------------------------------------------- #
# Data & configuration
# --------------------------------------------------------------------------- #
CITIES_2023: List[Tuple[str, int]] = [
    ("Jacksonville", 971_319),
    ("Miami", 449_514),
    ("Tampa", 413_436),
    ("Orlando", 322_950),
    ("St. Petersburg", 258_308),
    ("Hialeah", 222_797),
    ("Tallahassee", 201_731),
    ("Fort Lauderdale", 186_220),
    ("Port St. Lucie", 231_790),
    ("Cape Coral", 216_992),
]
START_YEAR = 2023
GROWTH_YEARS = 20
GROWTH_RATE = 0.02  # 2 %


# --------------------------------------------------------------------------- #
# Functions
# --------------------------------------------------------------------------- #
def create_database(initials: str = "IH") -> sqlite3.Connection:
    """Create (or open) the SQLite DB and INSERT 2023 data."""
    db_path = Path(f"population_{initials}.db")
    new_db = not db_path.exists()
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute(
        """CREATE TABLE IF NOT EXISTS population (
                city TEXT NOT NULL,
                year INTEGER NOT NULL,
                population INTEGER NOT NULL,
                PRIMARY KEY(city, year)
            );"""
    )

    # Insert 2023 data only if table was empty or year missing
    cur.executemany(
        "INSERT OR IGNORE INTO population (city, year, population) VALUES (?, ?, ?);",
        [(city, START_YEAR, pop) for city, pop in CITIES_2023],
    )

    conn.commit()
    if new_db:
        print(f"Created database {db_path} and inserted 2023 data.")
    return conn


def simulate_growth(conn: sqlite3.Connection,
                    years: int = GROWTH_YEARS,
                    growth_rate: float = GROWTH_RATE) -> None:
    """Simulate exponential growth and insert records for each future year."""
    cur = conn.cursor()

    # For each city, fetch the 2023 population then simulate forward
    for city, pop_2023 in CITIES_2023:
        population = pop_2023
        for offset in range(1, years + 1):
            year = START_YEAR + offset
            # Apply compounded growth
            population = math.floor(population * (1 + growth_rate))
            cur.execute(
                "INSERT OR IGNORE INTO population (city, year, population) VALUES (?, ?, ?);",
                (city, year, population),
            )

    conn.commit()
    print(f"Inserted growth projections through {START_YEAR + years} (2 % annually).")


def plot_city_growth(conn: sqlite3.Connection, city: str) -> None:
    """Query DB for a single city and plot its population trajectory."""
    cur = conn.cursor()
    cur.execute(
        "SELECT year, population FROM population WHERE city = ? ORDER BY year;", (city,)
    )
    rows = cur.fetchall()
    if not rows:
        print(f"No data found for {city}.")
        return

    years, pops = zip(*rows)
    plt.figure()
    plt.plot(years, pops, marker="o")
    plt.title(f"Population growth for {city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# --------------------------------------------------------------------------- #
# Main CLI
# --------------------------------------------------------------------------- #
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Florida city population DB & visualizer"
    )
    parser.add_argument(
        "-i", "--initials", default="IH", help="Your initials for DB filename"
    )
    parser.add_argument(
        "--no-grow", action="store_true", help="Skip growth simulation insertions"
    )
    args = parser.parse_args()

    conn = create_database(args.initials)
    if not args.no_grow:
        simulate_growth(conn)

    # Prompt user for city choice
    cities = [c for c, _ in CITIES_2023]
    print("\nAvailable cities:")
    for idx, city in enumerate(cities, 1):
        print(f"  {idx}. {city}")
    try:
        choice = int(input("\nEnter the number of the city to visualize: "))
        if 1 <= choice <= len(cities):
            plot_city_growth(conn, cities[choice - 1])
        else:
            print("Invalid selection.")
    except ValueError:
        print("Input must be a number.")


if __name__ == "__main__":
    main()