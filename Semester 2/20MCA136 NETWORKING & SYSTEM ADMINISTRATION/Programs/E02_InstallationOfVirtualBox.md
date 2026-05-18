# 📘 README

<div align="center">

# 🖥️ E02_InstallationOfVirtualBox

### NSA Lab – Installation of VirtualBox

</div>

---

# 🎯 Aim

To study and install Oracle VirtualBox and create a virtual machine for operating system installation. 

---

# 📘 Introduction

VirtualBox is a powerful open-source virtualization software developed by Oracle. It allows multiple operating systems to run simultaneously on a single physical machine. 

Virtualization is useful for:

* software testing
* operating system installation
* networking practice
* cybersecurity labs
* server configuration
* cloud computing practice

VirtualBox supports:

* Windows
* Linux
* macOS
* Solaris
* FreeBSD

Both host operating systems and guest operating systems are supported. 

---

# 🖥️ What is Virtualization?

Virtualization is the process of creating virtual versions of computer resources such as:

* operating systems
* storage
* hardware
* servers
* networks

A virtual machine behaves like a real computer system.

---

# ⚙️ What is VirtualBox?

VirtualBox is virtualization software used to create and manage virtual machines. 

## 📌 Features of VirtualBox

* Open-source software
* Supports multiple operating systems
* Snapshot support
* Shared folders
* Clipboard sharing
* USB support
* Network configuration
* Remote display support

---

# 🧠 Host OS and Guest OS

## 🖥️ Host Operating System

The operating system installed on the physical computer.

### Examples

* Windows 11
* Ubuntu
* macOS

---

## 💻 Guest Operating System

The operating system installed inside the virtual machine.

### Examples

* Ubuntu in VirtualBox
* Windows Server in VirtualBox



---

# 🔧 CPU Virtualization Features

VirtualBox requires hardware virtualization support:

* Intel VT-x
* AMD-V

These settings must be enabled in BIOS/UEFI. 

## 📌 Importance

* Enables 64-bit virtual machines
* Improves VM performance
* Required for modern virtualization

---

# 🌐 Downloading VirtualBox

VirtualBox can be downloaded from the official Oracle website. 

## 📌 Steps

1. Open browser
2. Visit VirtualBox website
3. Download installer
4. Choose operating system version

---

# ⚙️ Installing VirtualBox

## 📌 Installation Steps

### 1️⃣ Run Installer

Launch the VirtualBox setup file. 

---

### 2️⃣ Select Installation Options

Choose:

* installation directory
* shortcuts
* components

Default settings are usually sufficient.

---

### 3️⃣ Confirm Network Interface Installation

Allow installation of VirtualBox network drivers. 

---

### 4️⃣ Start Installation

Click Install to begin installation.

---

### 5️⃣ Launch VirtualBox

After installation completes, launch VirtualBox. 

---

# 🖥️ Creating a Virtual Machine

A virtual machine is a software-based computer system. 

## 📌 Steps to Create VM

### 1️⃣ Open VirtualBox

Launch Oracle VM VirtualBox Manager.

---

### 2️⃣ Click "New"

Create a new virtual machine.

---

### 3️⃣ Configure VM Details

Set:

* VM Name
* Operating System Type
* Version

Example:

* Name: Windows Server 2019
* Type: Microsoft Windows
* Version: Windows 2016 (64-bit)



---

### 4️⃣ Allocate Memory

Assign RAM size.

Example:

* 8 GB RAM

---

### 5️⃣ Create Virtual Hard Disk

Select:

* Create virtual hard disk now

---

# 💽 Virtual Hard Disk

A virtual hard disk acts like a physical hard drive. 

## 📌 Types of Virtual Disk Formats

| Format | Description              |
| ------ | ------------------------ |
| VDI    | VirtualBox native format |
| VHD    | Hyper-V format           |
| VMDK   | VMware format            |
| QCOW   | QEMU format              |

---

# 💾 Storage Allocation Types

## 🔹 Dynamically Allocated

* Uses space only when needed
* Saves physical storage
* Expands automatically

---

## 🔹 Fixed Size

* Allocates full size immediately
* Better performance
* Uses more disk space



---

# ⚙️ Virtual Machine Settings

VirtualBox provides several configuration sections. 

---

# 🧩 General Settings

Used for:

* VM name
* clipboard sharing
* drag and drop
* encryption

---

# 🧠 System Settings

Configure:

* processors
* boot order
* chipset
* acceleration

---

# 🖥️ Display Settings

Configure:

* video memory
* monitor count
* screen scaling
* 2D/3D acceleration

---

# 💽 Storage Settings

Used to:

* add virtual disks
* mount ISO files
* configure controllers

Example:

* Mount Windows ISO file

---

# 🔊 Audio Settings

Configure:

* audio driver
* audio controller

---

# 🌐 Network Settings

Virtual network adapters can be configured. 

## 📌 Network Modes

### 🔹 NAT

VM accesses internet through host machine.

### 🔹 Bridged Adapter

VM appears as separate machine in network.

### 🔹 Host-only Adapter

Communication only between host and VM.

### 🔹 Internal Network

Communication only among VMs.

---

# 🔌 USB Settings

Used for:

* pendrives
* USB devices
* printers

---

# 📁 Shared Folders

Shared folders allow file transfer between:

* host OS
* guest OS

---

# ▶️ Starting Virtual Machine

VirtualBox provides different startup modes. 

## 📌 Normal Start

Opens VM window normally.

---

## 📌 Headless Start

Runs VM in background without GUI.

---

## 📌 Detachable Start

VM continues running after closing window.

---

# 💿 Installing Guest Operating System

The operating system is installed using ISO image files. 

## 📌 Steps

1. Start VM
2. Boot from ISO image
3. Follow installation wizard
4. Create partitions
5. Install OS
6. Restart VM

---

# 🧩 VirtualBox Guest Additions

Guest Additions improve VM performance and integration. 

## 📌 Features

* Better graphics
* Shared clipboard
* Drag and drop
* Shared folders
* Mouse integration
* Time synchronization

---

# ⚙️ Advantages of VirtualBox

* Free and open-source
* Easy virtualization
* Supports multiple OS
* Safe testing environment
* Useful for networking labs
* Snapshot support

---

# ❌ Limitations

* Requires high RAM and CPU
* Performance lower than physical machine
* Large storage requirement

---

# 📚 Viva Questions

## 1️⃣ What is virtualization?

Virtualization is creating virtual versions of computing resources.

---

## 2️⃣ What is VirtualBox?

VirtualBox is virtualization software used to create virtual machines.

---

## 3️⃣ What is a virtual machine?

A virtual machine is a software-based computer system.

---

## 4️⃣ Difference between host OS and guest OS?

Host OS runs on physical machine while guest OS runs inside VM.

---

## 5️⃣ What is ISO file?

ISO is a disk image file used for OS installation.

---

## 6️⃣ What is NAT mode?

NAT allows VM internet access through host machine.

---

## 7️⃣ What are Guest Additions?

Guest Additions improve VM integration and performance.

---

## 8️⃣ What is dynamically allocated storage?

Disk space increases only when needed.

---

## 9️⃣ What is bridged networking?

VM behaves like separate computer in the network.

---

## 🔟 Why is virtualization important?

It helps in testing, networking, cloud computing, and system administration.

---

# 🎓 Result

Thus, Oracle VirtualBox was studied, installed successfully, and a virtual machine was created for operating system installation.
