from django.http import HttpResponse
from django.shortcuts import render
from color_mathcher.models import Colors
import requests

def adding_color(request):
    if request.method == "POST":
        params = request.POST
        invert_r = 255 - int(params["obsRed"])
        invert_g = 255 - int(params["obsGreen"])
        invert_b = 255 - int(params["obsBlue"])
        new_obs = Colors(
            red = params["obsRed"],
            green = params["obsGreen"],
            blue = params["obsBlue"],
            i_red = invert_r,
            i_green = invert_g,
            i_blue = invert_b
        )
    else:
        new_obs = Colors(
            red = "0",
            green = "0",
            blue = "0",
            i_red = 255,
            i_green = 255,
            i_blue = 255
        )
    data = {"obs" : new_obs}
    return render(request, "color_mathcher/color_invert.html", data)
        #new_obs.save()
    #all_obs = Colors.objects.all()
    #ave_color = 0
    # data = {"red_val" : ave_color, "green_val" : ave_color, "blue_val" : ave_color}
    #return render(request, "weather/display_my_weather.html", all_obs)
    return HttpResponse("Hello")