from datetime import datetime
import tkinter as tk
import math


def calculate_end_points(start_x, start_y, length, radius):
    angle = math.radians(-radius + 90)  # -radius + 90 is fix the tkinter canvas coordinate system
    x = start_x + length * math.cos(angle)
    y = start_y - length * math.sin(angle)
    return (x, y)


def update_hand(canvas, hand, center, angle, time):
    TEXT_WITH = 24
    for index, text in enumerate(hand):
        end_x, end_y = calculate_end_points(
            center["x"], center["y"], (index + 1) * TEXT_WITH, angle
        )
        canvas.itemconfig(text, text=time)
        canvas.coords(text, end_x, end_y)


def update_clock(canvas, center, second_hand, minute_hand, hour_hand):
    second = datetime.now().second
    minute = datetime.now().minute
    hour = datetime.now().hour % 12

    second_radius = second * 6
    minute_radius = minute * 6 + second * 0.1
    hour_radius = hour * 30 + minute * 0.5

    update_hand(canvas, second_hand, center, second_radius, second)
    update_hand(canvas, minute_hand, center, minute_radius, minute)
    update_hand(canvas, hour_hand, center, hour_radius, hour)

    canvas.after(
        1000, update_clock, canvas, center, second_hand, minute_hand, hour_hand
    )


def create_clock_hand(canvas, center, length, color):
    clock_hand = []
    TEXT_WITH = 24
    for i in range(1, length + 1):
        text = canvas.create_text(
            center["x"],
            center["y"] + i * TEXT_WITH,
            text="0",
            fill=color,
            font=("Arial", 12),
        )
        clock_hand.append(text)
    return clock_hand


def main() -> None:
    root = tk.Tk()

    root.title("ULTIMATE Clock")
    root.geometry("600x600")
    root.resizable(False, False)
    root.iconbitmap(r"clock-icon.ico")

    canvas = tk.Canvas(root, width=600, height=600, bg="gray")
    canvas.pack()

    canvas.create_oval(100, 100, 500, 500, fill="white")
    canvas.create_oval(295, 295, 305, 305, fill="black")

    CLOCK_CENTER = {"x": 300, "y": 300}
    SECOND_CLOCK_HAND_LENGTH = 6
    MINUTE_CLOCK_HAND_LENGTH = 5
    HOUR_CLOCK_HAND_LENGTH = 4

    second_clock_hand = create_clock_hand(
        canvas=canvas,
        center=CLOCK_CENTER,
        length=SECOND_CLOCK_HAND_LENGTH,
        color="black",
    )
    minute_clock_hand = create_clock_hand(
        canvas=canvas,
        center=CLOCK_CENTER,
        length=MINUTE_CLOCK_HAND_LENGTH,
        color="black",
    )
    hour_clock_hand = create_clock_hand(
        canvas=canvas, center=CLOCK_CENTER, length=HOUR_CLOCK_HAND_LENGTH, color="black"
    )
    update_clock(
        canvas, CLOCK_CENTER, second_clock_hand, minute_clock_hand, hour_clock_hand
    )

    root.mainloop()


if __name__ == "__main__":
    main()
