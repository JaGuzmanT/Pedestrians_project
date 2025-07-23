# Real-Time Pedestrian Counting with YOLO11 🚶‍♂️🚦

<div align="center">

![](Images/Home.png)

<img alt="Python" src="https://img.shields.io/badge/Python-3.8+-blue.svg">
<img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-2.8+-orange.svg">
<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg">

</div>

## Research Team 🧑‍🔬
- *Dr. José Alberto Guzmán Torres*  
jose.alberto.guzman@umich.mx  
*Universidad Michoacana de San Nicolás de Hidalgo, Faculty of Civil Engineering*  
*AULA-CIMNE, Morelia, Michoacán, México*  

---

## 🎯 Project Objective

This project implements a **real-time pedestrian detection and counting system** using the YOLO11 object detection algorithm. The main goal is to monitor and quantify pedestrian flow in urban areas by placing a virtual counting line on video footage. This tool is designed to assist in urban planning, pedestrian safety studies, and smart city applications.

---

## 🔄 Workflow Overview

1. 📹 **Video Input**  
   The script loads a video file of an urban area where pedestrian flow is to be analyzed.

2. 🖱️ **Virtual Counter Line Selection**  
   - A custom HTML tool (`Selector_puntos.html`) is provided to interactively select two points on a video frame, defining the position of the virtual counting line.
   - The selected coordinates are used in the main script to set up the counting region.

3. 🤖 **YOLO11 Model Initialization**  
   - The script loads a YOLO11 model pre-trained for pedestrian detection.
   - The model is configured to detect only the class corresponding to persons.

4. 🎯 **Real-Time Detection and Counting**  
   - For each frame in the video:
     - The YOLO11 model detects pedestrians.
     - The script checks if detected pedestrians cross the virtual counting line.
     - The count is updated in real time and can be displayed on the output video.

5. 📼 **Output Generation**  
   - The processed video, with bounding boxes, the virtual line, and the pedestrian count overlay, is saved to disk.
   - Optionally, the output can be displayed in real time.

---

## 🌟 Key Features

- **Interactive Line Selection:**  
  Use the included HTML tool to easily define the counting line on any video.

- **Accurate Pedestrian Detection:**  
  Utilizes YOLO11 for robust and efficient detection in urban environments.

- **Real-Time Counting:**  
  Counts pedestrians as they cross the virtual line, providing immediate feedback.

- **Customizable Output:**  
  Save the processed video with overlays for further analysis or reporting.

---

## 🏗️ Project Architecture
```
📦 Real_Time_Pedestrian_Counting/
├── Models/
│   ├── yolo11l.pt                # YOLO11 model weights for pedestrian detection
│   ├── yolo11m.pt               
│   ├── yolo11s.pt
│   ├── yolo11x.pt
│   └── yolo12l.pt
├── Resources/
│   ├── videos/                   # Input videos for analysis
│   │   ├── Cruce_Estacionamiento_CU_2.mp4
│   │   └── ...
│   └── videos_output/           # Processed videos with detection overlays
│       ├── Cruce_Estacionamiento_CU_2.mp4
│       └── ...
├── Images/
│   ├── background_minimalista.svg # Background for UI
│   ├── logo_siiia_w.png          # Institutional logos
│   └── ...
├── Real_time_object_counting.ipynb   # Main Jupyter notebook script
├── Real_time_object_counting.py      # Python version of the script
├── Selector_puntos.html              # Interactive line selection tool
└── README.md                         # This documentation file
```

---

## 🚀 How to Use

1. **Select the Counting Line:**  
   Open `Selector_puntos.html` in your browser and select the two points for the virtual line. Save the coordinates.

2. **Configure the Script:**  
   - Set the video path and model path in the script.
   - Input the selected region points for the counting line.

3. **Run the Script:**  
   Execute the script in your Python environment. The script will process the video, detect pedestrians, and count them as they cross the line.

4. **Review the Output:**  
   The output video will be saved in the specified folder, showing detections, the counting line, and the running count.

---

## 📚 Citation

If you use this tool or dataset in your research, please cite:

> Guzmán Torres, J.A., Universidad Michoacana de San Nicolás de Hidalgo, Faculty of Civil Engineering, AULA-CIMNE, Morelia, Michoacán, México.

---

## 🙏 Acknowledgements

This project was developed as part of research on urban mobility and smart city solutions. Special thanks to the open-source community and contributors to the YOLO and Ultralytics projects.

---

![](Home.png)

<img alt="Python" src="https://img.shields.io/badge/Python-3.8+-blue.svg">
<img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-1.20+-brightgreen.svg">
<img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-2.8+-orange.svg">
<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg">



## 💻 Technical Specifications  

### Prediction Model  
- **Framework**: TensorFlow 2.8+ / Keras  
- **Model File**: `carbonation_classifier_model.h5` (CNN architecture trained on labeled concrete images)  
- **Input Preprocessing**:  
  1. Images resized to 224×224 px  
  2. Pixel centering using `[123.68, 116.779, 103.939]` mean subtraction  
- **Inference Logic**:  
  - Probability ≤ 0.22 → “No carbonation detected”  
  - Probability > 0.22 → “Carbonation damage detected”

### User Interface  
- **Framework**: Streamlit 1.20+  
- **Animations**: Lottie via `streamlit_lottie`  
- **Styling**: Custom sidebar backgrounds and logos embedded with Markdown/HTML  
- **Security**: Simple password protection (default code: `concrete2025`) on sidebar  

---

## ⚙️ Installation & Setup  

