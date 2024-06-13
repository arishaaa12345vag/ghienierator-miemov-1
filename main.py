from PIL import Image,ImageDraw,ImageFont #импрортируем модули для работы с картинкой
print("Генератор мемов запущен!")

top_text = input("Введите верхний текст: ") #узнаем у пользователя верхний текст
bottom_text = input("Введите нижний текст: ")# узнаем нижний текст

print(top_text, bottom_text)

print("Список картинок:") #выводим возможный выбор картинок
print("1. кот в ресторане")
print("2. кот в очках")

image_number = int(input("Введите номер картинки ")) #спрашиваем об номере желаемой картинки

if image_number == 1: #если цифра 1- названием файла кот в ресторане
    image_file = 'кот в ресторане.jpeg'

elif image_number == 2: #если цифра 2- названием файла кот в очках
    image_file = 'кот в очках.jpeg'

image = Image.open(image_file) #открываем файл с которым будем работать
weight,height = image.size #узнаем ширину и высоту картинки

draw = ImageDraw.Draw(image) #пространство на котором рисуем

font = ImageFont.truetype('arial.ttf',size = 70) #создаем шрифт

#draw.text((0.0),top_text,font = font,fill = 'black')
text = draw.textbbox((0,0),top_text,font) #отдельно создаем надпись
text_weight = text[2] #ширина текста

draw.text(((weight - text_weight)/2,10),top_text,font=font,fill = 'black') #подсчитываем и прописываем в какое место мы переносим надпись(по середине)


text = draw.textbbox((0,0),bottom_text,font) #тоже самое но + высота
text_weight = text[2]
text_height = text[3]

draw.text(((weight - text_weight)/2,height - text_height - 10),bottom_text,font=font,fill = 'black')

image.save('new_meme.jpeg') #сохраняем картинку

