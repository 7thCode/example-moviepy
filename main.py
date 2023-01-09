import moviepy.video.fx.all as vfx
from moviepy.editor import *

from os.path import expanduser

class FilePath:
    root = ""

    def __init__(self, root):
        self.root = root

    def full_path(self, filename):
        return os.path.join(self.root, filename)


if __name__ == '__main__':

    # タイトルを合成したクリップと他２つのクリップをクロスフェードで繋いで、BGMを付けて最初と際顔をフェード。

    home = expanduser("~")

    local_root = FilePath(home + "/Desktop/video")

    titleback = VideoFileClip(local_root.full_path('clip0.mp4'))
    title_text_clip = TextClip('タイトル', fontsize=80, font=local_root.full_path('ipag.ttf'), color="white").set_duration(titleback.duration)
    title_clip = CompositeVideoClip([titleback, title_text_clip.set_pos(('center', 'center'))])

    content = VideoFileClip(local_root.full_path('clip1.mp4'))
    content_clip = content.subclip(0, 8)

    screensize = (1800, 300)
    subtitles_clip = TextClip('１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０',  kerning = -2, interline = -1, size = screensize, method = 'caption', fontsize=40, font=local_root.full_path('ipag.ttf'), color="white").set_duration(content.duration)
    main_clip = CompositeVideoClip([content_clip, subtitles_clip.set_pos(('center', 'bottom'))])

    end_clip = VideoFileClip(local_root.full_path('clip2.mp4'))

    bgm_clip = AudioFileClip(local_root.full_path('bgm.m4a'))

    clips = [title_clip,
             main_clip.set_start(5).crossfadein(1).audio_fadein(1),
             end_clip.set_start(9).crossfadein(1).audio_fadein(1)]

    composite_clip = CompositeVideoClip(clips)
    final_clip = composite_clip.set_audio(bgm_clip).set_duration(composite_clip.duration)

    complete_clip = vfx.fadeout(vfx.fadein(final_clip, 1, initial_color=(255, 255, 255)), 1)

    complete_clip.write_videofile(
        local_root.full_path('final.mp4'),
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='final.m4a',
        remove_temp=True)
