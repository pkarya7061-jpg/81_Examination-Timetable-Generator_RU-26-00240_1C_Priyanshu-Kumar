
from datetime import datetime, timedelta

# Take subjects from the user
subjects_input = input("Enter subjects separated by commas: ")
subjects = [s.strip() for s in subjects_input.split(",") if s.strip()]

# Check that at least one subject is entered
if not subjects:
    print("At least one subject is required.")

# Check for duplicate subjects
elif len(set(s.lower() for s in subjects)) != len(subjects):
    print("Duplicate subjects are not allowed.")

else:
    try:
        # Take and validate the starting date
        date_input = input("Enter start date (DD-MM-YYYY): ").strip()
        start_date = datetime.strptime(date_input, "%d-%m-%Y")

        if start_date.strftime("%d-%m-%Y") != date_input:
            print("Invalid date format. Please use DD-MM-YYYY.")

        else:
            # Take optional holidays
            holiday_input = input(
                "Enter holidays separated by commas (or press Enter): "
            )

            holidays = set()
            valid_holidays = True

            if holiday_input.strip():
                for h in holiday_input.split(","):
                    h = h.strip()

                    try:
                        holiday = datetime.strptime(h, "%d-%m-%Y")

                        if holiday.strftime("%d-%m-%Y") != h:
                            print("Invalid holiday format. Use DD-MM-YYYY.")
                            valid_holidays = False
                            break

                        holidays.add(holiday.date())

                    except ValueError:
                        print("Invalid holiday date. Use DD-MM-YYYY.")
                        valid_holidays = False
                        break

            if valid_holidays:
                # Generate the timetable
                current_date = start_date
                timetable = []

                for subject in subjects:

                    # Skip Sundays and holidays
                    while (
                        current_date.weekday() == 6
                        or current_date.date() in holidays
                    ):
                        current_date += timedelta(days=1)

                    timetable.append(
                        (
                            subject,
                            current_date.strftime("%d-%m-%Y"),
                            current_date.strftime("%A")
                        )
                    )

                    # Move to the next day
                    current_date += timedelta(days=1)

                # Display the timetable
                print("\n===== EXAMINATION TIMETABLE =====")
                print("---------------------------------")

                for subject, date, day in timetable:
                    print(f"{subject}: {date} ({day})")

    except ValueError:
        print("Invalid start date. Please use DD-MM-YYYY.")


        
