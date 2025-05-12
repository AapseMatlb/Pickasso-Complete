# 🤖 Pickasso Unified Robotic System

## 📦 Project Overview
A fully autonomous trash-picking robot with integrated:
- 📸 Vision Inference (YOLO + MediaPipe)
- 📖 Ethical Decision-Making Engine
- 📡 Navigation (ROS)
- 🤖 Manipulation Simulation
- 🎛️ HMI Dashboard (React + Convex)
- 🗣️ Speech Interface (Recognition + TTS)

---

## 🚀 Deployment Steps

1. **Clone the Repository**
```bash
git clone https://github.com/YourRepo/pickasso_unified.git
cd pickasso_unified
```
2. **Install Dependencies**
 ```bash
  pip install -r requirements.txt
  cd hmi/frontend && npm install
  ```
3. **Start the Complete System**
  ```bash
  chmod +x startup/start_simulation.sh
  ./startup/start_simulation.sh
  ```

🧩 Subsystem Details
--------------------

  | Subsystem            | Access/Command          |
  |----------------------|-------------------------|
  | HMI Dashboard        | `http://localhost:3000` |
  | Vision Inference     | Runs Automatically      |
  | Decision Engine      | Runs Automatically      |
  | Navigation & Manipulation | Simulated using ROS   |
  | Speech Interface     | Accepts Simple Voice Commands |

---

📖 **For detailed configuration and subsystem usage, refer to the respective directories.**

---

👨‍💻 Developed by: _Yashashwani Kashyap_

## 📚 Supporting Repositories

- [Pickasso Trash Picking Simulation](https://github.com/AapseMatlb/Pickasso-Trash-Picking-Simulation)
- [Pickasso Speech](https://github.com/AapseMatlb/Pickasso-Speech)
- [Pickasso Navigation Stack](https://github.com/AapseMatlb/pickasso_navigation_stack)
- [Pickasso HMI](https://github.com/AapseMatlb/pickasso-hmi)
- [Pickasso Vision Ethics](https://github.com/AapseMatlb/pickasso-vision-ethics)
- [Pickasso Manipulation](https://github.com/AapseMatlb/pickasso-manipulation)
- [Pickasso Navigation Stack Simulation](https://github.com/AapseMatlb/Pickasso-Navigation-Stack-Simulation)
- [Pickasso Vision Inference](https://github.com/AapseMatlb/pickasso-vision-inference)

---

## 🛠️ Hardware Requirements (For Real Robot Deployment)

- Intel RealSense D435i Camera  
- OpenManipulator-X Arm  
- TurtleBot3 Waffle Pi Base  

---

## ⚙️ Environment Setup

- Python 3.8+  
- ROS Noetic (Navigation & Manipulation)  
- Node.js 16+ (HMI Dashboard)  
- Convex Backend Account  

---

## 📦 Pre-trained Models

Ensure YOLOv8 models are downloaded and placed under : vision_inference/models/

---

## 🌐 Convex Backend Configuration

Update `CONVEX_API_URL` in all relevant scripts with your deployed Convex backend URL.


## To Run HMI Frontend:
1. Navigate to frontend and run:
```
npm install
npm start
```
## To Run Convex Backend:
1. Navigate to convex directory and run:
```
npx convex dev
```
