# python-autonomous-navigation

A Python-based autonomous navigation project focused on developing fundamental skills in robotics, path planning, obstacle avoidance, and motion simulation. Built progressively to explore core algorithms and their applications in UAV autonomous navigation.

The project is a 2D simulator written with Pygame. The drone is modelled as a simple moving agent on a grid (no flight dynamics). The aim is a drone that plans a route with A*, follows it, and replans when moving obstacles block its path. It is a personal learning project, built in stages and documented as it progresses.

## Current status

**Stage 1 complete: static 2D environment.**

![Stage 1 environment](docs/images/stage1_environment.png)

The window shows a 20 x 15 occupancy grid with static obstacles (grey), a start cell (green), a goal cell (yellow) and a drone (blue circle). The drone does not move or plan a path yet.

## Roadmap

- [x] Stage 1: Grid environment and drone display
- [ ] Stage 2: A* path planning
- [ ] Stage 3: Path following
- [ ] Stage 4: Dynamic obstacles
- [ ] Stage 5: Collision detection and replanning
- [ ] Stage 6: Testing, performance evaluation and documentation

## Requirements and how to run

- Python (tested with 3.11)
- Pygame

```text
pip install pygame
python main.py
```
