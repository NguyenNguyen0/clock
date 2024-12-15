import tkinter as tk
import math
import time


def calculate_end_points(start_x, start_y, length, radius):
    angle = math.radians(-radius + 90) # -radius + 90 is fix the tkinter canvas coordinate system
    x = start_x + length * math.cos(angle)
    y = start_y - length * math.sin(angle)
    return (x, y)


def update_hand(canvas, hand, center, length, radius):
    end_x, end_y = calculate_end_points(center["x"], center["y"], length, radius)
    canvas.coords(hand, center["x"], center["y"], end_x, end_y)


def update_clock(canvas, center, second_hand, minute_hand, hour_hand):
    current_time = time.localtime()
    second = current_time.tm_sec
    minute = current_time.tm_min
    hour = current_time.tm_hour % 12

    print(f"{hour}:{minute}:{second} \r", end="")

    second_radius = second * 6
    minute_radius = minute * 6 + second * 0.1
    hour_radius = hour * 30 + minute * 0.5

    update_hand(canvas, second_hand, center, 180, second_radius)
    update_hand(canvas, minute_hand, center, 120, minute_radius)
    update_hand(canvas, hour_hand, center, 80, hour_radius)

    canvas.after(
        200, update_clock, canvas, center, second_hand, minute_hand, hour_hand
    )


def main() -> None:
    root = tk.Tk()

    root.title("Normal Clock")
    root.geometry("600x600")
    root.resizable(False, False)
    root.iconbitmap(r"clock-icon.ico")

    canvas = tk.Canvas(root, width=600, height=600, bg="gray")
    canvas.pack()

    CLOCK_CENTER = {"x": 300, "y": 300}

    canvas.create_oval(100, 100, 500, 500, fill="white")

    second_clock_hand = canvas.create_line(
        CLOCK_CENTER["x"],
        CLOCK_CENTER["y"],
        CLOCK_CENTER["x"],
        CLOCK_CENTER["y"],
        width=1,
        fill="red",
    )

    minute_clock_hand = canvas.create_line(
        CLOCK_CENTER["x"],
        CLOCK_CENTER["y"],
        CLOCK_CENTER["x"],
        CLOCK_CENTER["y"],
        width=2,
        fill="black",
    )

    hour_clock_hand = canvas.create_line(
        CLOCK_CENTER["x"],
        CLOCK_CENTER["y"],
        CLOCK_CENTER["x"],
        CLOCK_CENTER["y"],
        width=4,
        fill="black",
    )

    update_clock(canvas, CLOCK_CENTER, second_clock_hand, minute_clock_hand, hour_clock_hand)

    root.mainloop()


if __name__ == "__main__":
    main()
