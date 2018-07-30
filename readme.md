# LF-Net: Learning Local Features from Images

This repository is tensorflow implementation for Y. Ono, E. Trulls, P. Fua, K.M. Yi, "LF-Net: Learning Local Features from Images". If you use this code in your research, please cite the paper.

![comparison](/teasers/teasers.png)


## Installation

This code is based on Python3 and tensorflow with CUDA-9.0. For more details on the required libraries, see `requirements.txt`. You can also easily prepare this by doing

```
pip install -r requirements.txt
```

## Download models and dataset

We are not ready to provide models and dataset yet.
It will include both outdoor and indoor trained models and 1 sequence outdoor dataset as a toy training example.

If you want to test with other dataset (e.g. [MegaDepth](http://www.cs.cornell.edu/projects/megadepth/)).
you need to make sure your dataset contains the following stuffs.

1) RGB (or grayscale) images
1) Depth images
1) Camera poses (extrinsic matrix)
1) Camera intrinsic matrix

If your images are multi-view collections, you can generate others from SfM (i.e. [COLMAP](https://colmap.github.io/)).
But LF-Net doesn't require any data except grayscale images if you just want to run local feature extraction.

## Running the keypoint extraction demo

If you want to run whole images in a given directory, you just run the following script.

```
python run_lfnet.py --in_dir=images --out_dir=outputs
```

Otherwise, you can easily visualize 2-view matching demo in the provided ipython-notebook `notebooks/demo.ipynb` .

## Training

Once you finish deploying your dataset, you can train the model by doing

```
python train_lfnet.py
```

## Running Examples

| Outdoor dataset</br> Top: LF-Net, Btm: SIFT | Indoor dataset </br>Top: LF-Net, Btm: SIFT | Webcam dataset</br>Top: LF-Net, Btm: SIFT |
|:---------|:--------------------|:----------------|
| ![outdoor](/teasers/sfm_ours_sift.gif)     | ![indoor](/teasers/scannet_ours_sift.gif) | ![webcam](/teasers/webcam_ours_sift.gif) |


