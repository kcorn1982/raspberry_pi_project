# Setting up ssh

## Pre-requisites

The following steps take into account that:

- you are using a Linux or Mac - I'll look into windows instructions at a later date
- you have installed a desktop server such as Raspios (bullseye verions at the time of writing this guide) on a Raspberry Pi
- Have gone through the basic setup and have connected to the internet through WiFi or Ethernet

## Index

- [Why SSH?](#why-ssh)
  - [Setting up ssh](#setting-up-ssh)
  - [Turning SSH on](#turning-ssh-on)
    - [Using the GUI config](#using-the-gui-config)
    - [Setting up SSH from the command line](#setting-up-ssh-from-the-command-line)

## Why SSH?

SSH allows you to log into your raspberry pi without having to input a password everytime. Most importantly it's a muh more secure practice especially if you turn off SSH password authentiation, which I would advise doing especially if you're intending to expose your Pi to the internet.

## Turning SSH on

Ideally you want to be accessing your Pi remotely so setting SSH up is a necessity.

### Using the GUI config

This is easiest way is to set up SSH from the Raspi GUI:

![Pi Menu Config](/img/pi_menu_config.png)

Then select Interfaces and at this point you may as well turn on both SSH and VNC, we will cover VNC in a later section.

![Gui Config Interfaces](/img/ssh_gui_conf.png)

### Setting up SSH from the command line

1. Using raspi-config

Similar to using the raspi GUI there is a useful command line config that follows a similar pattern:

simply typing `sudo raspi-config` into the command line will bring up the following menu and simply follow the steps in the images:

![Raspi Config Interfaces](/img/raspi_config_interface.png)
![Raspi Config SSH](/img/raspi_config_ssh.png)
![Raspi Config Enable](/img/raspi_config_enable_ssh.png)

## Connecting via SSH for the first time

When you originally setup your raspberry pi you would have either set a username or password up or you may have left it to the defaults.

If you have left the default user and password it is as below:

- username -> `pi`
- password -> `raspberry`

To connect via ssh you will need to use the below:

`ssh <pi username>@<pi ip address>`

An example as below:

`ssh pi@192.168.0.100`

You may need to input your password if you created a user on the standard set up or simply input the default password if no user created which is `raspberry`.

## Setting up your SSH keys

SSH keys need to be set be created on your local machine with the public key shared with the server. In this case the raspberry pi.

### Generating your local SSH keys

There is a useful article from GitHub that covers how to generate your SSH keys locally and can be found [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

Your keys should be stored under the hidden folder `.ssh`.

You can quickly check they have been generated successfullly by using the below command:

`ls ~/.ssh/` -> you should be able to see your `id_rsa` and `id_rsa.pub` keys in the folder.

### Copying your SSH

The SSH programme is actually `OpenSSH` if installing for the first time and `OpenSSH` comes with a useful key copying tool.

You will need to copy your local public key (`id_rsa.pub`) to your Raspberry pi.

You will need your Raspberry Pi's IP address, which you can find the instructions in the [local network setup](https://github.com/kcorn1982/raspberry_pi_project/tree/main/raspberry_pi_setup/local_network_setup)

Simply type `ssh-copy-id <pi username>@<pi ip address>`

e.g. -> `ssh-copy-id pi@192.168.0.100`

You will likely be met with the `password:` - which will be `raspberry` if your using the default `pi` user.

Once this is complete you should log out and login again, this time you should not have to enter your password.

## Switching off SSH password (Optional)

Although setting up SSH keys makes logging in easier, it's more for security purposes. If you intend to use your Pi as a web server, or if you wish to access your Pi externally you ideally want to switch off password authentication for SSH.

To do this you will need to access the `sshd_config` file.

You can access the file by typing `sudo nano /etc/ssh/sshd_config`.

Xithin the file you will need to look for the below, remove the `#` from `PasswordAuthentication` and switch to `no`:

```text
# To disable tunneled clear text passwords, change to no here!
PasswordAuthentication no
#PermitEmptyPasswords no
```

Lastly, you'll need to restart the SSH service:

`sudo /etc/init.d/ssh reload`

If you now exit any windows and attempt to SSH in, you should now be automatically logged in.
