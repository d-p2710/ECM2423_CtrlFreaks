from django.shortcuts import render
from PIL import Image
from io import BytesIO
import base64
from users.models import Profile, Avatar, Item, OwnedItem
from django.http import HttpResponse

#page views
def home_page(request):
    return render(request, 'app/homePage.html')

def profile(request):

    def sortItemsByType(item_list):
        # TODO function that takes list of items and returns dictionary,
        # of those items, sorted by part_type / category
        items_dict = {"colour":[], "mouth":[], "eyes":[], "headwear":[], "accessory":[]}
        for item in item_list:
            # if item.part_type
            pass

    marker = request.user.id
    profile = Profile.objects.filter(user=marker)[0]
    avatar = Avatar.objects.filter(profile=profile)[0]
    all_items = Item.objects.all()
    owned_item_objects = OwnedItem.objects.filter(profile=profile)
    context = {
        'profile_data': profile,
        'avatar_data': avatar,
        'all_items': all_items,
        # 'owned_items': owned_items
    }
    return render(request, 'app/profilePage.html', context)
    # return HttpResponse(avatar.colour.img_file.url)

#avatar shop views
# def avatar(request):
#     marker = request.user.id
#     if request.method == "POST":


#QR views
def qr_generator(request):
    context = {}
    if request.method == "POST":
        qr_text = request.POST.get("qr_text", "")
        qr_image = qrcode.make(qr_text, box_size=15)
        qr_image_pil = qr_image.get_image()
        stream = BytesIO()
        qr_image_pil.save(stream, format='PNG')
        qr_image_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
        context['qr_image_base64'] = qr_image_base64
        context['variable'] = qr_text
    return render(request, 'app/qrGenerator.html', context=context)

def qr_scanner(request):
    return render(request, 'app/qrScanner.html')


def geolocation_map(request):
    return render(request, 'app/geolocationMap.html')


def game_map(request):
    return render(request, 'app/gameMap.html')

#log in views
def logout(request):
    if request == 'POST':
        logout(request)

