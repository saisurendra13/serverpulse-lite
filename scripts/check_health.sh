#!/bin/bash
# ServerPulse Lite — Bash Health Checker
# Author: Sai Surendra Munagala
# Device: Raspberry Pi (Production_Monitoring)
# Reads CPU, RAM, disk from Linux system and appends to metrics.log
# Format matches actual output: 2026-05-15 12:18:04,3.3,28.6,23

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
CPU=$(top -bn1 | grep 'Cpu(s)' | awk '{print $2}' | cut -d'%' -f1)
RAM=$(free -m | awk 'NR==2{printf "%.1f", $3*100/$2}')
DISK=$(df -h / | awk 'NR==2{print $5}' | cut -d'%' -f1)

echo "$TIMESTAMP,$CPU,$RAM,$DISK" >> /home/seema/metrics.log
