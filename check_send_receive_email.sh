#!/bin/bash

################################################################################
# Nagios plugin to monitor email                         #

# Datum 03.03.2021                        #
################################################################################

VERSION="Version 1.0"
AUTHOR="Michael Tschoepe"

PROGNAME="check_send_receive_email.sh"

# Constants

# Input parameters


# Exit codes
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3

#Main #########################################################################



#  Zufallsnummer fuer  email Betreff


number=$RANDOM$RANDOM$RANDOM


# change receiver email


sudo echo "check_send_receive_email" | mail -s "icinga-ping $number" receiver email



sleep 240


# su nagios -c "fetchmail --nosslcert"

fetchmail -vvv -N -F -K --port=143  --sslproto '' > /dev/null 2>&1



# pruefen ob das mail  zureuck gesendet wurde


mailReceive=$(less /var/mail/root |grep "$number")


if [ ! -z "$mailReceive" ]

then

echo $PROGNAME: OK
echo Das Email mit dem Betreff $number wurde gesendet und die Antwort wurde empfangen. 

exit $STATE_OK


else

echo $PROGNAME: CRITICAL
echo Das Email mit dem Betreff $number wurde nicht gesendet oder die Antwort wurde empfangen. Es kann auch sein dass beim Emailversand und Emailempfang eine normale Verzoegerung stattfindet. Bitte abwarten, wenn der Fehler weiterhin angzeigt wird bitte manuell den Emailversand und Emailempfang pruefen.
exit $STATE_CRITICAL


fi







# installation und konfiguration




# apt install mailutils

# apt install postix
# intrnetsite

 # tl02v-mgmt01.tltges.local



# ++++++

# nano /etc/postfix/main.cf



# # neu
# append_dot_mydomain = no

# canonical_maps = hash:/etc/postfix/canonical
# # neu stop


# #neu
# relayhost = 10.0.16.160
# #neu stop


# nano /etc/postfix/canonical
# root@tl02v-linuxtest01  michael.tschoepe@telent.de



# postmap /etc/postfix/canonical

# systemctl reload postfix



# echo "Der Mailversand wird gepreuft." | mail -s icinga_check icinga.satellit@gmail.com


# +++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++

# apt install fetchmail

# adduser sat

# su sat 

# cd ~

# nano .fetchmailrc

# #set postmaster "ice"
# #set daemon 600
# poll 10.0.16.160 with proto IMAP
   # user "tltges\\icinga.satellit" is ice here
   # password "ov5D9KsmyRaF"
   # #options ssl
   # fetchlimit 400
   # folder 'INBOX'
   # fetchlimit 5

# chmod 0700 .fetchmailrc

# +++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++

# less /var/mail/sat 

# less /var/log/mail.log

# ##################


# Defaults:nagios !requiretty
# nagios ALL=(root) NOPASSWD: /usr/lib/nagios/plugins/check_send_receive_email





# #####################

# mail

# icinga

# 93gg99g4!!g()g(AgDDgF

# E-Mail Adresse 	icinga@netzikon.com


# Speicherplatz 	1,0 GB
# IMAP-Server: 	imap.strato.de
# POP-Server: 	pop3.strato.de
# SMTP-Server: 	smtp.strato.de
# Hilfe
# Passwort 	Ihr Passwort für folgende E-Mail Adresse wurde geändert: icinga@[Alle Domains]
# Spamschutz 	Betreff von Spam-Mails im Posteingang markieren 
