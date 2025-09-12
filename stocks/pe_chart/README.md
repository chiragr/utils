# Onetime Setup

PreReq: Python3

```
python3 -m venv Python-Envs/charting
source Python-Envs/charting/bin/activate
pip3 install pandas plotly
```

# Download/Refresh Data

This needs to be run first during the initial setup and then whenever you wish to refresh the data. Ideally this is needed only once a week.

Note that some indices done have enough data, and hence those lines are commented. They can be uncommented if needed.

```
./download_data.sh
```

# Execute Script

```
python3 pe_charts.py <number of days for moving averge>

E.g.:

python3 pe_charts.py 200
```
