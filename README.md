# berita-crawler

a simple and extensible Indonesian Index News Crawler

## Online Media List :
- Detik.com : "https://news.detik.com/indeks"
- Liputan6.com : "https://www.liputan6.com/indeks"
- Kompas.com : "https://indeks.kompas.com" (only the news site is being indexed)
- CNNIndonesia.com : "https://www.cnnindonesia.com/nasional/indeks/3" (only the nasional site is being indexed)
- Tempo.co : "https://www.tempo.co/indeks" (only the nasional site is being indexed)
- TurnBackHoax : "https://turnbackhoax.id" (HIGHLY EXPERIMENTAL, USE WITH CAUTION)
## Requirements :
- BeautifulSoup4
- requests

## How To Use :
### Setup VirutalEnv
**I recommend you to use virutalenv, but this is completely optional**

- on python > 3.x :

    ```virtualenv venv```

- activate the venv :

    ```.venv/bin/activate```

---
### Using the Program
- Install Requirements

    ```pip install -r requirements.txt```

- Open / Create `main.json` files

    this files is used to determine what task the program will do
    (see more info down below)

- Run the program

    ```python -m main```

