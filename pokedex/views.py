from django.shortcuts import render

def pokedex(request):
    pokemons = [
        'Bulbasaur', 'Ivysaur', 'Venusaur',
        'Charmander', 'Charmeleon', 'Charizard',
        'Squirtle', 'Wartortle', 'Blastoise'
    ]
    return render(request, 'pokedex/index.html', {'pokemons': pokemons})


def pokemons_details(request, name):
    pokemons_data = {
        "bulbasaur": {
            "tipo": "Planta/Veneno",
            "habilidad": "Overgrow",
            "descripcion": "Una semilla crece en su espalda desde su nacimiento."
        },
        "ivysaur": {
            "tipo": "Planta/Veneno",
            "habilidad": "Overgrow",
            "descripcion": "La planta en su espalda crece al absorber energía solar."
        },
        "venusaur": {
            "tipo": "Planta/Veneno",
            "habilidad": "Overgrow",
            "descripcion": "La flor libera un aroma relajante en combate."
        },
        "charmander": {
            "tipo": "Fuego",
            "habilidad": "Blaze",
            "descripcion": "La llama de su cola indica su estado de salud."
        },
        "charmeleon": {
            "tipo": "Fuego",
            "habilidad": "Blaze",
            "descripcion": "Se vuelve agresivo en combate."
        },
        "charizard": {
            "tipo": "Fuego/Volador",
            "habilidad": "Blaze",
            "descripcion": "Escupe fuego capaz de derretir rocas."
        },
        "squirtle": {
            "tipo": "Agua",
            "habilidad": "Torrent",
            "descripcion": "Se protege dentro de su caparazón."
        },
        "wartortle": {
            "tipo": "Agua",
            "habilidad": "Torrent",
            "descripcion": "Usa su cola para mantener equilibrio al nadar."
        },
        "blastoise": {
            "tipo": "Agua",
            "habilidad": "Torrent",
            "descripcion": "Sus cañones disparan agua a alta presión."
        }
    }

    pokemon = pokemons_data.get(name.lower())

    return render(request, 'pokedex/details.html', {
        'pokemon': pokemon,
        'name': name
    })