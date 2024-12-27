import hid
import time
from PIL import Image, ImageDraw, ImageFont

class MinimalDeck:
    # Stream Deck Mini vendor/product IDs
    VENDOR_ID = 0x0fd9
    PRODUCT_ID = 0x0063  # You may need to verify this ID for your specific model
    
    def __init__(self):
        # Connect to the Stream Deck
        self.device = hid.device()
        self.device.open(self.VENDOR_ID, self.PRODUCT_ID)
        self.device.set_nonblocking(True)
        
    def set_text(self, key_number: int, text: str):
        """Set text on a specific key"""
        # Create a black image
        image = Image.new('RGB', (72, 72), 'black')
        draw = ImageDraw.Draw(image)
        
        # Add text
        font = ImageFont.load_default()
        draw.text((10, 30), text, font=font, fill='white')
        
        # Convert image to bytes
        image_data = image.tobytes()
        
        # Send to Stream Deck
        header = bytearray([0x02, 0x01, key_number, 0x00, 0x00, 0x00, 0x00, 0x00])
        self.device.write(header + image_data)

    def read_keys(self):
        """Read which key was pressed"""
        try:
            data = self.device.read(255)
            if data:
                key_number = data[1]
                key_state = data[3]
                if key_state == 1:  # Key pressed
                    return key_number
        except IOError:
            pass
        return None

# Basic example
if __name__ == "__main__":
    # Initialize
    deck = MinimalDeck()
    
    # Set text on first key
    deck.set_text(0, "Hello!")
    
    print("Press key 0 to see hello world!")
    print("Press Ctrl+C to exit")
    
    # Main loop
    try:
        while True:
            key = deck.read_keys()
            if key == 0:  # First key pressed
                print("Hello World!")
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nExiting...")
        deck.device.close()
