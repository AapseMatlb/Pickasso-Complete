#!/bin/bash

echo "🚀 Starting Pickasso Complete System..."

# Start ROS Core
gnome-terminal -- bash -c "roscore; exec bash"

sleep 5

# Start Navigation
gnome-terminal -- bash -c "roslaunch navigation/launch/navigation.launch; exec bash"

# Start Manipulation
gnome-terminal -- bash -c "roslaunch manipulation/launch/manipulation.launch; exec bash"

# Start HMI
gnome-terminal -- bash -c "cd hmi/frontend && npm start; exec bash"

# Start Convex Backend
gnome-terminal -- bash -c "cd hmi/backend && npx convex dev; exec bash"

# Start Vision Inference
gnome-terminal -- bash -c "python3 vision_inference/scripts/vision_inference.py; exec bash"

# Start Decision Engine
gnome-terminal -- bash -c "python3 decision/decision_engine.py; exec bash"

# Start Speech Interface
gnome-terminal -- bash -c "python3 speech/speech_interface.py; exec bash"

echo "✅ Pickasso System Fully Started!"
