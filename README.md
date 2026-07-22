# Image Colorizer – Deep Learning Web App

Automatically transform grayscale images into vibrant colorized versions using a deep learning model powered by **OpenCV DNN**. Upload an image, preview the original and colorized outputs, and download the final result—all through a simple web interface.

---

## Live Demo

https://huggingface.co/spaces/mrgen06/image-colorization-ml

---

## 📖 Overview

Image Colorizer is a web application that leverages a pre-trained deep neural network to colorize grayscale images. The application provides an intuitive interface for uploading images, previewing results, and downloading the colorized output.

The model is served through a Flask backend and deployed using Docker on Hugging Face Spaces, while large model weights are hosted separately using Hugging Face Datasets for efficient deployment.

---

## Features

- Upload grayscale images
- Automatic image colorization using Deep Learning
- Side-by-side before & after preview
- Download the generated colorized image
- Web-based interface built with Flask
- Dockerized for reproducible deployment
- Hosted on Hugging Face Spaces

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Backend | Flask |
| Computer Vision | OpenCV (DNN Module) |
| Deep Learning Model | Pre-trained Caffe Model |
| Frontend | HTML, CSS |
| Deployment | Docker, Hugging Face Spaces |
| Model Storage | Hugging Face Datasets |

---

## Project Architecture

```
User Upload
      │
      ▼
 Flask Backend
      │
      ▼
OpenCV DNN
(Pre-trained Caffe Model)
      │
      ▼
Colorized Image
      │
      ▼
 Preview & Download
