import hid
import time
from button_enums import StreamDeckNeoButton
from PIL import Image, ImageDraw, ImageFont
from audio.driver_protocol import get_audio_driver


class StreamDeckNeo:
    # Stream Deck Mini vendor/product IDs
    VENDOR_ID = 0x0FD9
    PRODUCT_ID = 0x009A  # You may need to verify this ID for your specific model

    def __init__(self):
        # Connect to the Stream Deck
        self.device = hid.device()
        self.device.open(self.VENDOR_ID, self.PRODUCT_ID)
        self.device.set_nonblocking(True)
        self.counter = 0
        self.audio = get_audio_driver()

    # DOES NOT WORK
    def set_text(self, key_number: int, text: str):
        """Set text on a specific key"""
        # Create a black image
        image = Image.new("RGB", (72, 72), "cyan")
        draw = ImageDraw.Draw(image)

        # Add text
        font = ImageFont.load_default()
        draw.text((10, 30), text, font=font, fill="white")

        # Convert image to bytes
        image_data = image.tobytes()

        # Send to Stream Deck
        header = bytearray([0x02, 0x01, key_number, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.device.write(header + image_data)

    def read_keys(self):
        try:
            data = self.device.read(255)
            if data:
                buttons = []
                for button in StreamDeckNeoButton:
                    if data[button.value] == 1:
                        buttons.append(button)
                return buttons
        except IOError:
            pass
        return []

    def handle_keys(self, key_positions):
        if len(key_positions) > 1:
            print("CHORD is hit!", f"{[k.name for k in key_positions]}")
        for key_position in key_positions:
            if key_position == StreamDeckNeoButton.TOP_LEFT:
                self.audio.toggle_mic()
                if self.audio.mic_muted:
                    print("mic is muted")
                else:
                    print("mic is on")
            elif key_position == StreamDeckNeoButton.TOP_CENTER_LEFT:
                self.audio.toggle_volume()
                if self.audio.volume_muted:
                    print("volume is muted")
                else:
                    print("volume is on")
            elif key_position == StreamDeckNeoButton.TOP_CENTER_RIGHT:
                print("TOP_CENTER_RIGHT hit!")
            elif key_position == StreamDeckNeoButton.TOP_RIGHT:
                print("TOP_RIGHT hit!")
            elif key_position == StreamDeckNeoButton.BOTTOM_LEFT:
                print("BOTTOM_LEFT hit!")
            elif key_position == StreamDeckNeoButton.BOTTOM_CENTER_LEFT:
                print("BOTTOM_CENTER_LEFT hit!")
            elif key_position == StreamDeckNeoButton.BOTTOM_CENTER_RIGHT:
                print("BOTTOM_CENTER_RIGHT hit!")
            elif key_position == StreamDeckNeoButton.BOTTOM_RIGHT:
                print("BOTTOM_RIGHT hit!")
            elif key_position == StreamDeckNeoButton.TOUCH_SENSOR_LEFT:
                print("TOUCH_SENSOR_LEFT hit!")
            elif key_position == StreamDeckNeoButton.TOUCH_SENSOR_RIGHT:
                print("TOUCH_SENSOR_RIGHT hit!")


if __name__ == "__main__":
    deck = StreamDeckNeo()

    print("Listening for keypresses...")

    try:
        while True:
            key_position = deck.read_keys()
            deck.handle_keys(key_position)
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nExiting...")
        deck.device.close()
