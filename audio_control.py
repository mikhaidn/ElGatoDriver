import subprocess
import sys 

class AudioControl:
    def __init__(self):
        self.mic_muted = False
        self.volume_muted = False
    
    def toggle_mic(self):
        if sys.platform == "darwin":  # macOS
            # Toggle input volume between 0 and 100
            volume = "0" if not self.mic_muted else "100"
            subprocess.run(["osascript", "-e", f'set volume input volume {volume}'])
        elif sys.platform == "win32":  # Windows
            subprocess.run(["powershell", "-c", "(New-Object -ComObject WScript.Shell).SendKeys([char]174)"])
        
        self.mic_muted = not self.mic_muted
        return self.mic_muted

    def toggle_volume(self):
        if sys.platform == "darwin":  # macOS
            subprocess.run(["osascript", "-e", 'set volume output muted not (output muted of (get volume settings))'])
        elif sys.platform == "win32":  # Windows
            subprocess.run(["powershell", "-c", "(New-Object -ComObject WScript.Shell).SendKeys([char]173)"])
            
        self.volume_muted = not self.volume_muted
        return self.volume_muted