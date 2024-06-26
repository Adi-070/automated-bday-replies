import pywhatkit as kit
import time

def send_thank_you_message(phone_number, message):
   
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min + 2

    if minutes >= 60:
        minutes -= 60
        hours += 1

    kit.sendwhatmsg(phone_number, message, hours, minutes)

def main():
   
    birthday_wishes = {
        "+91 9748303778": "Abhi",
        "+91 8910109657": "Abu"
    }

   
    for number, name in birthday_wishes.items():
        thank_you_message = f"Hi {name}, thank you so much for the birthday wishes!"
        send_thank_you_message(number, thank_you_message)
        print(f"Scheduled message for {name} ({number})")

if __name__ == "__main__":
    main()
