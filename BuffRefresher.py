import pyautogui
import time
import winsound

def auto_clicker_scroll(clicks, scroll_amount, delay):
    initial_position = pyautogui.position()
    x_offset = 200  # Adjust this value to move the cursor more to the right

    for _ in range(clicks):
        pyautogui.move(x_offset, 0)  # Move the mouse to the right by the specified offset
        pyautogui.scroll(scroll_amount)  # Scroll the mouse
        winsound.Beep(1000, 200)  # Beep sound to indicate scroll action
        time.sleep(10)  # Small delay after scrolling to let it take effect
        pyautogui.moveTo(initial_position)  # Move the mouse back to the initial position
        time.sleep(3)
        pyautogui.click()  # Click on the initial position
        pyautogui.click(initial_position.x, initial_position.y - 50)  # Click on top of the initial position
        time.sleep(delay)  # Delay between actions

if __name__ == '__main__':
    clicks = 100  # Number of clicks
    scroll_amount = -1000  # Scroll amount (negative value for scrolling down)
    delay = 8  # Delay between actions in seconds

    print("Auto Clicker with Scroll")
    print("Press Ctrl+C to stop the program.")

    try:
        while True:
            auto_clicker_scroll(clicks, scroll_amount, delay)
    except KeyboardInterrupt:
        print("Program stopped.")


