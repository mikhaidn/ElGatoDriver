from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


class WindowsAudioDriver:
    """Windows implementation of the AudioDriver protocol"""

    def __init__(self):
        self.mic_muted = self._get_mic_state()
        self.volume_muted = False  # Initialize volume state

    def _get_mic_state(self) -> bool:
        """Get current microphone mute state"""
        try:
            mic = AudioUtilities.GetMicrophone()
            interface = mic.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            return bool(volume.GetMute())
        except Exception:
            return False

    def toggle_mic(self) -> bool:
        """Toggle microphone mute state"""
        try:
            mic = AudioUtilities.GetMicrophone()
            interface = mic.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            # Get current state and toggle it
            current_state = volume.GetMute()
            new_state = not current_state
            volume.SetMute(new_state, None)

            self.mic_muted = new_state
            return new_state
        except Exception as e:
            print(f"Error toggling microphone: {e}")
            return self.mic_muted

    def toggle_volume(self) -> bool:
        """Toggle speaker volume"""
        try:
            speakers = AudioUtilities.GetSpeakers()
            interface = speakers.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            # Get current state and toggle it
            current_state = volume.GetMute()
            new_state = not current_state
            volume.SetMute(new_state, None)

            self.volume_muted = new_state
            return new_state
        except Exception as e:
            print(f"Error toggling volume: {e}")
            return self.volume_muted
