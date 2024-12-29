import subprocess
import sys
from typing import Protocol

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

class WindowsAudioDriver:
    """Windows implementation of the AudioDriver protocol"""
    def __init__(self):
        self.mic_muted = False
        self.volume_muted = False
    
    def toggle_mic(self) -> bool:
        """Toggle microphone using Windows PowerShell commands"""
        subprocess.run(["powershell", "-c", "(New-Object -ComObject WScript.Shell).SendKeys([char]174)"])
        self.mic_muted = not self.mic_muted
        return self.mic_muted
    
    def toggle_volume(self) -> bool:
        """Toggle volume using Windows PowerShell commands"""
        subprocess.run(["powershell", "-c", "(New-Object -ComObject WScript.Shell).SendKeys([char]173)"])
        self.volume_muted = not self.volume_muted
        return self.volume_muted

class MacAudioDriver:
    """macOS implementation of the AudioDriver protocol"""
    def __init__(self):
        self.mic_muted = False
        self.volume_muted = False
    
    def toggle_mic(self) -> bool:
        """Toggle microphone using AppleScript commands"""
        volume = "0" if not self.mic_muted else "100"
        subprocess.run(["osascript", "-e", f'set volume input volume {volume}'])
        self.mic_muted = not self.mic_muted
        return self.mic_muted
    
    def toggle_volume(self) -> bool:
        """Toggle volume using AppleScript commands"""
        subprocess.run(["osascript", "-e", 'set volume output muted not (output muted of (get volume settings))'])
        self.volume_muted = not self.volume_muted
        return self.volume_muted

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