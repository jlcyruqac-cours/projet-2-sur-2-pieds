# Utilisation install.cmd
1. Copier "FreeSWITCH-1.10.0-Release-x64.msi" au même niveau que "install.cmd"

   [Télécharger ici](https://files.freeswitch.org/windows/installer/x64/FreeSWITCH-1.10.0-Release-x64.msi)
2. Exécutez "install.cmd"

***

Le serveur FreeSWITCH sera installé, configuré et lancé automatiquement.

external.xml
<param name="ext-rtp-ip" value="$${local_ip_v4}"/>
<param name="ext-sip-ip" value="$${local_ip_v4}"/>
<!-- <param name="ext-rtp-ip" value="$${external_rtp_ip}"/> -->
<!-- <param name="ext-sip-ip" value="$${external_rtp_ip}"/> -->
	
internal.xml
<param name="ext-rtp-ip" value="$${local_ip_v4}"/>
   <param name="ext-sip-ip" value="$${local_ip_v4}"/>