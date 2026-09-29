def print_report(summary, total_files):
    print("\n=== Organization Report ===")
    print(f"Total files moved: {total_files}")

    for category, count in summary.items():
        if count > 0:
            print(f"{category.title()}: {count}")

    print("===========================")