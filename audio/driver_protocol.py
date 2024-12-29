import subprocess
import sys
from typing import Protocol

from audio.mac_driver import MacAudioDriver
from audio.windows_driver import WindowsAudioDriver


class AudioDriver(Protocol):
    """Protocol defining the interface for platform-specific audio drivers"""

    def toggle_mic(self) -> bool:
        """Toggle microphone mute state

        Returns:
            bool: True if muted, False if unmuted
        """
        ...

    def toggle_volume(self) -> bool:
        """Toggle speaker volume mute state

        Returns:
            bool: True if muted, False if unmuted
        """
        ...


def get_audio_driver() -> AudioDriver:
    """Factory function to get the appropriate audio driver for the current platform

    Returns:
        AudioDriver: Platform-specific audio driver implementation

    Raises:
        RuntimeError: If the current platform is not supported
    """
    if sys.platform == "win32":
        return WindowsAudioDriver()
    elif sys.platform == "darwin":
        return MacAudioDriver()
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")


# Example usage:
if __name__ == "__main__":
    driver = get_audio_driver()
    is_muted = driver.toggle_mic()
    print(f"Microphone {'muted' if is_muted else 'unmuted'}")
