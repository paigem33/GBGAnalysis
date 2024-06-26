# For the Notebook

Download the csv files from https://usu.box.com/s/zf8pc1mw543efnmgte217qdfjczdi9se and add them to the root of the folder.

The files are too large to upload to the repo itself.

# For the Django application:

To populate your local GameBoard table (the list of all board games from the BGG csv) run the migrations and then run the following command: `python manage.py sync_games`. This will take a while to run, but then you will be able to see all the rows in your database via the admin section. 

After that, you are able to run `python mangage.py sync_reviews` to populate your reviews database. This will take several hours. 

Alternatively, you can then run `python manage.py random_reviews` to generate a csv with 10k random items from the reviews. 

Once you sync reviews into your database, you are able to run `python manage.py query_reviews` to see information from the reviews database.

Note: since this code takes so long to run, we recommend referring to the presentation and the report to see the output instead of running it manually. 

These scripts require the `bgg-19m-reviews.csv` file from this kaggle dataset: https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews?select=bgg-19m-reviews.csv
as well as `users.csv` file from this kaggle dataset: https://www.kaggle.com/datasets/thedevastator/board-game-ratings-by-country
and the list of games, `boardgame_ranks.csv`, from https://boardgamegeek.com/wiki/page/BGG_XML_API2#toc1

The files are very large, and thus we opted to have them downloaded directly from kaggle.
