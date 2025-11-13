from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

from django.http import JsonResponse
from .models import Sermon # Assuming your model is in the same app's models.py

def sermon_list_json(request):
    """
    Returns a JSON list of all sermons.
    """
    # 1. Get all sermon objects
    sermons = Sermon.objects.all().order_by('-date')

    # 2. Prepare the data for JSON serialization
    sermons_data = []
    for sermon in sermons:
        sermons_data.append({
            'id': sermon.id,
            'topic': sermon.topic,
            'preacher': sermon.preacher,
            'date': sermon.date.isoformat(), # Convert date object to string (YYYY-MM-DD)
            # Use the custom methods to get the file URLs
            'audio_url': sermon.get_audio_url(),
            'video_url': sermon.get_video_url(),
            'notes': sermon.notes,
            'created_at': sermon.created_at.isoformat(), # Convert datetime to ISO format string
            'updated_at': sermon.updated_at.isoformat(), # Convert datetime to ISO format string
        })

    # 3. Return the JSON response
    # The 'safe=False' argument is needed because you are passing a list (not a dictionary)
    return JsonResponse(sermons_data, safe=False)



def sermon_details(request, pk):
    sermon = Sermon.objects.get(id= pk)
    sermon = {
            'id': sermon.id,
            'topic': sermon.topic,
            'preacher': sermon.preacher,
            'date': sermon.date.isoformat(), # Convert date object to string (YYYY-MM-DD)
            # Use the custom methods to get the file URLs
            'audio_url': sermon.get_audio_url(),
            'video_url': sermon.get_video_url(),
            'notes': sermon.notes,
            'created_at': sermon.created_at.isoformat(), # Convert datetime to ISO format string
            'updated_at': sermon.updated_at.isoformat(), # Convert datetime to ISO format string
        }
    return JsonResponse(sermon, safe=False)
