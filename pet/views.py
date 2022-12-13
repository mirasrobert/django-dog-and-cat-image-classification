from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


from tensorflow import keras

import numpy as np
from keras.utils import load_img
from keras.utils import img_to_array

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def check_image(request):
    if request.method == "POST":
        # Image from form and convert to bytes
        image_file = request.FILES.get('image').file
        # Load the image
        input_image = load_img(image_file, target_size=(200, 200))
        # Load the ML Model
        model = keras.models.load_model('model/model.h5')

        input_image = img_to_array(input_image)
        # Convert single image to a batch.
        input_image = np.array([input_image])
        prediction = model.predict(input_image)
        result = ''

        if prediction[0][0] > .5:
            return redirect('/output/dog/')
        else:
            return redirect('/output/cat/')


def output(request, result):
    if result != 'dog' and result != 'cat':
        return redirect('/')
    else:
        return render(request, 'output.html', {
            'result': result
        })
