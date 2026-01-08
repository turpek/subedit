class MKVMergeTrackAdapter:
    def __init__(self, data: dict):
        prop = data.get('properties', {})
        self.id = data['id']
        self.uid = prop.get('uid', None)
        self.codec = data['codec']
        self.codec_id = prop.get('codec_id', "")
        self.default_track = prop.get('default_track', True)
        self.enabled_track = prop.get('enabled_track', True)
        self.forced_track = prop.get('forced_track', False)
        self.language = prop.get('language', 'eng')
        self.language_ietf = prop.get('language_ietf', None)
        self.number = prop.get('number', 0)
        self.track_name = prop.get('track_name', "")
        self.default_duration = prop.get('default_duration', None)
        self.flag_hearing_impaired = prop.get('flag_hearing_impaired', False)
        self.flag_visual_impaired = prop.get('flag_visual_impaired', False)
        self.flag_text_descriptions = prop.get('flag_text_descriptions', False)
        self.flag_original = prop.get('flag_original', False)
        self.flag_commentary = prop.get('flag_commentary', False)


class MKVMergeAudioAdapter(MKVMergeTrackAdapter):
    def __init__(self, data: dict):
        super().__init__(data)

        prop = data.get('properties', {})
        self.audio_channels = prop.get('audio_channels', None)
        self.audio_emphasis = prop.get('audio_emphasis', None)

        acc_key = prop.get('aac_is_sbr', None)
        acc_is_sbr = {'true': True, 'false': False}
        self.aac_is_sbr = acc_is_sbr.get(acc_key, None)


class MKVMergeSubtitleAdapter(MKVMergeTrackAdapter):
    def __init__(self, data: dict):
        super().__init__(data)

        prop = data.get('properties', {})
        self.encoding = prop.get('encoding', '')
        self.text_subtitles = prop.get('text_subtitles', None)


class MKVMergeVideoAdapter(MKVMergeTrackAdapter):
    def __init__(self, data: dict):
        super().__init__(data)

        prop = data.get('properties', {})
        self.display_dimensions = prop.get('display_dimensions', None)
        self.stereo_mode = prop.get('stereo_mode', None)
        self.field_order = prop.get('field_order', None)
        self.color_range = prop.get('color_range', None)
        self.color_primaries = prop.get('color_primaries', None)
        self.color_transfer_characteristics = prop.get('color_transfer_characteristics', None)
        self.color_matrix_coefficients = prop.get('color_matrix_coefficients', None)
