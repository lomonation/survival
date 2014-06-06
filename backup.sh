#!/bin/bash

cd /home/lomo/minecraft/survival/
screen -p 0 -S minecraft -X eval 'stuff "say Starting backup.\015"'
screen -p 0 -S minecraft -X eval 'stuff "save-off\015"'
screen -p 0 -S minecraft -X eval 'stuff "save-all\015"'
sleep 10
tar -czf ~/minecraft/backups/survival/$(date +%F_%H-%M).tar.gz *
screen -p 0 -S minecraft -X eval 'stuff "say Backup complete.\015"'
screen -p 0 -S minecraft -X eval 'stuff "save-on\015"'
