from subedit.assets.tracks import AudioTrackSnapshot, TrackSnapshot, VideoTrackSnapshot, SubtitleTrackSnapshot
from subedit.adapters.mkvmerge import MKVMergeAudioAdapter, MKVMergeSubtitleAdapter, MKVMergeVideoAdapter
from uuid import UUID


class AssetProxy:
    def __init__(self, original_asset, uuid: UUID):
        super().__setattr__('_original', original_asset)
        super().__setattr__('_changes', {})
        super().__setattr__('_uuid', uuid)

    def __getattr__(self, name):
        changes = object.__getattribute__(self, '_changes')
        if name in changes:
            return changes[name]
        original = object.__getattribute__(self, '_original')
        return getattr(original, name)

    def __setattr__(self, name, value):
        if name in ('_original', '_changes'):
            super().__setattr__(name, value)
            return

        if not hasattr(self._original, name):
            raise AttributeError(f"A propriedade '{name}' não existe no objeto original.")

        original_value = getattr(self._original, name, None)
        if value == original_value:
            if name in self._changes:
                del self._changes[name]
        else:
            self._changes[name] = value

    def __delattr__(self, name):
        # Restaura ao original deletando do buffer de mudanças
        if name in self._changes:
            del self._changes[name]

    def _get_changes(self) -> dict:
        return self._changes.copy()

    def __dir__(self) -> dict:
        return dir(self._original)


class Track(AssetProxy):
    def __init__(self, original: TrackSnapshot, uuid: UUID):
        super().__init__(original, uuid)


class AudioTrack(Track):
    def __init__(self, audio_adapter: MKVMergeAudioAdapter, uuid: UUID):
        audio = AudioTrackSnapshot(**vars(audio_adapter))
        super().__init__(audio, uuid)


class SubtitleTrack(Track):
    def __init__(self, subtitle_adapter: MKVMergeSubtitleAdapter, uuid: UUID):
        subtitle = SubtitleTrackSnapshot(**vars(subtitle_adapter))
        super().__init__(subtitle, uuid)


class VideoTrack(Track):
    def __init__(self, video_adapter: MKVMergeVideoAdapter, uuid: UUID):
        video = VideoTrackSnapshot(**vars(video_adapter))
        super().__init__(video, uuid)
