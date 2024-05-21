# Hub

## 📌 Table of Contents :

I. [Presentation](#📋-presentation)

II. [Equipment required](#⚙️-system-architecture)

III. [3D models](#💻-installation) 

IV. [Schématic](#💻-installation) 

V. [Installation and Assembly](#💻-installation) 

## 📋 Presentation :
The hub using the MQTT protocol enables the connection and control of various smart devices, such as a connected fan, via a dedicated mobile app. With its protocol, the hub ensures fast and reliable communication between devices and the app, allowing real-time commands.

## ⚙️ Equipment required :

- [Raspberry Pi](https://lc.cx/UVVqhr)
- [Ethernet cable](https://lc.cx/8I6v4b)
- [USB to micro USB cable](https://lc.cx/cJiMD6)
- [AC USB adapter](https://lc.cx/akJVcI)


## 🔰 3D models :
You can view the current model here : https://a360.co/48swrxa

The entire object can be printed in 3d from the files present in this folder :

[3D Models](/Hub/3D_Models/)

## 💡 Schématic :

## 💻 Installation :

### Prerequisites :

To begin, follow this guide to install your OS in the Raspberry Pi :
[Getting Started](https://www.raspberrypi.com/documentation/computers/getting-started.html)

- Use the Raspberry os lite 64-bits version.
- To connect the Raspberry to internet, use the Ethernet câble.

After that, follow the instruction below :

```bash
sudo apt update -y && sudo apt upgrade -y
sudo apt install git -y 
```

Please follow the Docker docs to install docker on the RPI : [Doc](https://docs.docker.com/engine/install/debian/)

Don't forget to add your user to the docker's group :
```bash
sudo usermod -aG docker $(whoami)
sudo systemctl enable --now docker.socket
```

### Install the hub :

Clone this repo : [https://github.com/Wanaps/DomoLabo](https://github.com/Wanaps/DomoLabo)

```bash
git clone https://github.com/Wanaps/DomoLabo
cd DomoLabo/Hub
docker compose up -d
```


5. Enjoy !😉