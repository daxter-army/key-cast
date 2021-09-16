<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" integrity="sha512-1ycn6IcaQQ40/MKBW2W4Rhis/DbILU74C1vSrLJxCq57o941Ym01SwNsOMqvEBFlcgUa6xLiPY/NS5R+E6ztJQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />

[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

<br/>

<p align="center">
  <a href="https://github.com/daxter-army/key-cast/">
    <img src="https://github.com/daxter-army/key-cast/blob/main/assets/icons/logo/keycast_logo_png.png" alt="Logo" width="50">
  </a>

  <h3 align="center">Key Cast</h3>

  <p align="center">
    Screen cast your keyboard and mouse clicks in style
    <br />
    <a href="https://daxter-army.github.io/key-cast/"><strong>Project Homepage »</strong></a>
    <br />
    <br />
    <a href="https://daxter-army.github.io/key-cast/">View Demo</a>
    ·
    <a href="https://daxter-army.github.io/key-cast/issues">Report Bug</a>
    ·
    <a href="https://daxter-army.github.io/key-cast/issues">Request Feature</a>
  </p>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started (Use only)</a>
      <a href="#getting-started">Getting Started (Development)</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#installation">Building</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

In this internet age, everyone is learning to stay ahead in their career or to develop something new, creative and fun. Digging the internet for quality tutorials, watching that youtube videos of blender, illustrator, photoshop, webdev and what not. To give back to your community, you also thought of creating some tutorials, but guess what, you are not having any good keyboard and mouse indicators, and that ones which are available in the market, do not suits your personality.
<br/>
Here comes **Keycast**, which enables you to, screen cast your keyboard and mouse clicks, while also being pleasant to your eyes and why you should consider Keycast, here's why:

**Cross-platform:** Run it anywhere. Run it on Linux, Windows or OS X.
<br/>

**Keybaord & mouse clicks:** From keyboard presses to mouse clicks, we've covered you all!.
<br/>

**[IN PROGRESS!] Show in style:** Choose from numerous themes, or create your own.
<br/>

**[IN PROGRESS!] Transparency control:** Adjust the transparency level of the panel as per your convenience.<br/>

### Built With

This was achieved with **Python** (cPython), with **Pynput** as global keyboard and mouse event listener, **Tkinter** powering the GUI, & **Pyinstaller** for creating distributable package files.
* [Python](https://getbootstrap.com)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Pynput](https://pypi.org/project/pynput/)
* [Pyinstaller](https://pyinstaller.readthedocs.io/en/stable/)

<!-- GETTING STARTED -->
## Getting Started (Use only)
* Go to application [Homepage](https://daxter-army.github.io/key-cast), and download the package as per your OS.

## Getting Started (Development)

This section will help you to get started with the project, locally

## Prerequistes
* You should be having Python version > 3.6.x
* Install the requirements from **REQUIREMENTS.txt** file via **pip** before actually running the application, with
```python
    pip3 install -r REQUIREMENTS.txt
```

### Installation

* Clone the project locally with
```sh
    git clone git@github.com:daxter-army/key-cast.git
```

* navigate to the project dir and activate virtual env
* *for windows*
```sh
    .\keycast_env\bin\activate
```
* *for linux/OS X*
```sh
    source .\keycast_env\bin\activate
```

* Now you'll see that virtual env has been activated, after this hit
```sh
    python3 keycast_dev.py
```
* You have done it, you will be seeing a window running on your screen, if everything goes well.

### Building
To create one distributable file on linux/OS X, type
```sh
    pyinstaller keycast_onefile.py --onefile --add-data "assets:assets"
```

With hidden console window, in Windows, type
```sh
    pyinstaller keycast_onefile.py --onefile --add-data "assets:assets" --windowed
```

With console window in the background, in Windows, remove **--windowed** argument


<!-- USAGE EXAMPLES -->
## Usage
Screenshots and Demos coming soon!

<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request -->

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
Mehul Singh Teya - mehulsinghteya@gmail.com
<br/>
Project Link: [https://github.com/daxter-army/key-cast](https://github.com/daxter-army/key-cast)
<br/>
Project Homepage : [https://daxter-army.github.io/key-cast](https://daxter-army.github.io/key-cast)

## Acknowledgement
* [Fontawesome](https://fontawesome.com)
* [Python](https://getbootstrap.com)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Pynput](https://pypi.org/project/pynput/)
* [Pyinstaller](https://pyinstaller.readthedocs.io/en/stable/)

## Note
Right now it is heavily under development, and is being developed in linux (ubuntu), can break if you try, because i am working on it to make compatible with all kind of keyboards (because sometimes key codes differ for same key combinations on different OS/PC)

## Issues
Visit Issues tab
<br/>
<a href="https://github.com/daxter-army/key-cast/issues/1">Issues</a>