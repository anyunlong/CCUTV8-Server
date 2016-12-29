from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from models import Cartoon, Episode

# Create your views here.
@require_http_methods(["GET"])
def cartoons(request):
    cartoons = []
    for cartoonObj in Cartoon.objects.all():
        cartoons.append({
            "name": cartoonObj.name,
            "url": cartoonObj.url
        })
    return JsonResponse({"cartoons": cartoons})

@require_http_methods(["GET"])
def episodes(request):
    cartoon = request.GET["cartoon"]
    episodes = []
    for episodesObj in Episode.objects.filter(cartoon=cartoon):
        episodes.append({
            "title": episodesObj.title,
            "url": episodesObj.url,
            "themeName": cartoon
        })
    return JsonResponse({"episodes": episodes})