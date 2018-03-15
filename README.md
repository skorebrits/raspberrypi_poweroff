# Poweroff a raspberry pi with a physically attached button

Connect a button to Ground & GPIO 2

Raspberry Installation

- cp power_off.py & poweroff.sh to /home/pi/
- chmod 755 poweroff.sh
- sudo crontab -e
- @reboot sh /home/pi/poweroff.sh >/var/log/poweroff.log 2>&1