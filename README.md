# Moduł 1

## Co robi moduł rekomendacji?

Poleca filmy na podstawie ocen innych użytkowników. Szuka osoby o podobnym guście i wedlug ich ocen przewiduje jakie filmy moga podobac sie danej osobie. Do porownywania od ocen odejmuje srednia ocen uzytkownikow i wie ktore filmy lubi bardziej, a ktore mniej - i nie ma to wplywu na ti czy wystawia duze czy male oceny. A nastepnie wylicza srednia wazona - osoby bardziej podobne w ocenach mialu wiekszy wplyw na przewidywana ocene filmu i dzieli przez sume wag podobienstwa osob, ktore oceniy film.

## Jak uruchomić moduł?

zainstalowac potrzebne biblioteki 	``pip install pandas scikit-learn flask ``
przejsc do folderu laba i wpisac w terminalu ``python app.py``
po uruchomieniu bedzie serwer Flask dzialal pod adresem `[127.0.0.1:5000](http://127.0.0.1:5000/)`

# Przykładowa odpowiedż api

Jeśli chcemy otrzymać przykladowe rekomendacje dla ani otwieramy adres `[127.0.0.1:5000/api/recommend?user=Ania](http://127.0.0.1:5000/api/recommend?user=Ania)`

```json
{
  "count": 5,
  "recommendations": [
    {
      "because": [
        "Celina",
        "Jacek",
        "Kasia"
      ],
      "predicted": 4.31,
      "title": "Fight Club"
    },
    {
      "because": [
        "Celina"
      ],
      "predicted": 3.08,
      "title": "Forrest Gump"
    },
    {
      "because": [
        "Celina",
        "Jacek",
        "Kasia"
      ],
      "predicted": 2.37,
      "title": "Toy Story"
    },
    {
      "because": [
        "Kasia"
      ],
      "predicted": 2.24,
      "title": "The Shawshank Redemption"
    },
    {
      "because": [
        "Celina",
        "Jacek",
        "Kasia"
      ],
      "predicted": 2.13,
      "title": "Spirited Away"
    }
  ],
  "user": "Ania"
}
```
