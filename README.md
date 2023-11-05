# 🍰 Bakllava Llama C++ Tutorial 🦙

Welcome to the delicious world of Bakllava Llama with C++! Follow these steps to get your code running and indulge in AI sweetness! 😋

🚨 Properly tested only with Apple silicon chip

## 🚀 Step 1: Install Llama C++

First things first, let's get the Llama C++ installed.

🔗 Clone the repository from GitHub:
```jsx
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```
### On Linux & macOS:
🛠 Build with make:
```
make
```
🏗 Or, if you prefer cmake:
```
cmake --build . --config Release
```

## 📦 Step 2: Download the Model!
1. 📥 Download from Hugging Face - [mys/ggml_bakllava-1](https://huggingface.co/mys/ggml_bakllava-1/tree/main) this 2 files:
* 🌟 ggml-model-q4_k.gguf (or any other quantized model) - only one is required!
* 🧊 mmproj-model-f16.gguf

2. ✂️ Copy the paths of those 2 files.
3. 🏃‍♂️ Run this in the llama.cpp repository (replace YOUR_PATH with the paths to the files you downloaded):

    #### macOS
    ```
    ./server -m YOUR_PATH/ggml-model-q4_k.gguf --mmproj YOUR_PATH/mmproj-model-f16.gguf -ngl 1
    ```
    #### Windows
    ```
    server.exe -m REPLACE_WITH_YOUR_PATH\ggml-model-q4_k.gguf --mmproj REPLACE_WITH_YOUR_PATH\mmproj-model-f16.gguf -ngl 1

    ```
4. 🎉 The llama server is now up and running!
    
    ⚠️ NOTE: Keep the server running in the background.
5. 📹 Let's run the script to use the webcam or send it a single picture!

## 🏃‍♀️ Step 3: Running the Demo
Open a new terminal window and clone the demo app:
```
git clone https://github.com/Fuzzy-Search/realtime-bakllava.git
cd realtime-bakllava
```
### 🛠 (Optional) Create a new Python virtual environment and activate it
```
python3 -m venv bakllava-venv
source bakllava-venv/bin/activate
pip3 install -r requirements.txt
```
### 🎥 Webcam Script
To start streaming from your webcam:

! if you have problem with FFMPEG lib, download the source code and in file src/video_stream.py modify second line of code

```
python3 src/video_stream.py
```

### 🖼 Simple Picture Drop
```
pip install -r picture_requirements.txt
python src/picture_drop.py --path src/sample_pic.png
```


## 📝 Enjoy your adventure with Llama C++! 🚀🦙

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Fuzzy-Search/realtime-bakllava&type=Date)](https://star-history.com/#Fuzzy-Search/realtime-bakllava&Date)
