from moviepy.editor import *
import moviepy.video.fx.all as vfx

class FilePath:

    root = ""

    def __init__(self, root):
        self.root = root

    def full_path(self, filename):
        return os.path.join(self.root, filename)

if __name__ == '__main__':

    # タイトルを合成したクリップと他２つのクリップをクロスフェードで繋いで、BGMを付けて最初と際顔をフェード。

    local_root = FilePath("/Users/xxxx/Desktop/video")
    title = VideoFileClip(local_root.full_path('clip0.mp4'))
    text_clip = TextClip('タイトル', fontsize=80, font=local_root.full_path('xxxx.ttc'), color="white")
    title_composite_clip = CompositeVideoClip([title, text_clip.set_pos(('center', 'center'))])

    title_clip = title_composite_clip.set_duration(title.duration)

    cut_clip = VideoFileClip(local_root.full_path('clip1.mp4'))
    main_clip = cut_clip.subclip(0, 8)

    end_clip = VideoFileClip(local_root.full_path('clip2.mp4'))

    bgm_clip = AudioFileClip(local_root.full_path('bgm.m4a'))

    clips = [title_clip,
            main_clip.set_start(5).crossfadein(1).audio_fadein(1),
            end_clip.set_start(9).crossfadein(1).audio_fadein(1)]

    composite_clip = CompositeVideoClip(clips)
    final_clip = composite_clip.set_audio(bgm_clip).set_duration(composite_clip.duration)

    complete_clip = vfx.fadeout(vfx.fadein(final_clip, 1, initial_color=(255,255,255)), 1)

    complete_clip.write_videofile(
        local_root.full_path('final.mp4'),
        codec='libx264',
        audio_codec='aac',
        temp_audiofile= 'final.m4a',
        remove_temp=True)