更新日志 *(1.7.10)*
##V6.06.02:
[COMPAT]
I went through the List of Items Erebus adds, to see what they could be used for.
I did not expect THAT many potentially compatible Items, when looking for the Mod that adds Jade, that I saw it in one of Ethos Videos.
Damn, even needed to add Ore Generation Handling to it in order to make Umberstone properly Ore-Generateable.
And I fixed some of their Bucket related Fluid things too, as it uses the Biomes o' Plenty Honey instead of the Forestry Honey.
[NINJA-FIXED] Loot Chest Replacing didn't work properly.
[FIXED] Some Stone alike Gears were not craftable the new intended way (4 Rocks + 4 Stone Blocks), and they were not usable as Buildcraft alike Gears despite being made of Rock.
[CHANGED] You can no longer use Stone alike Blocks for crafting Hammers. The Clubs can still be made with Blocks.
[ADDED] Breaking the GT6 Cobblestones with a Hammer, Club or Jackhammer will give you Rocks that can be used for Basic Tools. Don't worry, the natural Smoothstone still drops Cobblestone, so you can still Jackhammer the Granites and Stuff.
[ADDED] There is now more earlygame Tools available. Bamboo and Petrified Wood can be used as Handles and more Rocks can be used as Toolhead.
[ADDED] Sanding Machine. It does the same Stuff that the Grindstone does, but in Machine Form.
[ADDED]
Long Distance Item Pipelines and Fluid Pipelines.
They are similar to Long Distance Wires, and they are also One-Way.
Unlike the Long Distance Wires, they don't have any Loss, since they don't really transport Energy.
The Transfer of Items and Fluids is instant, basically Teleportation, but lets just pretend it's going through that Dummy Pipe.
Nonuple and Quadruple Fluid Pipes work with the Long Distance Fluid Pipeline too.


##V6.06.01:
[FIXED] When Roads were enabled, all Vanilla and GT6 Surface things close to the X and Z Axis ceased to generate, regardless of being in the Overworld (where it is intended) or not (such as in the Nether, the End or Twilight).
[CHANGED] The Bedrock Ore Variety has increased a little, because I felt like it while assigning Flowers to the Bedrock Ores.
[ADDED] Config to turn off Death by the currently 5 Types of Food Poisoning. You will be left with Half a Heart though!
[ADDED] Config to disable overground (>= Y:50) Mob Spawns close to Spawn. It is defaulting to TRUE, so for about 144 Meters in each direction from Spawn there is no Mobs spawning.
[ADDED]
Special Flowers generating in Grassy or Deserty Terrains.
They indicate the Location of the rare Bedrock Ore Mining Spots.
Bedrock Ore mining Spots do have a bunch the regular Ore around them, so they are still useful.
If you want to produce more of these Flowers, you will have to use Bumblebees to create more of the ones you already found.
The Desert Flowers work for both, regular Flower Bumblebees and Desert Bumblebees.


