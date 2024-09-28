# Interactive-Whiteboard-Pro-IR-and-Image-processing-
Revolutionizing Whiteboards: Geometrical Transformation and IR Pen Control for Dynamic Interaction on Any Surface with Computer Vision

**Digital Board Pro** is an innovative interactive whiteboard system that enables users to interact with projected content on flat surfaces using an infrared (IR) pen. The system is designed to be used on surfaces such as walls, whiteboards, and tables. It leverages a webcam (with the IR filter removed) and a projector to detect and track the movements of the IR pen, allowing seamless interaction with the projected screen.

## Features

- **Interactive Surface**: Turn any flat surface into an interactive whiteboard using an IR pen.
- **Real-time Tracking**: Accurately track and detect the movements of the IR pen using a modified webcam.
- **Simple Setup**: Utilize a webcam and projector for easy setup and calibration.
- **Versatile Use**: Ideal for interactive presentations, educational tools, and collaborative spaces.

## Project Demonstration

Check out a live demonstration of the Digital Board Pro in action on YouTube:
<div style="text-align: center;">
<a href="https://youtu.be/FpK8PYU6Rsc?si=9AVkPFdNyOAiSQc4">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/YouTube_icon_%282013-2017%29.png/480px-YouTube_icon_%282013-2017%29.png" alt="Project Demonstration" width="50" height="30">
</a>
</div>
> Click the image above to watch the video.

## Project Components

- **IR Pen**: Emits infrared light that is detected by the webcam.
- **Webcam**: Modified by removing the IR filter to capture infrared light from the IR pen.
- **Projector**: Displays the computer screen's content on the surface.
- **Software Framework**: Controls the detection, calibration, and interaction logic between the webcam, pen, and projected content.

## Installation

To set up the system on your machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DigitalBoardPro.git
   ```

2. Navigate to the project directory:
   ```bash
   cd DigitalBoardPro
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Calibrate the webcam and projector settings:
   - Follow the instructions in the calibration guide (`docs/calibration_guide.md`) to set up your webcam and projector for optimal performance.

## Usage

1. Connect your IR pen, webcam, and projector.
2. Run the system software:
   ```bash
   python main.py
   ```
3. Calibrate the system based on the on-screen instructions.
4. Start interacting with the surface using the IR pen.

## Project Images

Here are some images demonstrating the Digital Board Pro setup:

### IR Pen in Action
(![Screenshot (17)](https://github.com/user-attachments/assets/643ecd83-eb5e-434a-aef4-b43d8f0e4b35)
)
### IR Pen in Action
(https://github.com/user-attachments/assets/7d273ba3-347e-45f8-8311-1e09d52a39a0)

*The IR pen being used on a flat surface*



## Calibration

Calibration is critical for ensuring accurate mapping of the IR pen's position to the computer cursor. Please refer to the calibration guide for detailed steps on geometric transformation and projector settings.

## How It Works

The system works in three main stages:
1. **Capture & Detection**: The webcam detects the IR light emitted by the IR pen.
2. **Calibration**: The webcam and projector are calibrated based on geometric transformation principles.
3. **Mapping**: The detected IR pen position is mapped to the computer cursor, allowing users to control the projected content through pen movements.

## Future Work

Digital Board Pro has the potential for several future enhancements:
- Gesture recognition for advanced interaction without the pen.
- Modern state of the Art GUI.(with multiple features)

## Contributions

We welcome contributions! Please submit any pull requests or open an issue for any bugs or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
