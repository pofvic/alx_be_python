weather_condition = input("what's the weather like today? (sunny/rainy/cold) ")

if weather_condition == 'sunny':
    print("Wear a t-shirt and sunglasses")
elif weather_condition == 'rainy':
    print("Don't forget your umbrella and a raincoat")
elif weather_condition == 'cold':
    print('Make sure to wear a warm coat and a scarf')
else:
    print('Sorry, i have a recommendation for this weather')
