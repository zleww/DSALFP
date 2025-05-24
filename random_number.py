import random # generates random numbers

def over_under_simple():
    history = []  # is an empty list to store the history of outputs
    stack = set() # empty set to store unique numbers

    def extract_numbers_from_history():
        nums = []
        for entry in history:
            parts = entry.split()
            try:
                num = float(parts[-1])
                nums.append(num)
            except ValueError:
                pass
        return nums

    def print_status():
        print("\nHistory so far (newest first):")
        if history:
            for line in reversed(history):
                print(line)
        else:
            print("[Empty]")

        print("\nSorted unique numbers so far (lowest to highest):")
        if stack:
            formatted_numbers = [int(n) if n.is_integer() else n for n in stack]
            for num in sorted(formatted_numbers):
                print(num)
        else:
            print("[Empty]")
        print("-" * 30)

    while True:
        try:
            start = float(input("Enter the first number: "))
            end = float(input("Enter the second number: "))

            if start > end:
                start, end = end, start

            choice = input("Do you want an over or under? (yes or no): ").strip().lower()

            use_decimal = (start % 1 == end % 1)
            step = 1.0 if use_decimal else 1
            values = []
            current = start
            while current <= end:
                values.append(round(current, 1 if use_decimal else 0))
                current += step

            number = random.choice(values)

            if choice == "yes":
                result_type = random.choice(["over", "under"])
                output = f"The number is {result_type} {number}"
            elif choice == "no":
                output = f"The number is {number}"
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
                continue

            print(output)
            history.append(output)
            stack.add(number)

            # Show current history and sorted numbers
            print_status()

            # Option to delete a number
            delete_input = input("Delete a number from history? (Enter number or 'no'): ").strip().lower()
            if delete_input != "no":
                try:
                    delete_number = float(delete_input)
                    # Remove all history entries that match this number
                    history = [h for h in history if not h.endswith(f"{delete_number}")]
                    # Recalculate stack
                    remaining_numbers = extract_numbers_from_history()
                    stack = set(remaining_numbers)
                    print(f"Deleted {delete_number} from history and stack (if no longer used).")
                    print_status()
                except ValueError:
                    print("Invalid number input for delete.")

            # Option to clear all
            clear_all = input("Clear all history and stack? (yes or no): ").strip().lower()
            if clear_all == "yes":
                history.clear()
                stack.clear()
                print("History and stack cleared.")
                print_status()

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

        next_step = input("Try again? (Yes to continue / No to exit): ").strip().lower()
        if next_step in ["no", "n", "NO", "N", "No"]:
            print("\nGoodbye!\n")
            break
        elif next_step in ["yes", "y", "YES", "Y", "Yes"]:
            continue
        else:
            print("Invalid choice. Exiting.\n")
            break

over_under_simple()
