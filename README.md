# Studying the Robustness of Transformer-based Imitation Learning to Domain Shift

**As part of the final course project for CS330: Deep Multi-Task and Meta Learning, Fall 2022**

**Authors: Nikos Soulounias, Avidesh Marajh, Sidhart Krishnan**

![Alt Text](https://github.com/nsoul97/RLBench/blob/main/figures/open_drawer_random_clrs.gif)

This repo is based on the peract branch of [this RLBench fork](https://github.com/MohitShridhar/RLBench/tree/peract). We implement visual pertubations for the tasks 'open drawer', 'sweep to dustpan of size', 'place_wine_at_rack_location', 'slide_block_to_color_target', 'sweep_to_dustpan_of_size', 'turn_tap', which were used to train the PerAct agent.


Keep in mind, that the RLBench fork of the PerAct paper is not up to date with the latest changes in the official RLBnech repo, and therefore, neither is this repo.

## Install

RLBench is built around PyRep and V-REP. First head to the 
[PyRep github](https://github.com/stepjam/PyRep) page and install.

**If you previously had PyRep installed, you will need to update your installation!**

Hopefully you have now installed PyRep and have run one of the PyRep examples.
Now lets install RLBench:

```bash
pip install -r requirements.txt
pip install .
```

And that's it!

If you want to run the PerAct generalization experiments, follow the installation instruction in the [PerAct repo](https://github.com/peract/peract), but clone and install this RLBench repo instead.

## Generating expert demonstrations

```
cd <install_dir>/RLBench/tools
python dataset_generator.py --tasks=open_drawer \
                            --save_path=$PERACT_ROOT/data/val \
                            --image_size=128,128 \
                            --renderer=opengl \
                            --episodes_per_task=10 \
                            --processes=1 \
                            --all_variations=True
```

## Perturbed Tasks
We implement color- and texture-perturbed tasks based on the following original tasks, which were used to train the PerAct agent:

### Meat off grill

#### original task

![meat_off_grill](https://user-images.githubusercontent.com/34735067/206891002-44dc13c5-3d78-4f29-8926-4f5a191ba047.png)

#### random colors: [meat_off_grill_random_clrs.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/meat_off_grill_random_clrs.py)

![meat_off_grill_random_clrs](https://user-images.githubusercontent.com/34735067/206891003-77fbd143-f6b7-4f0e-b21a-16269e623cea.png)

#### random full body color: [meat_off_grill_random_full_body_clr.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/meat_off_grill_random_full_body_clr.py)

![meat_off_grill_random_full_body_clr](https://user-images.githubusercontent.com/34735067/206891004-38e49d54-28bd-40dd-a829-75b1549254ac.png)

#### random full body texture: [meat_off_grill_random_full_body_texture.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/meat_off_grill_random_full_body_texture.py)

![meat_off_grill_random_full_body_texture](https://user-images.githubusercontent.com/34735067/206891006-c4400d4f-63f0-432e-ba55-51cb7fd8b7f5.png)

#### random textures: [meat_off_grill_random_textures.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/meat_off_grill_random_textures.py)

![meat_off_grill_random_textures](https://user-images.githubusercontent.com/34735067/206891007-cf0fdd52-0b4f-46b7-bdfe-0f0676d5ece8.png)


### Open Drawer

#### original task

![zoomed_open_drawer](https://user-images.githubusercontent.com/34735067/206886062-1bd51ceb-5f18-49a9-9e3c-fcc44a91cf5d.png)

#### random colors: [open_drawer_random_clrs.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/open_drawer_random_clrs.py)

![zoomed_open_drawer_random_clrs](https://user-images.githubusercontent.com/34735067/206886064-613a0efb-8913-4e1f-9b40-cff237cfc67d.png)

#### random frame color: [open_drawer_random_frame_clr.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/open_drawer_random_frame_clr.py) 

![zoomed_open_drawer_random_frame_clr](https://user-images.githubusercontent.com/34735067/206886065-f2a38c9f-e829-4f25-a010-955ebd0d0767.png)

#### random frame texture: [open_drawer_random_frame_texture.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/open_drawer_random_frame_texture.py) 

![zoomed_open_drawer_random_frame_texture](https://user-images.githubusercontent.com/34735067/206886066-f39b5c03-46bd-40c5-81d9-d56d9484cce6.png)

#### random full body color: [open_drawer_random_full_body_clr.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/open_drawer_random_full_body_clr.py)

![zoomed_open_drawer_random_full_body_clr](https://user-images.githubusercontent.com/34735067/206886068-01ca2d62-240c-40e0-a753-aacbf5527235.png)

#### random full body texture [open_drawer_random_full_body_texture.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/open_drawer_random_full_body_texture.py)

![zoomed_open_drawer_random_full_body_texture](https://user-images.githubusercontent.com/34735067/206886070-a40f0f35-6d24-46c8-96ed-e3b570f08404.png)

#### random textures: [open_drawer_random_textures.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/open_drawer_random_textures.py)

![zoomed_open_drawer_random_textures](https://user-images.githubusercontent.com/34735067/206886071-5ca416d5-981f-4241-89f5-0ae32d9dcb2b.png)

### Place wine at rack location

#### original task

![place_wine_at_rack_location](https://user-images.githubusercontent.com/34735067/206890195-925f5156-8e69-4df2-b5bf-3fc59bbd773a.png)

#### random colors: [place_wine_at_rack_location_random_clrs.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/place_wine_at_rack_location_random_clrs.py)

![place_wine_at_rack_location_random_clrs](https://user-images.githubusercontent.com/34735067/206890196-18686fdc-12f5-4d8a-9c9c-93815d1adf0a.png)

#### random full body colors: [place_wine_at_rack_location_random_full_body_bottle_rack_clrs.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/place_wine_at_rack_location_random_full_body_bottle_rack_clrs.py)

![place_wine_at_rack_location_random_full_body_bottle_rack_clrs](https://user-images.githubusercontent.com/34735067/206890197-7d41dcf4-9a45-4625-8b37-45f263777e6a.png)

#### random full body textures: [place_wine_at_rack_location_random_full_body_bottle_rack_textures.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/place_wine_at_rack_location_random_full_body_bottle_rack_textures.py)

![place_wine_at_rack_location_random_full_body_bottle_rack_textures](https://user-images.githubusercontent.com/34735067/206890198-b371da07-c5a4-426f-9163-0c8babb2097f.png)

#### random same full body color: [place_wine_at_rack_location_random_same_full_body_clr.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/place_wine_at_rack_location_random_same_full_body_clr.py)

![place_wine_at_rack_location_random_same_full_body_clr](https://user-images.githubusercontent.com/34735067/206890199-ca75ace6-3cad-40db-a449-5c1954c9d9c7.png)

#### random same full body texture:  [place_wine_at_rack_location_random_same_full_body_texture.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/place_wine_at_rack_location_random_same_full_body_texture.py)

![place_wine_at_rack_location_random_same_full_body_texture](https://user-images.githubusercontent.com/34735067/206890200-f49829e8-e754-4b05-9dcc-4f954e741b81.png)

#### random textures: [place_wine_at_rack_location_random_textures.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/place_wine_at_rack_location_random_textures.py)

![place_wine_at_rack_location_random_textures](https://user-images.githubusercontent.com/34735067/206890202-b114e87c-d939-4631-accf-7dfb3694eb53.png)


### Slide block to color target

#### original task

![slide_block_to_color_target](https://user-images.githubusercontent.com/34735067/206886883-ea7e7327-2fae-43f9-9133-c89bcd58f6a6.png)

#### random block color: [slide_block_to_color_target_random_block_clr.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/slide_block_to_color_target_random_block_clr.py)

![slide_block_to_color_target_random_block_clr](https://user-images.githubusercontent.com/34735067/206886884-dfd88528-6c2b-474e-92c8-4c0ae3fbcaa9.png)

#### random block texture: [slide_block_to_color_target_random_block_texture.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/slide_block_to_color_target_random_block_texture.py)

![slide_block_to_color_target_random_block_texture](https://user-images.githubusercontent.com/34735067/206886886-ba2ac015-9a29-4d4d-89b8-8afd0ba76a00.png)

### Sweep to dustpan of size


#### original task

![sweep_to_dustpan_of_size](https://user-images.githubusercontent.com/34735067/206889607-bbcf4e64-192b-442f-92c0-739b9830c159.png)

#### random colors: [sweep_to_dustpan_of_size_random_clrs.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/sweep_to_dustpan_of_size_random_clrs.py)

![sweep_to_dustpan_of_size_random_clrs](https://user-images.githubusercontent.com/34735067/206889609-e7b42511-74d9-4452-b3f8-ae731d606b97.png)

#### random full body colors: [sweep_to_dustpan_of_size_random_full_body_entities_clrs.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/sweep_to_dustpan_of_size_random_full_body_entities_clrs.py)

![sweep_to_dustpan_of_size_random_full_body_entities_clrs](https://user-images.githubusercontent.com/34735067/206889610-3e074f00-ff23-4b5d-8758-20a5a4b47ed2.png)

#### random full body textures: [sweep_to_dustpan_of_size_random_full_body_entities_textures.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/sweep_to_dustpan_of_size_random_full_body_entities_textures.py)

![sweep_to_dustpan_of_size_random_full_body_entities_textures](https://user-images.githubusercontent.com/34735067/206889611-60bd89d8-cb75-4fd4-89f6-229742e622c3.png)

#### random same full body color: [sweep_to_dustpan_of_size_random_same_full_body_clr.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/sweep_to_dustpan_of_size_random_same_full_body_clr.py)

![sweep_to_dustpan_of_size_random_same_full_body_clr](https://user-images.githubusercontent.com/34735067/206889612-4e3ce070-5871-4e2a-880a-1a2874ba76b2.png)

#### random same full body texture: [sweep_to_dustpan_of_size_random_same_full_body_texture.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/sweep_to_dustpan_of_size_random_same_full_body_texture.py)

![sweep_to_dustpan_of_size_random_same_full_body_texture](https://user-images.githubusercontent.com/34735067/206889613-a6a7778f-a283-4947-9c4b-b7ab66e09626.png)

#### random textures: [sweep_to_dustpan_of_size_random_textures.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/sweep_to_dustpan_of_size_random_textures.py)

![sweep_to_dustpan_of_size_random_textures](https://user-images.githubusercontent.com/34735067/206889614-03cbd70b-707b-4cc7-bb6d-54cfb50bc88a.png)

### Turn tap

#### original task

![turn_tap](https://user-images.githubusercontent.com/34735067/206885497-552d391b-8d79-4b85-9db9-be9da964b6da.png)

#### random colors: [turn_tap_random_clrs.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/turn_tap_random_clrs.py)

![turn_tap_random_clrs](https://user-images.githubusercontent.com/34735067/206885498-2ffd376b-72b8-4d86-ba0b-96e9571d1a79.png)

#### random full body color: [turn_tap_random_full_body_clr.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/turn_tap_random_full_body_clr.py)

![turn_tap_random_full_body_clr](https://user-images.githubusercontent.com/34735067/206885499-a76e4ba9-3cf7-49bb-879a-ec04906c5f8b.png)

#### random textures: [turn_tap_random_textures.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/turn_tap_random_textures.py)

![turn_tap_random_textures](https://user-images.githubusercontent.com/34735067/206885501-660b354a-6207-49da-b0c9-d5b64b243b7e.png)

#### random full body texture: [turn_tap_random_full_body_texture.py](https://github.com/nsoul97/RLBench/blob/main/rlbench/tasks/turn_tap_random_full_body_texture.py)

![turn_tap_random_full_body_texture](https://user-images.githubusercontent.com/34735067/206885500-85323dc1-4766-4591-9010-f77d76ef2bdb.png)
