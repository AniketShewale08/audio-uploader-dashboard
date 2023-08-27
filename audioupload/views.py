# views.py

from django.shortcuts import render
from django.views import View
from .forms import AudioUploadForm
from .models import UploadedAudio
from pydub import AudioSegment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

class DashboardView(View):
    template_name = 'dashboard.html'
    form_class = AudioUploadForm

    def calculate_audio_duration(self, audio_file):
        audio = AudioSegment.from_file(audio_file)
        duration_seconds = len(audio) // 1000  # Convert from milliseconds to seconds (using integer division)
        return duration_seconds

    def get(self, request, *args, **kwargs):
        uploaded_files = UploadedAudio.objects.all()
        form = self.form_class()

        context = {
            'form': form,
            'uploaded_files': uploaded_files,
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            audio_files = request.FILES.getlist('audio_files')

            # Get or create a default user for uploaded files
            default_user, _ = User.objects.get_or_create(username='default_user')

            total_uploaded_duration = sum(file.duration for file in UploadedAudio.objects.filter(user=default_user))

            for audio_file in audio_files:
                extension = audio_file.name.split('.')[-1]
                size = audio_file.size

                # Calculate audio duration in seconds
                duration = self.calculate_audio_duration(audio_file)

                if total_uploaded_duration + duration <= 600:  # 10 minutes in seconds
                    UploadedAudio.objects.create(user=default_user, audio_file=audio_file, duration=duration, extension=extension, size=size)
                    total_uploaded_duration += duration
                else:
                    # Handle case where total duration exceeds 10 minutes
                    warning = "Total duration of uploaded files exceeds 10 minutes. Please remove some files."
                    uploaded_files = UploadedAudio.objects.filter(user=default_user)
                    context = {'form': form, 'uploaded_files': uploaded_files, 'warning': warning}
                    return render(request, self.template_name, context)

        return self.get(request, *args, **kwargs)




def delete_song(request, song_id):
    song = UploadedAudio.objects.get(id=song_id)
    song.delete()
    return HttpResponseRedirect(reverse('dashboard'))

