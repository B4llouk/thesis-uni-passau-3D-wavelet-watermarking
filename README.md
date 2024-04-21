# 3D WATERMARKING THROUGH DISCRETE TRANSFORMS
This repo contains the source code developed as part of the thesis work for Mohamed Bellakhal (CS MASTER STUDENT AT UNI PASSAU) 

## contact the author: 
bellak01@ads.uni-passau.de 
bellakhalmohamed79@gmail.com
+491783045692

## data: 
This directory contains the data used/generated during the thesis. Such as 3D automotive models in npy directory. 3D plots for experimentation and an example of the generated QR Code. 

## notebooks 
This directory contains the implementation of our thesis work as python scripts and Jupyter notebooks. In this directory we note: 

### helpers 
This module was implemented to avoid repeating code while developing the several notebooks. It contains basic functions that we developed  to handle wavelet operations, metrics, plots, qr code generation and watermarking. 

### notebooks labeled as draft/intro 
These notebooks are for experimentation and do not contain end results. 

### notebooks containing pywt /DCT 
These Jupyter notebooks contain the result of our work and are applying 3D watermarking using Discrete Transforms while varying the circumstances (the type of the transform, the intensity of the watermark, the vanshing moment etc..) 

### block implementation 
Block implementation notebook contains the implementation of the 3D watermarking on an array of 3D images using an array of wavelet transforms. In this notebook we try to watermark & evaluate the results of all circumstances(all possible discrete transfrms and their variations) in parallel using python lists and dictionaries. 

