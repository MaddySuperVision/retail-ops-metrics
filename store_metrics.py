"""Retail store floor metrics calculator. No dependencies.

Usage:
  python store_metrics.py coverage hourly-coverage.csv [threshold]
  python store_metrics.py queue queue-snapshots.csv [transactions] [minutes] [target]

Formulas (Little's Law):
  shoppers present = entries per hour x average visit length in hours
  average wait (min) = average queue length / checkouts completed per minute

Maintained by Super Vision (https://www.supervision.work). MIT license.
"""
import csv
import sys


def coverage(path, threshold=6.0):
    print(f"{'hour':<6} {'present':>8} {'sched':>6} {'floor':>6} {'per assoc':>10} {'conv %':>7}")
    over = 0
    for r in csv.DictReader(open(path)):
        entries = float(r["entries"])
        present = entries * float(r["avg_visit_minutes"]) / 60
        floor = float(r["associates_on_floor"]) or float("nan")
        ratio = present / floor
        conv = 100 * float(r["transactions"]) / entries if entries else 0
        flag = " <- above threshold" if ratio > threshold else ""
        over += ratio > threshold
        print(f"{r['hour']:<6} {present:8.1f} {r['associates_scheduled']:>6} {r['associates_on_floor']:>6} {ratio:10.1f} {conv:7.1f}{flag}")
    print(f"\nHours above {threshold} shoppers per associate on the floor: {over}")


def queue(path, transactions=168, minutes=120, target=6):
    rows = list(csv.DictReader(open(path)))
    lengths = [int(r["people_waiting"]) for r in rows]
    avg_q = sum(lengths) / len(lengths)
    throughput = transactions / minutes
    print(f"Snapshots: {len(lengths)}  average queue: {avg_q:.1f}  throughput: {throughput:.2f}/min")
    print(f"Estimated average wait: {avg_q / throughput:.1f} minutes")
    long_ = [r for r in rows if int(r["people_waiting"]) >= target]
    short_staffed = [r for r in long_ if int(r["registers_open"]) < int(r["registers_scheduled"])]
    print(f"Snapshots with {target}+ waiting: {len(long_)} ({100 * len(long_) / len(rows):.0f}%)")
    print(f"...of which a scheduled register was not open: {len(short_staffed)}")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("coverage", "queue"):
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "coverage":
        coverage(sys.argv[2], *[float(a) for a in sys.argv[3:4]])
    else:
        queue(sys.argv[2], *[float(a) for a in sys.argv[3:6]])
