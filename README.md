# PixPlot

## PLACEHOLDER README

<p class="welcome">This page visualizes 7,384 <a href="https://dp.la/search?q=%22fourth%20of%20july%22%20OR%20%22independence%20day%22%20OR%20%22July%204th%22%20OR%20%22July%20Fourth%22&type=%22image%22&page=1">"Fourth of July"</a> (and related search) images from <a href="https://dp.la/">Digital Public Library of America</a> (DPLA), which aggregates cultural heritage metadata from thousands of institutions.</p>
<p class="welcome">Under the hood is a WebGL model of how the <a href='https://www.cs.unc.edu/~wliu/papers/GoogLeNet.pdf' target='_blank'>Inception</a> Convolutional Neural Network perceives "relatedness" and then a mapping of the computed relationships into 3-dimensional space using <a href='https://github.com/lmcinnes/umap' target='_blank'>UMAP</a> algorithm such that similar images appear near each other.</p>
<p class="welcome">Except for a few small modifications, this is based on the work and code published by the Yale Digital Humanities Labs in their <a href="https://github.com/yaledhlab/pix-plot">PixPlot repository</a>, which I learned about through an excellent <a href="https://vimeo.com/274922887">video presentation</a> from a Coalition for Networked Information (CNI) <a href="https://www.cni.org/topics/special-collections/neural-networks-machine-vision-for-the-visual-archive">project briefing</a>.</p>
--- 
<h3 class="welcome">Controls:</h3>
<p class="welcome">Click the clusters on the left to zoom to those areas, or use the mouse to navigate on your own.</p>
<p class="welcome">Clicking an item will center the camera to that image, and double-clicking an item will take you to the record for that image in DPLA.</p>

## Acknowledgements

<p>I couldn't have done this without the awesome code and materials published by the <a href="http://digitalhumanities.yale.edu/">Yale Digital Humanities Lab</a> See their <a href="https://github.com/YaleDHLab/pix-plot">original repo</a> for much more thorough background and acknowledgements in terms of the data science and techniques that underlie this visualization.
