
# Setting up the environment 

Welcome. Before you can start with the module, we need to make sure that you and your computer both are ready. Follow these steps 

1. Go to Anaconda Prompt. 
2. Type the following command: 
`conda create -n simvis python=3.6`
3. Activate the environment with the following command: 
`conda activate simvis`
**Note that the virtual environment we are creating is in for python 3.6. You may have Anaconda Prompt with maybe version 3.7 or above, do not worry. When specifying `python=3.6` you create an environment with version 3.6 despite whatever version of Anaconda you own**
4. Now download the following wheel files from the google drive folder <a href="https://drive.google.com/open?id=1-3R4ecMf1YHQC9D7utkUvrxJEcZNuZYD">here</a> 
5. Following the download, browse through the folder where you saved these files. Foe example if they are saved in a folder with directory:  `C:\Users\admin\Downloads`, navigate through the Anaconda Prompt by typing `cd C:\Users\admin\Downloads`
6. Now use the following commands: 

`pip install rasterio-1.1.2-cp36-cp36m-win_amd64.whl`

`pip install Shapely-1.7.0-cp36-cp36m-win_amd64.whl`

`pip install Fiona-1.8.13-cp36-cp36m-win_amd64.whl`

`pip install GDAL-3.0.4-cp36-cp36m-win_amd64.whl`

`pip install geopandas-0.7.0-py3-none-any.whl`

`pip install pyshp-2.1.0-py2.py3-none-any.whl`
7. Now we have succesfully installed all the files which require a lot of work due to their dependencies in a few seconds. Finally we will install the requirements.txt 

`pip install -r requirements.txt`
8. You are now done. You can now start spyder or jupyter notebook by typing either `spyder` (Some versions use `spyder3` command) or `jupyter notebook`  
