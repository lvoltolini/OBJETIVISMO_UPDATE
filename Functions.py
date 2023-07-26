import os # Check dir_path and create a "Videos" folder.
import json

from pytube import YouTube # Importa la classe "YouTube" dal modulo "pytube"
from pytube import Playlist # Importa la classe "Playlist" per il download di Playlists

from moviepy.video.io.VideoFileClip import VideoFileClip # Importa la classe "VideoFileClip" dal modulo "moviepy.video.io.VideoFileClip"


dir_path = os.path.dirname(os.path.abspath(__file__))

# Imposta la directory di lavoro corrente sulla directory che contiene lo script principale
os.chdir(dir_path)

# Crea la cartella per salvare il film.
master_path = os.getcwd() + '//'
path_videos = os.getcwd() + '//Videos//'
if not os.path.exists(path_videos):
        os.makedirs(path_videos)
        
class Pyvideo:
        @staticmethod
        def convert_time_to_seconds(min, sec): # FUNZIONE DEPRECATA
                # Converte il tempo da minuti e secondi a secondi
                correct_rime = int(min)*60 + float(sec)
                return correct_rime
        
        @staticmethod
        def check_path_exist(path):
                if os.path.exists(path):
                        print(f"{path} already exists.")
                        return True
        
        @staticmethod
        def convert_to_mp3(video, mp3_folder = master_path):
                if type(video) == str:
                        mp3_name = video.split('//')[-1].replace('mp4', 'mp3')
                        print(mp3_name)
                        video =  VideoFileClip(video)
                else: 
                        print(type(video))
                        mp3_name = video.title
                
                audio = video.audio 
                return audio, mp3_name
        
        @staticmethod
        def save_audiofile(audio, filename):
                audio.write_audiofile(filename)
                
        @staticmethod
        def segment_video(video, 
                          start_time, end_time, 
                          output_prefix_filename,
                          format = 'mp4'):
                if type(video) == str:
                        video =  VideoFileClip(video)
                if start_time < end_time:
                        # Estrae il segmento di video specificato
                        segmento = video.subclip(start_time, end_time)

                        # Salva il segmento di video
                        segment_path = f"{os.getcwd()}//Videos//segment_{output_prefix_filename}.{format}"
                        if Pyvideo.check_path_exist(segment_path):
                                return
                        segmento.write_videofile(segment_path, codec="libx264")
                        
        @staticmethod
        def download(url,  
                     output_prefix_filename = 'video'):

                #print('start:', start_time, 'end:', end_time)
                
                # Crea un oggetto YouTube usando l'URL fornito
                yt = YouTube(url)

                # Scarica il video con la qualità progressiva e l'estensione mp4
                video_path = yt.streams.filter(
                        progressive = True, file_extension = 'mp4'
                        ).order_by(
                                'resolution'
                                ).desc().first().download()

                # Rinomina il file video scaricato
                mp4_name = f"{path_videos}Video_{output_prefix_filename}.mp4"
                if Pyvideo.check_path_exist(mp4_name):
                        return
                os.rename(video_path, mp4_name)
                
                return mp4_name

        @staticmethod 
        def download_playlist(link, format, remove = False):
                # Download logic
                playlist_obj = Playlist(link)
                print(f'Downloading: {playlist_obj.title}')
                
                # Create the folder
                playlist_folder = os.path.join(os.getcwd(), "Playlist")
                        
                for index, video in enumerate(playlist_obj.videos):
                        errors = list()
                        # Download each video in the playlist
                        print(f'Downloading {video.title}')
                        video.streams.filter(progressive = True, file_extension = 'mp4').first().download(output_path=playlist_folder)
                        
                        if format == 'mp3':
                                # Convert the downloaded video to MP3
                                mp4_file_path = f"{playlist_folder}//{video.title}.mp4"
                                try: audiofile, name_audiofile = Pyvideo.convert_to_mp3(mp4_file_path)
                                except: errors += [mp4_file_path]
                                else: Pyvideo.save_audiofile(audiofile, os.path.join(playlist_folder, name_audiofile))
                return errors
                

if __name__ == '__main__':
        
        dict_of_options = {
                'segment': [Pyvideo.segment_video, 
                            
                            ]        
        }
        # print('Testando download')
        # file = Pyvideo.download('https://www.youtube.com/watch?v=FFkKm_4FOFE')
        # print('Testando convert')
        # audio, mp3_name = Pyvideo.convert_to_mp3(file)
        # print('Testando save')
        # Pyvideo.save_audiofile(audio, mp3_name)
        print('Testando segment')
        Pyvideo.segment_video(
                'D:\WORKSPACE\OBJETIVISMO BRASIL\Videos\Video_Rand_sentimento.mp4', 
                Pyvideo.convert_time_to_seconds(9,58), Pyvideo.convert_time_to_seconds(12, 48), 
                'rand_pelo_que_devemos_lutar')
        # print('Testando playlist')
        # print(Pyvideo.download_playlist('https://www.youtube.com/playlist?list=PLwDC6BK_89J2l-tIIgaJJIlfYAO9_LR_N', 'mp3'))

