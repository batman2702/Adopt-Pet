from flask import Flask
from helper import pets
app=Flask(__name__)


@app.route('/')
def index():
  return f'''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  '''
@app.route('/animals/<pet_type>')
def animals(pet_type):
  html=f'<ul>'
  for idx,pet in enumerate(pets[pet_type]):
    html+="<li>"+f'''<a href='/animals/{pet_type}/{idx}'>'''+pet['name']+"</a></li>"
  #html=f'''<h1>List of {pet_type}</h1>'''
  html+=f'</ul>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type,pet_id):
  pet=pets[pet_type][pet_id]
  return f'''<h1>{pet['name']}</h1>
  <p>{pet['description']}</p>
  <img src="{pet['url']}">
  '''