### System Requirements  
| Component | Minimum     | Recommended  |
|-----------|-------------|--------------|
| **Python**| 3.8+        | 3.10+        |
| **RAM**   | 4 GB        | 8 GB+        |
| **OS**    | Windows/Linux/macOS | —   |

### Clone & Install  
```bash
# 1. Clone the repo
git clone https://github.com/JoseAlbertoGT/Concrete_Carb_Classifier.git
cd Concrete_Carb_Classifier

# 2. (Optional) Use Dev Container
#    Open in VS Code and click “Reopen in Container”

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run Central_app.py
```
## :abacus: Methodology & Algorithms

### :books: Machine Learning Pipeline

1. **Data Collection**: High-resolution photographs of concrete specimens with known carbonation states.
2. **Image Preprocessing**: Resize, center‐crop, and pixel-value normalization based on ImageNet means.
3. **Model Training**: Fine-tuned CNN in Keras with binary cross-entropy loss.
4. **Deployment**: Model weights loaded at runtime in a Streamlit interface for inference.
5. **Explainability**: Confidence thresholds and clear color–coded messaging to assist non-expert users.

### :trophy: Why Concrete Carbonation Classifier?

| Feature         | Traditional Methods    | ConcreteCarbClass API    |
|-----------------|-----------------------|---------------------------|
| **Speed**       | Visual inspection     | Instant verdict           |
| **Accuracy**    | Subjective            | Objective                 |
| **Explainability** | Limited            | Transparent, interactive  |
| **Accessibility** | Specialist required | Anyone, anywhere          |
| **Scalability** | Static                | Easily updatable          |
---
## :scientist: Research Team

### :man_scientist: Principal Researchers

<table>
<tr>
<td width="33%">

**Dr. José Alberto Guzmán Torres** :mexico:
- :office: [SIIIA MATH: Soluciones en ingeniería](http://www.siiia.com.mx)
- :classical_building: [Universidad Michoacana de San Nicolás de Hidalgo](http://www.umich.mx)
- :microscope: Engineering applications & Artificial Intelligence
- :email: jose.alberto.guzman@umich.mx
- :globe_with_meridians: [ORCID](https://orcid.org/0000-0002-9309-9390)

</td>
<td width="33%">

**Dr. Francisco Javier Domínguez Mota** :mexico:
- :office: [SIIIA MATH: Soluciones en ingeniería](http://www.siiia.com.mx)
- :classical_building: [Universidad Michoacana de San Nicolás de Hidalgo](http://www.umich.mx)
- :microscope: Applied Mathematics & Finite Difference Methods
- :email: francisco.mota@umich.mx
- :globe_with_meridians: [ORCID](https://orcid.org/0000-0001-6837-172X)

</td>
<td width="33%">

**Dr. Gerardo Tinoco Guerrero** :mexico:
- :office: [SIIIA MATH: Soluciones en ingeniería](http://www.siiia.com.mx)
- :classical_building: [Universidad Michoacana de San Nicolás de Hidalgo](http://www.umich.mx)
- :microscope: Numerical Methods & Computational Mathematics
- :email: gerardo.tinoco@umich.mx
- :globe_with_meridians: [ORCID](https://orcid.org/0000-0003-3119-770X)

</td>
</tr>
</table>
---

## :books: Scientific References

### :books: Core Publications

1. **Guzmán-Torres, J. A.**, Domínguez-Mota, F. J., Tinoco-Guerrero, G., Tinoco-Ruíz, J. G., & Alonso-Guzmán, E. M. (2024). *Extreme fine-tuning and explainable AI model for non-destructive prediction of concrete compressive strength, the case of ConcreteXAI dataset.* **Advances in Engineering Software**, 192, 103630. [DOI: 10.1016/j.advengsoft.2024.103630](https://doi.org/10.1016/j.advengsoft.2024.103630)

2. Guzmán-Torres, J. A., Domínguez-Mota, F. J., Alonso-Guzmán, E. M., Tinoco-Guerrero, G., & Martínez-Molina, W. (2024). ConcreteXAI: A multivariate dataset for concrete strength prediction via deep-learning-based methods. Data in Brief, 53, 110218. [DOI: 10.1016/j.dib.2024.110218](https://doi.org/10.1016/j.dib.2024.110218)

---

## :bookmark_tabs: License

MIT License

Copyright (c) 2025 José A. Guzmán-Torres

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---
## :email: Contact & Support

### :busts_in_silhouette: Research Group Contact

**Primary Contact:**
- **Dr. José Alberto Guzmán Torres**
  - :email: jose.alberto.guzman@umich.mx
- :office: Research Group: SIIIA MATH – Soluciones en Ingeniería
- :classical_building: Institution: Facultad de Ingeniería Civil, UMSNH
- :technologist: Technical Issues: Report bugs or request features via GitHub Issues

### :question: Technical Support

For technical questions and issues:
1. **Email Support**: Contact the research team directly for complex technical inquiries
2. **Academic Collaboration**: Reach out for research partnerships and joint projects

### :mortar_board: Student Inquiries

Interested in graduate research opportunities?
- **Contact**: Dr. José Alberto Guzmán Torres (jose.alberto.guzman@umich.mx)
- **Topics**: Machine Learning, Deep Learning, Computer vision applications
- **Institution**: Universidad Michoacana de San Nicolás de Hidalgo

### :globe_with_meridians: Institutional Affiliations

- **SIIIA MATH**: [Soluciones en ingeniería](http://www.siiia.com.mx)
- **UMSNH**: [Universidad Michoacana de San Nicolás de Hidalgo](http://www.umich.mx)

---

<div align="center">

⭐ If this tool enhances your research or teaching, please ⭐ this repository!
</div>



