<h2 align="center">Voxel Creatures Generator</h2>

<p align="center">
<a href="https://github.com/RaulSimpetru/voxel-creatures-generator/blob/main/LICENSE"><img alt="License: GPLv3" src="https://img.shields.io/static/v1?label=license&message=GPLv3&color=informational"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Installation

To install the voxel creatures generator [poetry](https://python-poetry.org/docs/) is required.  
After you have installed poetry and cloned this repository you can auto-build a python .venv using: `poetry install`.

## Usage

To run this repository you can use `poetry shell` to start a shell using the auto-built .venv.  
After that you can simply call `python generate.py -h` to see all arguments that must be set. 

The first time you run the script with all the arguments set the input and
output directories are set up for you and the script will stop.  

All you have to do then is to put your data (how to create it is described below under data generation) in
the input directory.   
The next time you run the script all the data will be auto-sorted for you and the creatures generated.

#### Arguments overview

*-h, --help*  
&emsp;&emsp;&emsp;&emsp; show this help message and exit  
*-n NROFCREATURES, --nrOfCreatures NROFCREATURES*  
&emsp;&emsp;&emsp;&emsp; how many creatures to create  
*-i INPUT, --input INPUT*  
&emsp;&emsp;&emsp;&emsp; input path  
*-o OUTPUT, --output OUTPUT*  
&emsp;&emsp;&emsp;&emsp; output path  
*-u, --uniques*  
&emsp;&emsp;&emsp;&emsp; if only unique creatures should be generated

## Data generation

For the generation of data [MagicaVoxel @ ephtracy](https://ephtracy.github.io/#ss-carousel_ss) is recommended. 

Each creature can be created in one `.vox` file (for an example see [this](extra/example.vox)). **Note that the red axis must always show towards you!**

<img src="https://github.com/RaulSimpetru/voxel-creatures-generator/blob/main/extra/docs/body_parts_color_chart.png" alt="alt text"/>

To be able to use this color coding you can use this [special palette](extra/special_pal.png) for MagicaVoxel.

After you have created new body parts you can then export them as `.ply` files by going to `export -> cubes`.  
Then you just have to put the exported files in the input directory.

## Examples
Although the original data used for generation will not be provided, I hope that this examples can show you what 
interesting stuff can be made with the generator.

<img src="https://github.com/RaulSimpetru/voxel-creatures-generator/blob/main/extra/docs/example2.png" alt="alt text"/>
<img src="https://github.com/RaulSimpetru/voxel-creatures-generator/blob/main/extra/docs/example3.png" alt="alt text"/>
<img src="https://github.com/RaulSimpetru/voxel-creatures-generator/blob/main/extra/docs/example4.png" alt="alt text"/>
