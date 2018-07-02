# PixPlot

## PLACEHOLDER README

<p class="welcome">This page visualizes 7,384 <a href="https://dp.la/search?q=%22fourth%20of%20july%22%20OR%20%22independence%20day%22%20OR%20%22July%204th%22%20OR%20%22July%20Fourth%22&type=%22image%22&page=1">"Fourth of July"</a> (and related search) images from <a href="https://dp.la/">Digital Public Library of America</a> (DPLA), which aggregates cultural heritage metadata from thousands of institutions.</p>
<p class="welcome">Under the hood is a WebGL model of how the <a href='https://www.cs.unc.edu/~wliu/papers/GoogLeNet.pdf' target='_blank'>Inception</a> Convolutional Neural Network perceives "relatedness" and then a mapping of the computed relationships into 3-dimensional space using <a href='https://github.com/lmcinnes/umap' target='_blank'>UMAP</a> algorithm such that similar images appear near each other.</p>
<p class="welcome">Except for a few small modifications, this is based on the work and code published by the Yale Digital Humanities Labs in their <a href="https://github.com/yaledhlab/pix-plot">PixPlot repository</a>, which I learned about through an excellent <a href="https://vimeo.com/274922887">video presentation</a> from a Coalition for Networked Information (CNI) <a href="https://www.cni.org/topics/special-collections/neural-networks-machine-vision-for-the-visual-archive">project briefing</a>.</p>
--- 
<h3 class="welcome">Controls:</h3>
<p class="welcome">Click the clusters on the left to zoom to those areas, or use the mouse to navigate on your own.</p>
<p class="welcome">Clicking an item will center the camera to that image, and double-clicking an item will take you to the record for that image in DPLA.</p>

<!-- This repository contains code that can be used to visualize tens of thousands of images in a two-dimensional projection within which similar images are clustered together. The image analysis uses Tensorflow's Inception bindings, and the visualization layer uses a custom WebGL viewer.

![App preview](./assets/images/preview.png?raw=true)

## Dependencies

To install the Python dependencies, you can run (ideally in a virtual environment):

```bash
pip install -r utils/requirements.txt
```

If you have an NVIDIA GPU, consider replacing `tensorflow` with `tensorflow-gpu` in `requirements.txt`.  You'll need to have CUDA and CUDNN working as well.

Image resizing utilities require ImageMagick compiled with jpg support:

```bash
brew uninstall imagemagick && brew install imagemagick
```

The html viewer requires a WebGL-enabled browser.

## Quickstart

If you have a WebGL-enabled browser and a directory full of images to process, you can prepare the data for the viewer by installing the dependencies above then running:

```bash
git clone https://github.com/YaleDHLab/pix-plot && cd pix-plot
python utils/process_images.py "path/to/images/*.jpg"
```

To see the results of this process, you can start a web server by running:

```bash
# for python 3.x
python -m http.server 5000

# for python 2.x
python -m SimpleHTTPServer 5000
```

The visualization will then be available on port 5000.

## Processing Data with Docker

Some users may find it easiest to use the included Docker image to visualize a dataset.

To do so, you must first [install Docker](https://docs.docker.com/install/). If you are on Windows 7 or earlier, you may need to install [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/) instead.

Once Docker is installed, start a terminal, cd into the folder that contains this README file, and run:

```bash
# build the container
docker build --tag pixplot --file Dockerfile .

# process images
docker run -v $(pwd)/output:/pixplot/output pixplot \
  bash -c "cd pixplot && python3.6 utils/process_images.py images/*.jpg"

# run the web server
docker run -v $(pwd)/output:/pixplot/output \
  -p 5000:5000 pixplot bash -c "cd pixplot && python3.6 -m http.server 5000"
```

Once the web server starts, you should be able to see your results on `localhost:5000`.

## Curating Automatic Hotspots

By default, PixPlot uses [*k*-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) to find twenty hotspots in the visualization.  You can adjust the number of discovered hotspots by changing the `n_clusters` value in `utils/process_images.py` and re-running the script.

After processing, you can curate the discovered hotspots by editing the resulting `output/plot_data.json` file. (This file can be unwieldy in large datasets -- you may wish to disable syntax highlighting and automatic wordwrap in your text editor.) The hotspots will be listed at the very end of the JSON data, each containing a label (by default 'Cluster *N*') and the name of an image that represents the centroid of the discovered hotspot.

You can add, remove or re-order these, change the labels to make them more meaningful, and/or adjust the image that symbolizes each hotspot in the left-hand **Hotspots** menu.  *Hint: to get the name of an image that you feel better reflects the cluster, click on it in the visualization and it will appear suffixed to the URL.*


## Demonstrations

| Collection | # Images | Collection Info | Image Source |
| ---------- | -------- |  --------------- | ------------ |
| [Per Bagge](https://goo.gl/uk8oUx) | 29,782 | [Bio](https://goo.gl/2jQYGz) | [Lund University](https://goo.gl/zHpebT) |
| [Meserve-Kunhardt](https://goo.gl/sE3ZGy) | 27,000 | [Finding Aid](https://goo.gl/ESfcdB) | [Beinecke (Partial)](goo.gl/ESfcdB) | -->


## Acknowledgements

<p>I couldn't have done without the awesome code and materials published by the <a href="http://digitalhumanities.yale.edu/">Yale Digital Humanities Lab</a> See their <a href="https://github.com/YaleDHLab/pix-plot">original repo</a> for much more thorough background and acknowledgements in terms of the data science and techniques that underlie this visualization.
