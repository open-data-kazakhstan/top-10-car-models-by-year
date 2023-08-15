# Top 10 Best Selling Car Companies Since 2005


## Installation

Clone the repository
```shell
$ git clone https://github.com/open-data-kazakhstan/top-10-car-models-by-year.git
```

Requires Python 3.11.3 

Create a virtual environment and activate it 
```bash
pip install venv
python -m venv /path/to/localrepo
```

Swicth to venv directory by using cd comand
```bash
cd /path/to/localrepo
Scripts/activate
```

Install dependecies in venv by using pip
```bash
pip install -r requirements.txt
```

Run the project:
```bash
python scripts/main.py
```
## Data 

Car data collected by hand from https://auto.vercity.ru/statistics/sales/marks/

We downoladed data from these sources and placed it in the acrhive folder as car_models.csv.

We have processed the source data to make it normalized and derived  several aggregated datasets from it:

* `archive/car_models.csv` - sourсe data
* `data/car.csv` - wranged and transposed data
* `data/csv_expandeds.csv` - expanded main dataset
* `datapackage.json` - conatins all of the key information about our dataset

## Scripts

* `wrang.py`- cleaning and wranging the source data script
* `expand.py` - uses main dataset and expands it to 25 steps to make animation smoother
* `animate.py` - uses matplotlib to create an infographic about car sales for all models
* `datapack.py` - creating datapckage.json file that conatinsall meatadata
* `main.py` - launches all scripts step by step

## Visualization

Final result is visualized data that displays average salary and inflation data


<img src="car.gif" alt="car" width="450" height="800">

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/