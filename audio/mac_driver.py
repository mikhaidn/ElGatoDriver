import subprocess

class MacAudioDriver:
    """macOS implementation of the AudioDriver protocol"""

    def __init__(self):
        self.mic_muted = False
        self.volume_muted = False

    def toggle_mic(self) -> bool:
        """Toggle microphone using AppleScript commands"""
        volume = "0" if not self.mic_muted else "100"
        subprocess.run(["osascript", "-e", f"set volume input volume {volume}"])
        self.mic_muted = not self.mic_muted
        return self.mic_muted

    def toggle_volume(self) -> bool:
        """Toggle volume using AppleScript commands"""
        subprocess.run(
            [
                "osascript",
                "-e",
                "set volume output muted not (output muted of (get volume settings))",
            ]
        )
        self.volume_muted = not self.volume_muted
        return self.volume_muted
