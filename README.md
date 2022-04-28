# RainbowSix-Rating


## Character table

1. id - identity value of the character.
2. character_name - name of character.
3. side - side of character.
4. talent - talent of character.


## Rating table

1. id - identity value of character.
2. user_name - identity value of the movie.
3. rating - rating value of character.

## Setup

1. Clone this project repository to your machine.

    ``` 
    git clone https://github.com/borrabeam/RainbowSix-rating.git
    ```

2. Install all required packages.

    ```
    pip install -r requirements.txt
    ```

3. Create your sample database.

    ```
    sqlite3 rainbow_data.db < rainbow.schema
    ```

4. Import csv data into the database.

    ```
    sqlite3 character_data.db
    sqlite3> .import data/Character_data.csv character
    sqlite3> .import data/Rating_data.csv rating
    sqlite3> .quit
    ```


