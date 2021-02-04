---
author: liuadmin
categories:
- NSM
comments: true
date: 2007-06-21T08:58:00Z
slug: how-to-install-hyperic-hq-on-opensuse-102
tags:
- Hyperic HQ
- opensuse
title: How to install  hyperic-hq on openSuse 10.2
url: /2007/06/21/how-to-install-hyperic-hq-on-opensuse-102/
wordpress_id: 49167
---

<br />	
  * <br />

#### ****Make the hq and group****

<br />
<br /><br />groupadd hq useradd -c 'hyperic hq' -d /home/hq -g hq -s /bin/bash  hq mkdir /home/hq chown -R hq.hq /home/hq<br /><br />	
  * <br />

#### ****Untar installer package and install ****

<br />
<br /><br />cd /home/hq tar zxf hyperic-hq-installer-3.0.4-389-x86-linux.tgz chown -R hq.hq . su hq  hq@Suse:~> cd hyperic-hq-installer/ hq@Suse:~/hyperic-hq-installer> ls LICENSES.txt  agent-3.0.4.tgz  installer-3.0.4  server-3.0.4.tgz  setup.bat  setup.sh  shell-3.0.4.tgz hq@Suse:~/hyperic-hq-installer> ./setup.sh Unpacking JRE to temporary directory /tmp/jre Initializing Hyperic HQ 3.0.4 Installation... Loading taskdefs... Taskdefs loaded Choose which software to install: 1: Hyperic HQ Server 2: Hyperic HQ Shell 3: Hyperic HQ Agent You may enter multiple choices, separated by commas. 1,2,3 HQ server installation path [default '/home/hyperic']: /home/hq HQ shell installation path [default '/home/hq']:  HQ agent installation path [default '/home/hq']:  Loading install configuration... Install configuration loaded. Preparing to install... Validating agent install configuration... Validating shell install configuration... Validating server install configuration... Checking server webapp port... Checking server secure webapp port... Checking server JRMP port... Checking server JNP port... Verifying admin user properties Validating server DB configuration... Installing the agent... Looking for previous installation Unpacking agent to: /home/hq/agent-3.0.4... Installing the JRE ... Unpacking JRE x86-linux-glibc2-jre.tar.gz to: /home/hq/agent-3.0.4... Setting permissions on agent binaries... Fixing line endings on text files... -------------------------------------------------------------------------------- Installation Complete: Agent successfully installed to: /home/hq/agent-3.0.4 --------------------------------------------------------------------------------  You can now start your HQ agent by running this command:  /home/hq/agent-3.0.4/hq-agent.sh start  Installing the shell... Unpacking shell to: /home/hq/shell-3.0.4... Installing the JRE ... Unpacking JRE x86-linux-glibc2-jre.tar.gz to: /home/hq/shell-3.0.4... Setting permissions on shell binaries... Fixing line endings on text files... -------------------------------------------------------------------------------- Installation Complete: Command shell successfully installed to: /home/hq/shell-3.0.4 -------------------------------------------------------------------------------- You can now start the HQ shell by running this command:  /home/hq/shell-3.0.4/hq-shell.sh  Installing the server... Unpacking server to: /home/hq/server-3.0.4... Creating server configuration files... Copying binaries and libraries to server installation... Copying server configuration file... Copying server control file... Copying server binaries... Copying server libs... Setting up server database...  Now login to another terminal as root and execute this script:  /home/hq/hyperic-hq-installer/installer-3.0.4/data/hqdb/tune-os.sh  This script sets up the proper shared memory settings to run the built-in database.  Press Enter after you run the script to continue this installation.  Setting up JDBC driver... Copying database files... Configuring database... Starting repopulation of configuration table... Waiting for built-in database to start (on port 9432)... Starting built-in database... Preparing database... Vacuuming database... Waiting for server to stop... Stopping built-in database... Built-in database stopped. Installing the JRE ... Unpacking JRE x86-linux-glibc2-jre.tar.gz to: /home/hq/server-3.0.4... Setting permissions on server binaries... Fixing line endings on text files... -------------------------------------------------------------------------------- Installation Complete: Server successfully installed to: /home/hq/server-3.0.4 --------------------------------------------------------------------------------  You can now start your HQ server by running this command:  /home/hq/server-3.0.4/bin/hq-server.sh start  Note that the first time the HQ server starts up it may take several minutes to initialize.  Subsequent startups will be much faster.  Once the HQ server reports that it has successfully started, you can log in to your HQ server at:  http://Suse.opensource.org:7080/ username: hqadmin password: hqadmin  To change your password, log in to the HQ server, click the "Administration" link, choose "List Users", then click on the "hqadmin" user.  Setup completed. A copy of the output shown above has been saved to: /home/hq/hyperic-hq-installer/installer-3.0.4/hq-install.log  Deleting temporary JRE hq@Suse:~/hyperic-hq-installer> hq@Suse:~/hyperic-hq-installer> /home/hq/server-3.0.4/bin/hq-server.sh start Starting HQ server... Initializing HQ server configuration... Checking jboss jndi port... Checking jboss mbean port... Starting HQ built-in database... HQ built-in database started. Booting the HQ server... HQ server booted. Login to HQ at: http://127.0.0.1:7080/ hq@Suse:~/hyperic-hq-installer><br /><br />	
  * <br />

#### ****Startup a Linux agent ****

<br />
<br /><br />login as: hq Using keyboard-interactive authentication. Password: Have a lot of fun... hq@Suse:~> pwd /home/hq hq@Suse:~> ls agent-3.0.4           hyperic-hq-installer-3.0.4-389-x86-linux.tgz  shell-3.0.4 hyperic-hq-installer  server-3.0.4 hq@Suse:~> cd agent-3.0.4/ hq@Suse:~/agent-3.0.4> ls agent.properties  hq-agent.exe  jre  pdk                 README.txt background.bat    hq-agent.sh   lib  product_connectors  tmp background.sh     jaas.config   log  rcfiles hq@Suse:~/agent-3.0.4> ./hq-agent.sh Syntax: ./hq-agent.sh hq@Suse:~/agent-3.0.4> ./hq-agent.sh start Starting agent - Unable to load agent token file.  Generating a new one ... Done - Invoking agent - Starting agent process Agent successfully started  [ Running agent setup ] What is the HQ server IP address: 127.0.0.1 Should Agent communications to HQ always be secure [default=no]: What is the HQ server port     [default=7080]: - Testing insecure connection ... Success What is your HQ login [default=hqadmin]: What is your HQ password: What IP should HQ use to contact the agent [default=127.0.0.2]: What port should HQ use to contact the agent [default=2144]: - Received temporary auth token from agent - Registering agent with HQ - HQ gave us the following agent token 1182416897800-4295885070579017509-616515886345923858 - Informing agent of new HQ server - Validating - Successfully setup agent hq@Suse:~/agent-3.0.4>  Note: this agent and server are same machine.<br /><br />	
  * <br />

#### ****Access to Web console ****

<br />
<br /><br />http://Ip_address:7080/ default username and password [hqadmin/hqadmin]
