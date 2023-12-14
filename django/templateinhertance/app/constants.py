from django.shortcuts import render


dic = {
    'kohli': {'image_path': 'images/viratkholi.jpg', 'content': 'Kohli has often expressed his admiration for the cover drive, which he considers to be his signature stroke.'},
    'kaur': {'image_path': 'images/kaur.jpg', 'content': 'Kaur was born on 8 March 1989 in Moga, Punjab, to Harmandar Singh Bhullar, a volleyball and basketball player and Satwinder Kaur'},
    'dhoni': {'image_path': 'images/dhoni.jpg', 'content': '''Mahendra Singh Dhoni (born 7 July 1981) is an Indan professional cricketer, who plays as a wicket-keeper-batsman. Widely regarded as one of the world's greatest wicket-keeper-batsmen and captains in the history of the sport,[a] he is known for his explosive batting, wicket-keeping and leadersh'''}}
def player_view(request, name):
    data = dic.get(name)
    return render(request, 'home.html', {'name': name, 'data': data})