## V6.06.00:
[IMPORTANT]
Fluid Pipes have their Tank Capacity halved, but they still transfer the same amount of Fluid per Tick.
DRAINS NEED TO BE ON PIPES TWICE THE SIZE TO WORK PROPERLY!!! (unless they are in an Ocean, Swamp or River)
This will also affect filling of vanilla Cauldrons and Advanced Worktables, as you need a Pipe twice the size for that now.
Don't worry, excess Fluid in Pipes on loading the World wont be voided, and it likely won't overflow anything either.
Yet still I verily recommend to turn off all Steam related things before the Update.
I will let my Test Bear run all his pipe connected Boiler Setups before and after the Update, to make sure nothing blows up on your end either.
[COMPAT] Fallen Meteors Mod
I checked it for OreDict related Information. I added 5 new Materials due to that.
The Magnetization Enchant of it is now applied to all Magnetic Materials of GT6 if it is installed.
[COMPAT] Railcrafts Implosion Enchant will now automatically be applied to a lot of Gems. Implosion = Extra Creeper Damage.
[FIXED] A Bug that crashed GT6 with Ars Magica.
[FIXED] Large Ore Veins were generating all over the Y Axis, having a different Y Coordinate for generating in each Chunk.
[CHANGED] Electrolyzer and Centrifuge decomposing Recipes will now use 14 instead of 16 as a Basis for GU/t.
[CHANGED]
Some Alloys can now have multiple Attack Enchants attached to them.
Black, Red and Blue Steel now have their Sharpness slightly nerfed due to that, since they got quite a few additional effects now.
Electrum now has Smite, Disjunction and Werebane for example.
Damascus Steel is still Sharpness 5.
[ADDED] Universal Spade can now place Torches
[ADDED] A more convenient Recipe for Dispensers, using Droppers as step inbetween, without having the unstackability of Bows make things a bitch.
[ADDED] Slime Fluid and Slime Bottles that can be used like Glue Bottles. It gives you a chance of Jump Boost.
[ADDED] Plastic Storage Boxes, that are like Mass Storages, but for 128, 256, 512 or 1024 Items at a time and way cheaper than even the Item Barrels, once you get Plastic.
[ADDED]
Optional Worldgenerated Asphalt Streets along the X and Z Axis.
I know from own experience that Roads are a Server Infrastructure thing nobody really wants to work on, so Worldgen it is. Maybe I can later add Structures to this too.
The Roads have Signs every 512 Meters, close to the Region File Borders. The Signs tell what Coordinates the 4 Region Files have at the Chunk Border between the Sign and the U-Turn Section.
Once the Middle Crossing at 0, 0 is Generated, it will automatically set the Server Spawn Point to itself once (It won't try to do that anymore after the Crossing generated). The Compass may point to the old Spawn until you reload the Client.
They are disabled by Default because they could be seen as not only unfitting for the more Medieval/Fantasy Playstyles, but also because they are easily exploitable Sources of Asphalt and Concrete.
Note, that GT6 Dungeons do not spawn close to these Roads (at least 256 Meters away), so they won't help you find them at all!
GT6 Trees, Logs, Sticks, Rocks, Bushes, Glowtusses, Bumblehives, Black Sand and Clay Pits are at least 64 Meters away from the center of a Street Section to not interfere with the Road itself.
I know that Tunnels sometimes have Light Update Issues, but unlike with the GT6 Dungeons where I fixed them already, those Issues are pretty much unfixable for Roads, as I would have to cause an Infinite Worldgen Loop to make those Lights work! THAT's how Terrible Minecraft is!


//=== Version Number Jump because of Fluid Pipes changing a bit ===//


## V6.05.52:
[COMPAT] Open Modular Turrets Recipes got changed for:
Hard Walls. They now adopt a System similar to my Concrete and Reinforced Concrete by requiring Metal Bolts and the Hand Drill. The Tier 1 and 4 Variants can be crafted directly out of GT6 Concrete and Reinforced Concrete.
Fences. They require Fine Iron Wires for the Fence itself and Metal Bolts for the barbs of the Barbed Wire Part. I changed up the Tiering to be more GT6 than Vanilla, so the Fence Barb Colors may not match the Recipe anymore.
Turret Bases. They require a lot of Electric Components to be crafted now. The Wooden one just requires a Tier-0 Motor, and doesn't need a Battery, Circuit or Sensors, so your Handcrank Potato Cannons are still very earlygame.
Ammo has cheaper  and more realistic Recipes now.
[FIXED] Eggs now despawn after a Minute regardless of my Item Despawn Time Config. This is because Chickens would be spamming Item Entities on the ground, so see this as if the Eggs are rotting.
[ADDED] Blast Resistance Tooltips now say whether they can stand a Ghast Fireball, Creeper or TNT Blast or not.
[ADDED]
Wall Spikes that can be pushed by Pistons. (and you can't walk horizontally into ones placed on the floor, so you won't be damaged by accident all the time)
There is also an Omnidirectional Spike, but it only deals half the Damage in return.
And a Gravity Variant of the Omnidirectional Spike exists too!
Walking ontop of any Spikes will slow you down a lot, meaning escaping is a bit harder, also balancing ontop of Sideways Wall Spikes is slower due to that too.
Steel Spikes don't work on Skeletons, Slimes or Iron Golems.
Titanium Spikes work on all Mobs and deal twice the Damage of Steel Spikes.
Tungstensteel Spikes work on all Mobs and deal three times the Damage of Steel Spikes.
Gold, Silver, Copper and Lead Spikes deal four times the Damage of Steel Spikes when they are against a Mob that is weak to their Material, otherwise it's only minimal or no Damage in case of Iron Golems, Slimes or Skeletons (unless they are weak to it).
Adamantium Spikes deal ten times the Damage of Steel Spikes against every Mob touching them.
Placing Hoppers below the Spikes will work fine, as they have a Slab alike Box Shape for Collision.

## V6.05.51:
[兼容] 星系(Galacticraft)机器在接入HV以上的GT6能量后也会爆炸。
[兼容] 模块化开放式炮塔(Open Modular Turrets)
炮塔能够接入HV及以下的电压。如果在EV以上会爆炸! 注意这点!!!
作者给硬化墙壁加入了爆炸抗性说明, 能够读出其硬度。1阶的墙壁甚至不能抵挡TNT爆炸,这至少需要2阶。
[兼容] Lycanite Mobs。
通过加入搅拌机中的恶魂之泪+岩浆配方来修复该mod中"Pure Lava Bucket" 配方复制铁桶的bug。
用GT6的斧头和锯子对付树妖会掉落更多橡木 (斧头更好些)。 原木数量取决于对其非魔法攻击的伤害 (无论它还有多少血量剩余). 甚至能够做到一击64个原木
Wargs会掉落狗肉。
[修复] 黄蜂不会在星系间的暗物质或虚空中工作了。
[修复] 所有mod的流体标志, 导致某些情况下渲染流体标志, 而不是产生一个流体方块。 这修复了Lycanite Mobs的某两种液体。
[移除] 纸覆盖版的碰撞箱, 你怎么能站在一张纸上???? 让我们看看有多少人用一张纸当管道保护板之后……喜闻乐见。
[增加] 石灰石, 与大理石的生成率和方块属性相同, 材质和GT5的混凝土一样。 如果需要方解石粉,这也是一个来源。
[增加] 用锤子或辊压机压平弯曲板的配方。
[增加] 木片, 只是木质覆盖版罢了, 所以不需要用帆布做木材质覆盖版了。 所有可以用来做书架的木板都能做成这个。 每片需要1个钢/铁螺丝 (每次合成6个).
[增加] 混凝土, 建筑泡沫和沥青板 (也只是覆盖版罢了)。 在沥青覆盖板上可以加速行走!
[增加] 衣橱。 一个盔甲交换处, 可以用来快速穿衣服, 并且不像盔甲架那样会产生卡顿。 可用多种材料制作。工作原理是4个基础接口的交互。
[增加] 充能衣橱。 可以用来给IC2的盔甲充电。请确保电压级正确。 "正在工作" 和 "成功" 模式能够判断内容物是否充能完毕。

## V6.05.50:
[修复] Some things I noticed while writing the Patreon Post.
[增加] Small Vinteum Ore now generates automatically when Ars Magica is installed.
[增加] The Primal Mana Fluid from Thermal Foundation (can't be produced atm afaik), can be used to make certain Magical Materials, such as Astral Silver, Midasium, Mithril and Thaumium.


## V6.05.49:
[兼容] AE Devices can now accept GT6 EU Directly if it is HV or less. If it is EV or more it will explode! SO BE WARNED!!!
[兼容] Thermal Expansion
Tectonic Petrotheum can now be used in the Sluice for washing Ore instead of Water. (This was SUPPOSED to be already possible, but there was a Bug, preventing that from working on my end).
Blizz, Blitz and Basalz Powder can now be created in the Injector with their respective Item and Fluid Redstone.
A lot (if not all) of Recipes for filling Energy Cells, Tesseracts, Plates and Conduits with Redstone/Glowstone/Ender/Cryotheum/Aerotheum are now doable in the GT6 Canning Machine AND inside the Injector aswell (for convenience, due to the Blitz/Blizz/Basalz Recipes being Injector Only).
In the newly added Recipes, Molten and Destabilized Redstone work just fine for doing the Job. Same goes for Resonant Ender and Molten Enderpearls.
Filling a vanilla Bucket with 1440L Molten Redstone or 576L Molten Enderpearls using any GT6 thing (Taps, Canners, Crucibles etc.), will make it turn into the TE-Bucket, making an easy conversion possible without relying on the Generifier.
Blizz, Blitz and Basalz Rods use the "craft = 1 powder, mortar = 2 powder, shredder = 4 powder"-System now.
[修复] GregTech Worldgen and Burning Box Fire Placement no longer overwrite Thaumcraft Nodes as if they were Air.
[修复] Applecore caused Water to have Food Value for some reason despite me having clearly declared a Food Value of Zero.
[CHANGED] Barrels, Drums, Pots and other Fluid Containers can now be stacked when empty. The only ones Stackable when full are still the Capsule-Cell-Containers.
[CHANGED] A lot of Sluice, Bath and Magnetic Separator Recipes changed to make it possible to process singular Tiny Crushed and Purified Ores.
[增加] An example Recipe for each of the Handle based Tools.
[增加] A Compartment Drawer that has 4 Drawers with 36 regular Inventory Slots each, and is compatible with adjacent Advanced Workbenches. The Crafting Recipe needs overall 32 Units of a Metal (the Metals you can make the Chests of)
[增加]
Storage Inserter
It is SOMEWHAT like a Drawer Controller, but it only works for inserting Items BY HAND into a Wall Shaped Area of Mass Storages and/or Item Barrels.
The Wall of Mass Storages can be 50 Meters long in each direction, and 7 Meters tall counting from the Floor below it.
There are some quirks to scanning the Area, for example there has to be a Floor in front of the Wall of Mass Storages, and they aren't allowed to be obstructed nor to face the wrong way.
This whole thing is based on "simulating a person* running in front of the Wall and rightclicking every single Storage from bottom to top", so just make sure that THAT is possible to be done and it should work.
The direction the Insert will scan does depend on what side of it you click. It will essentially behave like "spawning a person* on the side you click" and then run that "person*" in all 4 compass directions trying to insert Stuff from bottom to top.
As Floor counts the following: Slabs/Stairs (any rotation possible, and most modded ones work too), Full Blocks and Blocks with a solid Top Side.
It will insert the held Item in the Hotbar when you click it, if it can.
If you click it with an Empty Hand, it will try to insert all Items in the 27 Slot Player Inventory, except things with a Max Stacksize of 1 (such as Tools), Ammunition (Arrows) and Tool-Rightclick-Placeable-Torches (because that would be annoying, if you have a Torch Item Barrel or something).
Placement for the Inserter is advised to be either as Part of the Storage Wall, or inside the Floor in front of the Storage Wall.
You can NOT, I repeat CANNOT, attach Pipes to the Storage Insert AT ALL and I will NOT add that Functionality to it!!!
(* = its not actually a person, this is just a metaphor, it only checks if the Blocks in front either don't have a Collision Box or are Carpets)

## V6.05.48:
[修复] 如今小漏斗能够装填不足1000L的流体了。
[添加] 喷嘴,气体版的龙头。


## V6.05.47:
[修复] The Names of Railcraft Plates. No longer Confusion caused by "Tin Plates" and "item.lead.plate.name" or whatever that one was.
[CHANGED] Mud is now affected by Gravity, like Sand. Also Gravity is now mentioned in Block Tooltips if it applies.
[增加] Magnetic Separator Recipes for impure and pure Dusts, so you dont have to use purified-crushed Ores for it.
[增加] All GT6 Tools can now harvest Torches directly, and in that specific case they will always be "Magnetic" and won't lose any Durability in the Process (aka: Tool + Leftclick = Pick up a Torch from the Wall directly into your Inventory).
[增加] Treated Planks in Block Form, the Item variant got removed and will automatically turn into the Block Form in all GT6 Blocks and your Inventory. It can be crafted into the Immersive Engineering Variant and back if needed.
[增加]
Black Sand to Rivers that aren't adjacent to Oceans or Swamps.
It can be used similarily to Magnetite in a lot of Recipes, also using the Centrifuge you can get Ferrovanadium out of Black Sand, so no need to worry about getting your Vanadium Pentoxide.
The Sand generates similarily to the Clay Pits, but is only 2 Blocks deep. It is NOT Part of the Ore Vein Grid!!!
Magnetite Ore itself in any form will no longer generate, in favour of the new Black Sand.
I did increase the amount of Small Hematite Ores to compensate the new lack of small Magnetite Ores. You can be happy that you have 2 more Inventory slots free for Ores that way lol.
As for the Large Magnetite Veins (that includes Ferrovanadium too), they will no longer happen in new Terrain, meaning that all other Large Veins have a slightly higher chance of spawning now.

##6.05.46:
[NOTE] I have hit the 2^16 Byte Limit of Code on MT.java yet again and needed to trim it down further in order to get GT6 to compile, this means large Code changes and some removals inside that File.
[修复] Several Tools being available for Stone despite not being intended to be like that.
[修复] Dust Funnels not dropping their partial Content when broken. They will no longer store it, making it possible to clear a Dust from the Dust Funnels.
[修复] Sealed Wood Pipes were unintentionally Gas Proof (back then it might have been intended but we have better solutions now). I fixed that by making them leak Gasses aswell, and buffing their Capacity from 50 to 75.
[CHANGED] Some Acids can no longer be electrolyzed into their Components anymore. Same goes for most Sulfur containing Chemicals.
[CHANGED] Fake 'Osmium' is now easier obtainable when Mekanism is installed. It can be processed in a Furnace too now.
[CHANGED] If a Material has a Fluid form and can be electrolyzed or centrifuged, you are going to have to use said Fluid form for that now, and can't use Dusts for it anymore.
[CHANGED] Tungsten Ore, if you happen to find any (due to other Mods or old GT6 Worldgen) will crush into 2x Scheelite instead, to ensure proper processing, while also giving a slight Bonus compared to actual Scheelite.
[CHANGED] Small Tungsten or Pinalite Ores of GT6 to Scheelite Ores. And added small Pyrolusite Ore with the same location and rarity as small Gold and Silver Ores.
[增加] Plastic Rods can now also be used instead of Wooden Sticks for most Tool Handles.
[增加] Made GC Rockets Recycleable.
[增加] Selenium as Byproduct of some Ores (I will likely use it for Batteries). I also added it into the Moon-Cheese Veins, since Selenium is literally named after the Moon.
[增加] Sodium Nitrate and a bunch of Saltpeter related Chemical Recipes.
[增加] New Processing for getting Elemental Sulfur from Sulfur Dioxide. It is similar to the Claus Process but far easier, due to not having to Filter other Materials out of the SO2.
[增加] Potassium and Sodium based Chemicals can now be interchanged in a lot of Recipes, but not all of them.
[增加] Lots of Chemistry related Materials and Recipes that didn't exist before, to make things more complete.
[增加] Crowbarred Covers now go directly into the Inventory if possible.
[增加] Tungsten Chemical Processing for Tungsten containing Ores.
[增加] Pyrolusite + Hydrochloric Acid Processing and removed its Electrolyzer Recipe.

## V6.05.45

[修复] Aqua Regia to Chloroplatinic Acid Processing producing a very unbalanced output (more Cl out than you put in), I only needed to change up the Ratios, it's the same Products as before.
[修复] Some Bugs regarding the Player Inventory restock from the Slot above Functionality of GT6 in regards of GT6 Tools and their Scrap.
[CHANGED] Tin Alloy counts as Furnace Smeltable now.
[CHANGED] Neodymium and its Magnetic variant are now Diamond-Tool Quality.
[CAHNGED] Bushes now grow 5 times slower. They were just too OP.
[增加] A dedicated Loot Chest for the Dungeon Loot change in the previous Version. Now it is no longer made of Tin Alloy, but instead is not Craftable and made of Stone and looking a bit like Mossy Stone Bricks.
[增加] Cobalt, Nickel, Germanium and Draconium "Storage Set" (Chests, Mass Storages, Shelves, Adv Crafting Tables, Hoppers etc). Also made it easier for me to add more "Storage Sets" by rewriting the Code a little.
[增加] A few Recipes regarding BoP Mud and GT6 Mud.
[增加] Tin Alloy Fluid Pipes.
[增加] Mud Version of GT6 Ores to fit in better with the muddy Swampwater of GT6. (SERIOUSLY, IT'S LIKE SAND ORES, OR NETHERRACK ORES, JUST THAT IT BELONGS TO MUDDY WATER IN NEWLY GENERATED SWAMPS!!! WHY THE FUCK IS EVERYBODY HYPED ABOUT THIS?!?)
[增加]
Some Tools will now autocollect their Drops instead of letting Item Entities fall on the ground, if the Player has enough Inventory Space.
This also applies to certain Materials you can craft Tools out of. You know, the "Magnetic" Variant.
Among those Tools (its about half of ALL Tools that can do that) is the Wrench for example, meaning you autocollect whatever you Wrench, no matter what Material the Wrench is.
That kindof fixed the Issue of "Removing Hoppers above a Crucible" as a Side Effect, since the Hopper would not Drop as Item in this case (If you have Space in your Inventory).
As Examples, here are a few Tools that Automatically have this Ability even without being Magnetic: Construction Pickaxes, Wrenches, Mining Drills and the Plow.
[增加]
Made several Extruder Recipes accessible much earlier.
The Tier 1 Extruder no longer needs Tungsten Carbide to be crafted, instead it uses Steel.
New Low Heat Extruder Shapes can be made using any Type of regular Steel.
Several Low Tier Metals count as Simple for the Extruder now, meaning they have a fixed low cost and can be formed using the Low Heat Shapes.

## V6.05.44

[NOTE] Users of the Custom Veins etc in my Worldgen Config have to manually set the amount of Custom Veins, as it no longer defaults to 8, in order to prevent Debug Error Messages from appearing in the Log (due to NULL Material in Config). And yes the Debug Errors about Worldgen Ores are for Users, not for me, and they are in the GregTech.log
[修复] A HUGE Maths Error in the Extruder Recipe Code. It used about 10 times more Energy in some cases than it should have used (all the Metal related Recipes basically). Now it will just use 25% more Energy than a Crucible would.
[修复] A Stupid Error in the Extruder Recipe Code that made Wax, Plastic and Rubber Stuff cost exactly the same no matter how many Items the Recipe Outputs.
[修复] Fluid Filters resetting again.
[CHANGED] Dungeon Loot Chests will now be replaced with GT6 Chests that only generate their Loot once you open or break them and not before that.
[CHANGED] A tiny thing in the Crafting Recipe Searching Code, might make the Adv Crafting Table create less of a spike when being used.
[CHANGED] Moved Mineral Water production from Mixer to Injector.
[CHANGED] The Tooltip for contained Materials got a bit slimmed down and more overviewable.
[增加] GT6 Blocks that have Covers on them now have a Tooltip stating that a Crowbar can be used to remove them.
[增加] XP Orbs now get combined if there is more than 32 of them in one World at once. The resulting larger Orb will have the despawn Age of the youngest Orb.
[增加] Ender Garbage Bin (only top side) and Ender Garbage Dump (any side) are now accessible via Funnel/Tap.
[增加] Recipe for Calcium => Calcium Carbonate (Calcite), mixing Water and CO2. It has Hydrogen Gas as a Byproduct.
[增加] Draconium Fluid Pipes. A very high Tier Type of Pipes for people, who have a Draconium Adding Mod installed.
[增加]
More proper Titanium Processing.
The Centrifuging of molten Ilmenite into Rutile and Hematite is no longer possible.
You generally don't need a Crucible to process Titanium containing Ores anymore, except for the final step of shaping the resulting Titanium Dust into whatever you need, like Plates or something.
Instead you need Sulfuric Acid to make Rutile and Green Vitriol.
Rutile (or Ilmenite directly) + Coke + Chlorine + Calcite in Burner Mixer is needed to make it into Titanium Chloride.
Titanium Chloride + Sodium or Magnesium = Titanium + Salt.
This change also fixes the Niobium-Titanium Crucible in the Tech Tree, so that it can be used again to progress.
[增加]
My own Type of 3D Universal Fluid Cells that follows my standard set of Rules for Fluid Containers, and are all stackable up to 64 and Gas Proof.
Since I was not able to settle for a specific Name of them, due to "Cell", "Capsule" and "Container" being already taken by other Mods and "Can" not really fitting the purpose, I decided to go for "Capsule-Cell-Container".
There is 22 different possible Materials they can be made of, which includes Plastic, all the Wax Types and lots of Metals.
1 Unit of the Material it is made of equals 1000L of Fluid. Usually Drums are better, but those can't be made of Wax or Tin.
They can only be made using the Extruder and the Capsule-Cell-Container Shape.
Did I mention that you can paint them too, just like all the other GT6 Containers?



##V6.05.43

[修复] Calcification Display of the Boilers.
[修复] 3 Mixer Recipes missing their Output Fluid.

## V6.05.42

[移除] The GT6 Meta-IC2-Cell-Item, because it won't ever be used anyways (I have a better System for that kinda stuff by now, see Measuring Pots). Also removed some unused Textures aswell.
[移除] Recipe for the Universal Fluid Cell of IC2-Exp. I also replaced the Universal Cell with Empty Cells in Recipes that needed it.
[移除] The "cheaty" Recipes from the Metal Former. The Metal Former itself is still craftable due to compat Reasons.
[CHANGED] IC2-Exp Empty Fuel Rods are now made with Zirconium instead of Steel.
[增加] Plantalyzer, a Machine that scans IC2 Crops and Forestry Saplings, similar to how the Bumblelyzer does it, but it does not use Honey at all.
[增加] Queue Hopper, a Hopper that remembers the order at which things came in, and always emits the first inserted Item and works it's way to the last inserted Item in an ordered fashion. Professionals would call it a FIFO (First IN, First OUT). You can manually change the Order in its GUI ofcourse.
[增加] Glow Glass, a variant of my Clear Glass that emits light like Glowstone. It is produced with the Injector, 1 Glowstone Dust per piece (or half a Glowstone Dust per Slab) and a Block of GT6 Clear Glass. Aside from emitting a constant Light Level this Block uses the same Texture as the normal Clear Glass.
[增加] The Chemical Formula Tooltips back. Now even with Subscript Numbers instead of normal ones!
[增加] Satanic Bumblebees that produce Soul Combs (Soulsand & Soulsand Oil). Spoiler alert do not continue reading if you wanna find out the combo yourself, it is the combination of CITSILIHIN and CINOMED (you have to read those in reverse).
[增加] A Book containing Descriptions of all current GT6 Tools. It is added to all Loot Lists that contain Books of that kind.

## V6.05.41
**##Caution:更新至此版本前务必备份存档！！！！！**
[REWRITE]
The Worldgen Code of GT6 got improved a lot, and that did change quite a lot of internals on how my Worldgen works, including the Config Files. This will also let GalacticGreg crash very hard, due to the massive Changes I made (not that that Addon is needed anymore since I add that Compat myself now).
[兼容] Galacticraft & GalaxySpace
Moon and Mars now have GT6 Rocks in their Worldgen.
Moon, Mars and Asteroids now have GT6 Ores. Mars and Asteroids even have Naquadah and Dilithium related Ores.
Schematics and Keys now go into Book Shelves.
Scanner and Printer can now copy NASA Workbench Schematics, and the Schematics can ofcourse be stored on USB just like Books. This is especially useful in Multiplayer since the NASA Workbench eats those things per Player.
[修复] GT6 Dungeons were spawning in Twilight Forest and on other Planets (now they don't anymore).
[修复] A Bug that caused an exponential Worldgen Loop. I don't know if that Bug was in 6.05.40 already or if it was purely in-Dev, but it's fixed now. (that damn Bug was the reason for wasting a shitload of my time)
[CHANGED] AE Grindstone, because it is way too exploitable to use that thing the way it is (especially because it made Aluminium way too easy if Aluminium Ores are present). I decided to add a lot of Crop related Recipes to it, and kept the Quartz and some low Tier ones, but I removed ALL OTHER RECIPES in it.
[CHANGED] Lead Armors from Thermal Foundation and Galaxy Space now count as Radiation Proof like a Hazmat Suit. (does not apply to IC2 Items that happen to be radioactive)
[CHANGED] The Recipes for dyeing Blocks in the Bath now use less Dye. Using the Spray Cans is still twice as "Dye-Effective" as the Bath.
[IMPROVED] Implemented AEs IMovableTile Interface on my TileEntities. Teleporting them should cause less Issues now.

## V6.05.40

[NOTE] Bear has Advanced Rocketry on his Server, and for some reason it turned off The Galacticraft Oxygen System, as if you have used the Config for that (and that caused by just updating GT6, it even fixes itself if you downgrade GT6). If that happens to you too, make sure to check everything Advanced Rocketry Config related, maybe it somehow gets ignored or corrupted.
[兼容] Galacticraft
Made most GT6 Blocks
Sealable (Bricks, Glass, Concrete, Asphalt, Long Distance Wires, Dry C-Foam etc),
Conditionally Sealable (for Slabs that are only sealable on one side) or
Entirely Unsealable (Stone/Cobblestone/Mossy/Cracked variants of Rock, Wood of any kind, Bales, Wet C-Foam and ALL Machines).
C-Foamed Wires and Pipes will always be sealable. Most Covers that aren't considered simple Attachments can seal things aswell, Canvas is NOT sealable so you need C-Foam behind it, Huge Pipes without C-Foam are NOT sealable either.
[兼容] Galacticraft
I made all shaped Crafting Table Recipes of Galacticraft use Plates (and the different variants of Copper/Iron/Steel) as a potential alternative to the Compressed Items, without messing up OreDict, in order to make Crafting less of a hassle. This does NOT apply to the Recipes inside the NASA Workbench or Machines.
GT6 Batteries are now working to charge Galacticraft things. (I intentionally made GT6 Batteries not chargeable in GC Stuff, so it is one way)
GT6 Wrenches now work on Galacticraft Machines.
GC Machines can now be powered by GT6 EU. I tried my best to make it as lossless as possible, please don't use absurd Voltages like anything past HV.
Bushes do count as Leaves for the Oxygen Collector now.
Desh related Material Data Issues got resolved.
Oxygen Tanks can now be filled in a Canning Machine (Taps on Drums are NOT Canning Machines, I won't make it THAT easy on you!)
Blacklisted Oxygen Canisters for the Tap and some other things! The only GT6 thing that can fill those Canisters now, is the Canning Machine (emptying them via Funnel is no problem).
[修复] All Aluminium Ores now crush into Alumina (and they drop twice as many crushed Ores now), and they cannot be smelted into Aluminium either, so even if someone doesn't disable Aluminium Worldgen from other Mods they still have to go through GT6 Aluminium Processing to make it useful (unless they use other Mods Machines to crush it).
[修复] Low Tier Rotational Pumps were not working at all for some reason.
[修复] GT6 Brown Clay and Mud were preventing Mobspawns ontop of them despite being "natural" Blocks.
[CHANGED] The Wood Plate that is outputted by Recycling Recipes of Vanilla Objects got replaced by the "Generic Wood Plank" Block, so it is placeable now. Also all Planks can now be Crated, not just the Wood Plate ones.
[CHANGED] Made Chisel Purpur Blocks compatible with Et-Futurum Purpur whereever possible, and removed the Chisel Purpur Block Recipe if Et-Futurum is installed.
[CHANGED] Ender Bumblebees now have slightly different requirements if Et-Futurum is installed. They will in that case always require either Chorus Flowers or the Dragon Egg, anything else that they usually accept doesn't count then.

===========================================================分割线=================================================

## v6.05.39

* [修复] 电解机和离心分离机在许多情况下不给含杂粉尘和纯净粉尘提供副产品。
* [修复] 大黄蜂不能再攻击骷髅,因为骷髅是-嗯…骨架。
* [修复] 手钻不使用钢杆(或者铁杆?)来加固砖。
* [修复] 大黄蜂不再在太空(譬如飞船)中生成了。
* [改动] 锤子勘探只消耗以前耐久的1 / 10。
* [新增] 液态氧(与星空兼容)。以及关于它的一个冷冻配方。
* [新增] 现在可以在焊机中制造转子。这也减少了1个螺丝的材料量。
* [新增] 你不需要再把盐和水混合到电解盐水中(但这仍然是可行的)。这两种成分可以直接注入到电解机中,而无需预混合。岩盐(KCl)现在也有用了,在电解机中产出目前还无用的氢氧化钾(KOH)。
* [新增] 混凝土和钢筋混凝土砖块。
  在混凝土上行走时并不能加速,那仍然是沥青的功能。具体的配方是 石头 + 方解石 + 灰烬,然后将产生的粉末与水混合,然后放入烘干机中。它的增强版本需要在烘干机中使用一些铁或钢棒,或者只是使用类似于岩石类型的钻头。混凝土的默认颜色是浅灰色,可以很容易地画出来。与c -泡沫不同的是,它不是预先着色的,但你可以在干块上使用水和染料给它染色,就像沥青一样。它的质地非常光滑,比泡沫塑料更光滑。普通混凝土需要石镐水平,钢筋混凝土需要钻石镐水平,需要4倍的时间来打破它。普通混凝土和钢筋混凝土的防爆阻力为12(16和以上是TNT的威力不能穿透的)。比较:玄武岩= 18(强化后36),c-泡沫=24,黑曜石=36(通过GT6和IC2得到此值),黑色/红色花岗岩= 36(强化后72)。
* [新增] 高压釜,与GT5的略有不同,用大量不锈钢制成。(单方块机器)
  它是由底部的蒸汽直接驱动的,不能加速,因为它是一个以时间计算耗能的机器。
  大多数(或者全部)配方运行时要不间断地使用每秒32mB蒸汽,但对大多数人来说,他们只会制造更强劲的锅炉以即时填补它,所以他们不需要扑灭燃烧室,这也很好。如果人们使用蒸汽储罐,那就不是什么好事情,但幸运的是,在GT6中没有蒸汽储罐这样的东西。:P
  : NaOH处理铝土矿的配方从浸洗机转移到这台机器。
  大多数石英类物质都可以结晶,这也包括琥珀粉,ic2 - exp能量水晶粉(压缩机配方已被移除)和来自AE的石英种子。
* [新增] 燃烧反应器。
  :这是搅拌机的防火版本。它被用来作为燃烧反应的反应容器。它需要一个点火器以及马达/涡轮机来启动。
  :一些作者不曾注意的化学配方被移动到这个燃烧反应器。
  :当作者注意到一些忘记修改的合成的时候,也会有一些被转移到这里。
  :如果你找到了需要燃烧的配方来产出一些东西,请通知作者。(加热不算是燃烧!)
  氢+氧=水确实是燃烧反应,这是一个很好的建议,以备将来参考。


## v6.05.33
* [修复] 僵尸猪人不再会掉落添加到僵尸身上的材料。相反,它们现在掉落一些与地狱相关的材料。
* [改动] 冒险模式斧现在是冒险模式小刀。
* [改动] 装满脏水和海水的木桶可以被潜行右键清空。
* [改动] 现在所有的树的叶子都有快速腐烂的功能。如果需要,它可以在配置中关闭。这使得**快速树叶掉落** *(FastLeafDecay)* 变得毫无价值,因为它现在被集成到GT6中。
* [添加] 僵尸现在也可以掉落普通的小石头,与燧石掉落几率相同。
* [添加] 煤和褐煤石子可以用于制作火把。(之前忘了把它加到更新日志里了)

此线以上转载至function-z的翻译,并由NH4HCr2O7修改
===========================================================分割线================================================





## V6.05.31:
[增加]
A Config to use Electric Cables from GT6 as RF Emitters (1EU:4RF Ratio so it is 1:1). Placing Stuff adjacent to a GT6 Battery Box or Dynamo will work too.
You can power most random RF Mod Stuff with GT6 EU using this Config (but NOT the other way around!). If anyone prefers this kind of Compat over the inbuilt Engine RF Compat, they can turn it on.
Note that it will not convert EU to RF for GT6 Machines that happen to accept RF (such as the RF Converters), unless you have a RF Conductor inbetween. This is because my Stuff always prioritizes my own Interfaces and not the RF ones.


## V6.05.30:
[修复] Basic Machines when they got interrupted, while having the Running Possible Circuit on them, were not restarting as soon as possible, unless you inserted somethign that would match the recipe.
[修复] A ton of Bugs regarding the recharging from IC2 Battery Armor Pieces.
[修复] Several Issues that happened when no version of IC2 was loaded, and reworded the Requirements List on the Download Page to reflect this fix.
[修复] Engines were not working with the Adjacent Machine ON/OFF Functionality.
[CHANGED] Clay Jug and Clay Measuring Pot Recipes now require the Rolling Pin to be made aswell (in order to flatten the Clay easier before shaping it).
[CHANGED] Flint Tools, except for the Pickaxe, the Sword and the Club, can now be made in a 2x2 Grid (I made every Flint Tool only require one Stick/Bone, just like regular GT6 Tools do, since those are also 1xHandle + 1xToolHead)
[CHANGED] Sneaking while rightclicking a Dust Funnel with a Monkey Wrench will now cycle backwards through its Modes.
[增加] Battery Boxes can now finally charge and decharge IC2 Items, I made the Tier conditions very loose, so you can do MV Stuff in LV and vice versa. Note, that Energy and Lapotron Crystals will not work in them and are blacklisted. However the Armor Pieces are not blacklisted.
[增加] Jugs and Measuring Pots can now fill Growthcraft Rice Paddies with Water by clicking the Rice ontop of the Paddy. It will reduce the Water content by up to 70 Liters for a fully dry Paddy.
[增加]
Brown Clay Blocks, aside from being Brown-Orangeish they are almost exactly like normal Clay Blocks.
This variant is slightly different as it contains Potassium instead of Sodium.
The Lithium Content stays the same as the one of regular vanilla Clay.
It is possible to generify any Brown Clay into vanilla Clay, what essentially would be able to turn its Potassium into Sodium, but that would be pointless considering how infinite Sodium is through Ocean Water.
[增加]
Clay "Veins" below Grass in Plains and Savanna alike Biomes (Independant from the Ore Vein Generation Grid).
It will generate 3 times more often with Brown Clay than with Vanilla Clay.
So you can now have large 48m x 48m Clay Mining Pits that are at most 7m deep.
I did this also because Clay is annoying to acquire when digging for it in Water, and because Bricks look nice as Building Material. Also also, Mesas shouldn't be the only Biome where you can get Mass amounts of Clay for Clay Dust.
[增加]
Mud Blocks, which will slow down anyone walking on them and are Spade compatible.
Swampwater will turn all adjacent Dirt or Grass Blocks into Mud Blocks when updated or freshly generated.
You can Plant Sugarcanes on Mud even without an adjacent Water Source.
[增加]
A Prototype for Berry Bushes (Prototype as in no Crossbreeding System what-so-ever for now, they DO Generate).
The one you can get from the Creative Menu does not have a Berry assigned to it, just rightclick the Bush with a Berry of your choice to set it.
There is no benefit in attaching a Berry Bush to another, it just looks better and has a smaller Size, while giving exactly as much as a regular sized Bush.
They will generate in Forests and Plains with random Berry Type.


## V6.05.29:
[修复] Jugs and Measuring Pots crashing when rightclicking a TileEntity while filled with Water and with IC2Classic being installed instead of IC2exp.
[修复] Club did not give Time to Strike Achievement.
[CHANGED] You can now only drink from placed Jugs if you click their Top.
[增加] Jugs, Cups and Measuring Pots now get filled with Water when they are in the Rain.
[增加] Jugs and Measuring Pots can now fill Growthcraft Rice Paddies with Water, and that slightly more efficiently than Buckets, but as a slight downside not in a 3x3 Area.


## V6.05.28:
[NOTE] Before Updating to this Version it is advised to Update to 6.05.26 or 6.05.27 first for making sure the last Slot in the Cutter doesn't get filled with the Fluid Display Item. (I added one more Output Slot to it for the Bark)
[移除] The old 2D Measuring Pot and it's corresponding Item, that I once planned to use more, but that Idea got replaced entirely by 3D Fluid Containers instead.
[CHANGED] Flint Tools can now not only be made with Sticks but also with Bones.
[IMPROVED] Ore Byproduct List in NEI.
[增加] Coal and Graphite Ores can now be bathed in HF to get more Graphite out of them.
[增加] A Ceramic Jug for early drinkable Fluid Storage, that stores up to 2000L (can be filled by clicking Fluid Blocks, but won't place them in World). Also changed the Measuring Pot Recipe to no longer require a Bending Cylinder. Note, that a Jug can contain 2000L of Lava, what is more than a Crucible can hold at once (18 Units overall), so you cannot dump a full Jug into the Crucible.
[增加] A Club (weapon) so that Bear989 can go full Caveman on Mobs with slightly higher Damage than a Sword. It works like a slow Pickaxe too, and it costs 6 Units of Material and crushes Blocks, just like the Hammer.
[增加] Ore Blocks for PFAA Stones, even though GT6 disables Ores per default if PFAA is loaded. It somehow only grabs the 16x16 Textures when copying them. I guess that is some weird PFAA Render thing and therefore not really something to fix on my side without way too much effort.
[增加] Vanilla Furnaces now require some sort of Firestarter in their Recipe to be crafted. (Matches, Flint&Tinder, Flint&Steel, Fire Charges and Lighters work too)
[增加] Cinnamon Tree, that has Cyan Planks. Instead of Bark it drops Cinnamon when being unbarked. The Cinnamon won't regrow though, so you can cut the whole thing down anytime.
[增加] Tree Bark. It can be outputted in half the usual amount by the Cutter when cutting non-debarked Logs, and it counts as a Dust. It can be used for Wood Pellets too.
[增加] Dry Bark Version of the Firestarter. Dry Bark can only be gotten from debarking Dead Logs (which do spawn even in Deserts).
[增加]
Random rotten, dry (dead), mossy and frozen Logs to the Landscape.
They don't count as Logs for the OreDict, but they do have Planks (which do count for OreDict)
3 of them can be made using normal Logs in Machines.
The Mossy ones spawn Mushrooms and Harvestcraft Mushroom Gardens ontop of them. So the original Mushroom Gardens, that don't really generate that nicely looking, could be disabled.
[增加]
Wood Beams for MC, IC2 and GT6 Logs, which are basically just Logs without Bark on them.
Only used in Processing (gives +1 Plank) and as Decoration, not gonna do anything with Physics on them.
They can be made by rightclicking a compatible Log with a Saw, Knife or Axe, the Axe only losing half as much durability as the others.
Works with most Wooden Logs of other Mods, but will only result in a generic looking Wooden Beam (I tried my best to at least let the rotation match after rightclicking).
[增加]
Hydraulic Debarker.
It is debarking Logs to not only get more Bark for your Bite, but also more Wooden Planks from your Logs in the Sawmill.
It does work on all modded Logs too, but will only output a "generic" debarked Log in those cases that will give you a "generic" Wooden Planks Block.
It has a left to right configuration in regards of Input and Output like the Sawmill, while auto-accepting Water from the top and rotation Power from the back.

## v6.05.27
* [改进] 部分沼泽水与海水的生成。并且也修复了新生成的海洋和沼泽群系中的光照问题,因为Minecraft太怠惰了。
* [新增] 沼泽水在干燥器中的配方（比现有任何获取蒸馏水的方法更低效,但这能产生泥土！）
6.05.32:
[修复] Bushes attaching to already attached Bushes, even though I only intended the grounded Bushes to be attached to.
[修复] Juicer voiding excess Fluid if you juice too much Stuff at once.
[修复] Mortar is now also craftable with Steel Ingots, not just Iron Ingots.
[修复] Saplings were not burning as Furnace Fuel. Also fixed several burn Values for Wood related Blocks.
[修复] Exploits regarding Wood and Iron Doors being worth 6 units even though some Mods add the x3 Doors Recipe of future MC Versions, ending up making it worth only 2 Units. I will x3 the Iron Door Recipe too from now on.
[CHANGED] Regular Honey Combs and Wax Combs can now be done via Squeezer, Juicer and Mortar. Not just via Centrifuge. I only do the Forestry-Only Combs as a Centrifuge exclusive, because their thing is a Centrifuge aswell.
[IMPROVED] Juices (but not Smoothies) have more Food Value now, so they are a bit more worth it.
[增加] AE Presses can be made from Scratch using the Tier 3 Laser Engraver, making it more possible to disable those annoying AE Meteorites.
[增加] Horses, Donkeys and Mules now drop Meat when killed. They will also drop more Meat if they have good Jump or Health Stats. (I intentionally left out the Speed Stat, because it's not variable for Donkeys and Mules)
[增加] Zombies now have the following additional Drops when killed by a Player (Looting does not affect these chances): 25% Flint; 20% Stick; 10% Mud Ball; 5% Matches;
[增加]
Compass that actually points towards North.
It even has a few Modes, like pointing into the direction that you Face like on a Map (aka inverse North) or pointing to Spawn like the vanilla Compass.
Even to your latest Death Point, if you don't quit the Game like a whiny Ragequitter. Relogging without entirely closing the Client won't delete that Point.
All Compass Modes aside from the North Mode are hidden from NEI.
[增加]
Tiny Rocks that are spread over most Biomes. Their worth is 0.25 Units of Material. (also ofcourse I got that Idea from Terrafirmacraft)
They can indicate that there is a Large Ore Vein up to 25 Blocks below the Ground in a closeby Chunk, if the Rocks themselves contain a certain Ore.
Some Rocks are also dropping Flint, that can be used for Flint Tools. There is a 1 in 32 chance that the Flint will be a Meteoric Iron Rock instead (I also tweaked Meteoric Iron and Meteoric Steel).
Other will just be literal Rocks that can be used for some early Tools but not for Swords or Knifes. They can also be crafted into Cobblestone Blocks if you got 4 of them.
The Coal Variants can be burned in a Furnace too, if you desire to use them that way.
It should be possible to find those Rocks in the Nether and the End aswell, just not that abundantly.
Rightclicking will directly insert the Rock into your Inventory, but I would use a Fortune Pickaxe on it instead.

## v6.05.26
* [修复] 关于GT地牢的光照问题。
* [移除] 移除 **实用拓展** *(Actually Additions)* 的发酵桶配方,因为油的来源没那么简单。
* [移除] 移除Dropbox链接。
* [改动] 将锤子探矿所勘探的样品翻倍。
* [改动] 现在制作冰淇淋需要牛奶,另新增蜂蜜冰淇淋。
* [改进] GT地牢中的地狱门房间会生成一些火柴等与地狱相关的物品,同时左右双方还会生成地狱疣农场。
* [改进] GT地牢中的工作室会有一个一定生成所有GT说明书的书架。
* [新增] 第五个健康指标：血脂。高血脂会导致心脏病突发(譬如连吃两块黄油)。
* [新增] 当加载 **暮色森林** *(Twilight Forest)* 且此地牢已经生成一个末地门房间或地狱门房间时,GT地牢中会生成一个通向暮色森林的传送门(传送门未打开)房间,此房间会生成一个含一颗钻石,16个活根和一本暮色森林手册(为不会扔钻石的萌新准备)的箱子。
* [新增] GT地牢会生成一个 **Mystcraft** 图书馆,只会在此地牢生成末地门房间时生成,会有一个Mystcraft传送门。
* [新增] 脏水,会在沼泽生成,与海水十分相似,但不会向四周蔓延,且能制成脏水瓶和脏水桶。
* [新增] ☆★☆(重点)大理石、闪长岩、花岗岩、采掘砖块等会生成GT矿石,**凿子2** *(Chisel)* **把未来带回现实** *(Et Futurum)* 以及 **铁路** *(Railcraft)* 再也不会吞矿脉辣
* [新增] 药瓶,能够在任何时候饮用,回复20心,消耗10饥饿值/饱和度（饥饿buff）

## v6.05.25
* [兼容] GT6的铲子在农田中可以像普通的铲子一样放置水稻田了,并且也可以用GT6的木桶为其供水。（显然这是做得到的事情）
* [修复] 气体燃烧室不再拥有相邻的开/关特性,作者之前一直忘记改这玩意了。
* [改动] 你可以用木桶装蒸馏水了,然而这么做会让蒸馏水变回普通水。


## v6.05.24
* [兼容] 更好地支持了 **生长工艺** *(Growthcraft)* 模组的社区版本。例如它的竹子可以用在焦炉里面了（我因同样的理由为 **超多生态群系** *(Biomes O' Plenty)* 也增加了相同的配方）。
* [修复] 修复了MV和HV电锯砍树时消耗太多能量到呃问题。
* [修复] Control and Detector Covers which are placed on Universal Extenders which are placed on formed Multiblock Parts were not working, because the Multiblock Part didn't implement the Interface for that.
* [修复] 多功能离心机底部贴图已经按Z轴镜像旋转。
* [修复] A Bug where Supporter Certificates were not given to people, who had a full Inventory at the time they were supposed to receive it, it will now wait until there is a Slot free for the Certificate to spawn in. You can delete "gregtech/certificates.support.dat" from your Save File if you want to reset the "already given" status for all Players.
* [修复] Oceanwater Block Render Issues with all the things (namely Underwater Plants), because Forge AGAIN royally fucked up the Logic behind certain checks, such as "shouldSideBeRendered" where it first checks "if (Block is not this) then abort checks" before performing the checks for "all the non-this blocks that could be there", resulting in absolute failure. Sadly I cannot fix that in other Mods, that add Fluids.
* [修复] Honey, again... Apparently there are now THREE fucking kinds of Honey in MC: Forestry Honey because they wanted to be different and chose to change it's name to "for.honey" (that was ages ago, but is still annoying as fuck), Biomes O'Plenty Honey because it uses the proper name that Forestry used originally ("honey"), and GrowthCraft Honey that wanted to be EXTRA SPECIAL and chose "grc.honey", because we obviously "don't" get serious compatibility problems, when there is multiple different kinds of Honey...
* [修复] Milk, for the same reason as Honey, since GrowthCraft wanted to be SPECIAL and chose "grc.milk", while Forestry and MFR used "milk"...
* [修复] Transformers and Battery Boxes turning on/off due to adjacent Machines auto-turning on/off when active/inactive.
* [修复] IC2 Machines not exploding when being overvolted by a GT Energy Emitter. Note, that it uses the GregTech Tiers of Voltage, so 64 EU/t is still fine for a 32 EU/t Machine, while 65 EU/t would blow it up for example.
* [改动] GT6 Chocolate Bars can now be fed to Pets. I don't say it's a good Idea, I just say it is possible now, unless you have Actually Additions installed where I have to default Unification to its Chocolate Bar.
* [新增] Printer Recipes for Forestry Stamps and Letters. They are overall cheaper than the Crafting/Carpenter Recipes. Also some of them enable different Materials to be used, such as Silver, Zinc, Bismuth or Lead. It does check if the Stamp is even craftable before adding the Recipe. (Forestry disables 20n, 50n and 100n Stamps by default, because anything above 10n is useless in gameplay, but if they are enabled they will have Recipes)
* [新增] Butter and Salted Butter. Currently a Mixing Bowl and Centrifuge Recipe with Heavy Cream.
* [新增] 现在需要蒸馏新增的甜菜汁而不是甜菜才能制糖。
* [新增]
  White and Red Grapes, with Crops, Juices, Smoothies, Wines and everything, simply because Growthcraft has Red Grapes and I only had Green and Purple. (also updated the Raisin Cookie/Dough Textures to reflect this colorful addition)
  Now Growthcrafts Grape Juice is the Purple one, Binnies old Grape Juices are Red and White, while the Green Grape Juice/Smoothie/Wine is just a GT6 thing now.
  Also Purple Grape Juice now turns into Ricardo Sanchez, what is a Wine that is named very similarily to a character in Rick&Morty. I got that Idea, because I literally saw a Bottle of it at home. (because people are gifting random Bottles of Alcohol to others during Holidays, that no one ever drinks, or that just get re-gifted)
* [新增]
  It was time that those get a bit updated, so GT6 Dungeons now spawn with the following Stuff:
  Colored Porcellain Cups and Coins in the Barracks and Libraries*, some of the Cups even being filled with a random Drink. (* = only with the Thaumcraft Library Design, Cups in any Library Design always have stretched Night Vision Potions, because that makes total sense, being a place where you need your eyes to read stuff)
  A new un-lit Nether Portal Room, similar to the already existing End Portal Room. (Does not always have to generate)
  The Crate Room now also contains Barrels and Drums with useful raw Materials (including Stainless Drums full of different kinds of Raw Oil).
  A Room with a Pool and random Glowtus Pads in it, which can contain up to 4 Chests with the Bonus Chest Loot.
  Barrels full of some randomly selected Drink for the Default Rooms. They can be Ironwood Barrels 33.3% of the time, and Purple Drink is the most likely Stuff contained in them compared to the others.
  A WaterDrum+Taps+Funnel+MixingBowl+Cauldron+BathingPot-Setup for the Default Rooms.
  A Corner to the Default Room, where there is the Safe, 3 Chests, a Crafting Table, a Mortar, some Coins, a Measuring Pot, an Advanced Crafting Table and 2 Mass Storages, which contain the Cobblestone Variant of the 2 Blocks that the Structure is made of (in order to make it easier to expand the Area)
  The T-Intersections in Corridors now have a few Coins and a Cup with a random Drink.


## v6.05.23

* [兼容] 增加对 **实用拓展** *(Actually Additions)* 物品的支持：6种晶体已有对应的矿石,也可以在物质复制机使用特殊合成表获得。
* [兼容] 现已支持林业扩展 *Binnie's Mod* 的pre-15版本,但不建议升级至该版本,除非你已经阅读了其更新日志并决定升级。你也可以使用Binnie-Patcher并停留在pre-14版本,因为pre-15移除了大量物品,例如所有的饮料。作者将会尽量支持两种版本。
* [兼容] 更好地支持了 **更多武器** *(Balkon's Weapon Mod)* 模组。
* [修复] 鲜奶油和椰奶油可以在GT搅拌盆使用防腐木棍制作（木棍不会被消耗）。
* [修复] 移除了将镀锌钢等镀件的锭削成棒的不合理合成表。
* [改动] 提升了GT6炉的工作速度并加工单位过程内消耗的HU从400减至256。
* [改动] 扫描仪将给出所点击方块更详尽的数据。
* [改动] 调试工具 *(Debug Items)* 将不能被非创造模式下的玩家或者自动化工具（例如漏斗）从GT6方块中提取出来或随之消失而掉落。
* [新增] 添加了黑麦、燕麦、大麦和水稻对应的作物和谷物垛。这些谷物垛在世界中正如普通小麦垛一样不会腐烂,所以可以安全地将其用于装饰。
* [新增] 草垛会在提示中显示其是否已经干燥。

## v6.05.22
* [兼容] 兼容了  **把未来带回现实** *(Et Futurum)* 的物品,例如可以使用GT6的铲子在草地上生成道路及其他一小部分合成表。
* [修复] 修复了与 **双重快捷栏** *(Dual-Hotbars)* 的一个冲突。
* [修复] 修复了太小的能量包既不会被接受也不会消失、最终导致有时卡在变压器的问题。
* [修复] 修复了由于作物扫描器覆盖了所有行为而导致的通常和调试扫描器不扫描作物以外物品的问题。

## v6.05.21
* [兼容] 增加对 **实用拓展** *(Actually Additions)* 物品的支持。
* [兼容] 增加对 **大型反应堆** *(Big Reactors)* 物品的支持以及类似于铀和沥青铀矿处理链的合成表。
* [修复] 修复了坩埚温度的问题：当向坩埚里加入温度高于坩埚熔点的物体时,坩埚温度不再会升至该物体温度,这使得制作黑曜石工具需要燃烧室或加热器。
* [修复] GT树叶现在遵循流畅图像品质了。
* [修复] 右键能放置火把的工具（例如镐子、铲子、钻头）现在可以放置 **星系** *(GalactiCraft)* 模组中的萤石火把了。
* [改动] 如果安装了**实用拓展** *(Actually Additions)* 模组,IC2咖啡作物会改用该模组的咖啡豆。
* [改动] 改动了花生酱配方,因此花生在两种榨汁机中又会产出坚果油了。
* [新增] 地下生物群系的石头现在能泛型化地使用普通石头和原石了。（译注：即类似矿物使用空矿石+元数据区分矿物类型的方法）
* [新增] 装箱机现在能制作废料箱,拆箱机在NEI中也有了一个拆箱的伪合成表。
* [新增] 大型蒸汽涡轮现在可以从正面9个方块接受蒸汽,包括这些方块的侧面。这意味着你可以摆放成将蒸汽涡轮可见的样子。（注1：作者仍没有做好涡轮的正确材质）（注2：这个改动不会影响蒸馏水输出或者任何已经存在或展示场合的配置）
* [新增] 现在可以从除菌丝以外的任何土中筛滤出 **海洋物语** *(Mariculture)* 中的鱼饵。
* [新增] 重新添加了便携式扫描仪（针对作物）和调试扫描仪（无限能量）。
* [新增] 添加了便携式作物扫描仪,比便携式扫描仪便宜但是只能扫描IC2作物。
* [新增] 添加了电动修剪器,类似电动剪枝器。
* [新增] 普通炼药锅现在能通过水龙头填满。
* [新增] 能精确采集草方块、菌丝、粘土块和灰化土的铲子,这些铲子也在采集沙子和泥土材质的方块方面比普通铲子快。

## v6.05.12

* 修复了某坚果从任何树叶掉落的bug
* 加入空木箱,功能类似木板
