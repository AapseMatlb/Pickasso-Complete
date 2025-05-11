#!/bin/bash
python3 scripts/vision_inference.py &
python3 scripts/ethical_decision.py &
echo 'Pickasso Simulation Fully Started.'
