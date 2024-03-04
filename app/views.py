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
        # take list of items, return dictionary sorted by category
        items_dict = {"colour":[], "mouth":[], "eyes":[], "headwear":[], "accessory":[]}
        for item in item_list:
            items_dict[item.category].append(item)
        return items_dict

    marker = request.user.id
    profile = Profile.objects.get(user=marker)
    avatar = Avatar.objects.get(profile=profile)
    all_items = sortItemsByType(Item.objects.all())
    owned_item_ids = []
    owned_item_relations = OwnedItem.objects.filter(profile=profile)
    for relation in owned_item_relations:
        owned_item_ids.append(relation.item.id)
    context = {
        'profile_data': profile,
        'avatar_data': avatar,
        'all_items': all_items,
        'owned_item_ids': owned_item_ids,
    }
    return render(request, 'app/profilePage.html', context)
    # return HttpResponse(sortItemsByType(owned_item_list)["colour"][0].img_file.url)

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

