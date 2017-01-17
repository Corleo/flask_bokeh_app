# Embedding Bokeh App into Flask App

Flask App and Bokeh App are coded at separeted python scripts and they have to be executed as independent processes like start.sh shell script.

Got **sliders.py** and **fourier_animated.py** from Bokeh 0.12.4 [examples/app](https://github.com/bokeh/bokeh/tree/0.12.4/examples/app).
The **slider_func.py** was modified from [flask_embed.py](https://github.com/bokeh/bokeh/blob/0.12.4/examples/howto/server_embed/flask_embed.py).


## Instructions

Create a conda environment with Flask and Bokeh:

    $ conda create --name flask_bokeh python=2.7 flask=0.12 bokeh=0.12.4

Clone this repo:

    $ git clone this_repo.git

In one terminal, run shell script:

    $ cd this_repo
    $ source start.sh

Go to [http://localhost:8080/](http://localhost:8080/)


## Obs

Use [Git Bash](https://git-for-windows.github.io/) on Windows to be able to execute shell code.
