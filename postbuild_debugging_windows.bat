CALL conda install nodejs -y
CALL conda install -c conda-forge xeus-python=0.7.1 ptvsd -y
CALL conda install -c conda-forge jupyterlab=2 -y
CALL jupyter labextension update --all
CALL jupyter labextension install @jupyterlab/debugger

:: https://github.com/jupyterlab/jupyter-renderers#looking-for-plotly-extension
:: now our old plotly-version would break, so...
CALL jupyter labextension uninstall @jupyterlab/plotly-extension
CALL conda install -c plotly plotly==4.7.1 -y
CALL conda install ipywidgets=7.5 -y
CALL jupyter labextension install jupyterlab-plotly@4.7.1
CALL jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.7.1

CALL jupyter lab build 
