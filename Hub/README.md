# Hub

## 📌 Table of Contents :

I. [Presentation](#📋-i---presentation)

II. [Equipment required](#⚙️-ii---equipment-required)

III. [3D models](#🔰-iii---3d-models) 

IV. [Schematics](#💡-iv--schematics) 

V. [Installation](#💻-v---installation) 

## 📋 I - Presentation :
The hub using the MQTT protocol enables the connection and control of various smart devices, such as a connected fan, via a dedicated mobile app. With its protocol, the hub ensures fast and reliable communication between devices and the app, allowing real-time commands.

## ⚙️ II - Equipment required :

- [Raspberry Pi](https://lc.cx/UVVqhr)
- [Ethernet cable](https://lc.cx/8I6v4b)
- [USB to micro USB cable](https://lc.cx/cJiMD6)
- [AC USB adapter](https://lc.cx/akJVcI)


## 🔰 III - 3D models :
You can view the current model of the hub here : https://a360.co/48swrxa

The entire object can be printed from the files present in the [3D Models](/Hub/3D_Models/) folder in the repo.

## 💡 IV - Schematics :

You can find the electrical schematics in the [schematics folder](/Hub/SCH/)

## 💻 V - Installation :

### Prerequisites :

To begin, follow [this guide](https://www.raspberrypi.com/documentation/computers/getting-started.html) to install your OS in the Raspberry Pi.

- Use the Raspberry OS Lite 64-bits version.
- To connect the Raspberry to internet, use the Ethernet cable.

After that, follow the instructions below :

```bash
sudo apt update -y && sudo apt upgrade -y
sudo apt install git -y 
```

Please follow the Docker docs to [install docker on the RPI](https://docs.docker.com/engine/install/debian/).

⚠️ Don't forget to add your user to the docker group :
```bash
sudo usermod -aG docker $(whoami)
sudo systemctl enable --now docker.socket
```

### Install the hub :

Clone the [DomoLabo repo](https://github.com/Wanaps/DomoLabo) into the RPI.

```bash
git clone https://github.com/Wanaps/DomoLabo
cd DomoLabo/Hub
docker compose up -d
```

Enjoy your own HUB at home! 😉