from datetime import datetime, timedelta

def calculate_wakeup_time(sleep_time):
    # Convert sleep time to datetime object
    sleep_time = datetime.strptime(sleep_time, '%H:%M')

    # Calculate wakeup time
    wakeup_time = sleep_time + timedelta(hours=8)
    
    return wakeup_time.strftime('%H:%M')

def calculate_bedtime(wakeup_time):
    # Convert wakeup time to datetime object
    wakeup_time = datetime.strptime(wakeup_time, '%H:%M')

    # Calculate bedtime
    bedtime = wakeup_time - timedelta(hours=8)
    
    return bedtime.strftime('%H:%M')

def calculate_medication_timing(sleep_time):
    # Convert sleep time to datetime object
    sleep_time = datetime.strptime(sleep_time, '%H:%M')

    # Calculate medication timing
    medication_timing = sleep_time - timedelta(minutes=15)
    
    return medication_timing.strftime('%H:%M')

def main():
    print("Welcome!")
    print("Please follow the steps below and select the calculation you want to perform.")
    print("1. Calculate bedtime from wakeup time")
    print("2. Calculate wakeup time from bedtime")

    choice = input("Please enter the number of your choice (1 or 2): ")

    if choice == "1":
        # Calculate bedtime from wakeup time
        wakeup_time = input("Enter the wakeup time (in HH:MM format): ")
        recommended_bedtime = calculate_bedtime(wakeup_time)
        print("The best time to sleep for 8 hours is at", recommended_bedtime)
        # Calculate medication timing
        medication_timing = calculate_medication_timing(recommended_bedtime)
        print("Take medication at", medication_timing)

    elif choice == "2":
        # Calculate wakeup time from bedtime
        sleep_time = input("Enter the bedtime (in HH:MM format): ")
        wakeup_time = calculate_wakeup_time(sleep_time)
        print("The wakeup time is", wakeup_time)
        # Calculate medication timing
        medication_timing = calculate_medication_timing(sleep_time)
        print("Take medication at", medication_timing)

    else:
        print("Please enter a valid choice.")

if __name__ == "__main__":
    main()
