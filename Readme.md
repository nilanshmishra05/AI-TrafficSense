🚦 AI-TrafficSense

Reimagining urban traffic with the power of AI.
AI-TrafficSense is an AI-powered traffic monitoring system that uses real-time computer vision to count vehicles and dynamically manage traffic signals. Say goodbye to static traffic lights and hello to smarter, adaptive city streets.

🌟 Why AI-TrafficSense?

Traditional traffic systems are static, inefficient, and blind to real-time road conditions. AI-TrafficSense aims to flip the script by using a YOLOv8-based vehicle detection system to:
🧠 Think in real-time – Count vehicles using live camera feeds.
🕒 Adapt intelligently – Dynamically adjust signal timings based on actual road congestion.
📊 Log smartly – Record traffic data to help improve future planning and analysis.

🧰 What’s Inside?

Here’s a quick breakdown of what makes AI-TrafficSense tick:
Component	Description
vehicle_counter.py	Detects and counts vehicles using YOLOv8
ui_vehicle_counter.py	Simple interface to view traffic insights
backend_server.py	Manages data flow and model inference
model_train.py	Train your own detection model if needed
traffic_data.csv	Dataset for training and analysis
vehicle_counts_log.csv	Real-time logs of detected vehicle counts
yolov8n.pt	Pre-trained YOLOv8 model for detection


🚀 Getting Started

1.Clone the repo:

git clone https://github.com/hacktopus-primes18/AI-TrafficSense.git
cd AI-TrafficSense

2.Install the dependencies:

pip install -r requirements.txt


3.Download YOLOv8 Model: Place yolov8n.pt in the root directory. You can grab it from Ultralytics YOLOv8 Releases.

4.Run the app:

python run.py

Optional: Want to train your own model?

python model_train.py


🧪 How It Works

Camera feed →
YOLOv8 detects vehicles →
Vehicle counts recorded in CSV →
Traffic signal decisions optimized in real-time
You can visualize the whole process through the UI and watch your traffic control system get smarter over time.


📈 Use Cases

🚙 Urban traffic optimization
🛣️ Smart city infrastructure
🧪 Research & data analysis on traffic patterns
🧵 Integration into larger IoT systems

🤝 Contributing

Got ideas? Found bugs? Want to improve the detection model or UI?
Fork this repo
Create a feature branch (git checkout -b feature/cool-idea)
Push your changes and open a PR
Let’s build smarter cities together 🏙️

📄 License
MIT License – free to use, modify, and distribute. See LICENSE for full details.

📬 Contact
Created by Hacktopus Primes. Feel free to reach out via issues or discussions!
