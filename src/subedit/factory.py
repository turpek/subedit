from pathlib3x import Path
from subedit.assets import Attachment, AudioTrack, SubtitleTrack, VideoTrack
from subedit.asset_builder import MKVMergeAssetBuilder
from subedit.adapter import MKVMergeAttachmentAdapter, MKVMergeTrackAdapter
from subedit.readers import JSONReader
from subedit.media_enums import MediaType
from subedit.media_enums import Provider
from subprocess import run, PIPE


class MKVMergeFactory:
    def __init__(self, path: Path):
        self.__command = ['mkvmerge', '-J', f'{path}']

    def build(self) -> MKVMergeAssetBuilder:
        bjson = run(self.__command, stdout=PIPE)
        data = JSONReader.read(bjson.stdout)
        builder = MKVMergeAssetBuilder(data)
        builder.register_type(MKVMergeAttachmentAdapter, Attachment, MediaType.ATTACHMENT)
        builder.register_type(MKVMergeTrackAdapter, AudioTrack, MediaType.AUDIO)
        builder.register_type(MKVMergeTrackAdapter, VideoTrack, MediaType.VIDEO)
        builder.register_type(MKVMergeTrackAdapter, SubtitleTrack, MediaType.SUBTITLE)
        builder.build()
        return builder


class Factory:
    _provider = {
        Provider.MKVMERGE: MKVMergeFactory,
    }

    @staticmethod
    def build_parse(path: Path, provider: Provider):
        factory = Factory._provider[provider](path)
        return factory.build()
