# start.sh

python app_bokeh.py &
python app_flask.py && fg

# Util commands:
#   * jobs:
#       - returns the process ID (PID) pushed to background
#   * kill %<job_number>:
#       - kill the process with job_number
