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

    ```virtualenv main```

  on python > 3.3 :

  ```python -m venv main```

- activate the virutalenv :

    ```source main/bin/activate```

- deactivate the virtualenv:

    ```deactivate```

---
### Using the Program
- Install Requirements

    ```pip install -r requirements.txt```

- Open / Create `main.json` files

    this files is used to determine what task the program will do
    (see more [here](#json-files))

- Run the program

    ```python -m main```

## JSON Files
this program use a simple json file to determine from which source it needs to take.

a template under the name `main.json` is already available. You can use it as a base.

### Task
```
    "tasks" : [
        {
            "src":"detik",
            "target_length":5,
            "start_date": "29/3/2021"
        }
    ]
```

**available parameter**
|    params     | required |                              options                              |                   description                    |            default             |
| :-----------: | :------: | :---------------------------------------------------------------: | :----------------------------------------------: | :----------------------------: |
|      src      | required | "detik", "liputan6", "cnnIndo", "kompas", "tempo", "turnbackhoax" |              the source of the news              |                                |
| target_length | required |                                                                   |             how many news is crawled             |                                |
|  start_date   | optional |                                                                   |  the start date of the news (format dd/mm/yyyy)  | system date (`datetime.now()`) |
|   end_date    | optional |                                                                   | the maximum date of the news (format dd/mm/yyyy) | system date (`datetime.now()`) |

### Output
```
    "output": {
        "type": "csv",
        "name": "result.csv"
    }
```

**available parameter**
| params | required | options |     description      |   default    |
| :----: | :------: | :-----: | :------------------: | :----------: |
|  type  | required |  "csv"  | the output file type |              |
|  name  | optional |         | the output file name | "output.csv" |



