更新日志 *(1.7.10)*

## V6.05.45

[FIXED] Aqua Regia to Chloroplatinic Acid Processing producing a very unbalanced output (more Cl out than you put in), I only needed to change up the Ratios, it's the same Products as before.
[FIXED] Some Bugs regarding the Player Inventory restock from the Slot above Functionality of GT6 in regards of GT6 Tools and their Scrap.
[CHANGED] Tin Alloy counts as Furnace Smeltable now.
[CHANGED] Neodymium and its Magnetic variant are now Diamond-Tool Quality.
[CAHNGED] Bushes now grow 5 times slower. They were just too OP.
[ADDED] A dedicated Loot Chest for the Dungeon Loot change in the previous Version. Now it is no longer made of Tin Alloy, but instead is not Craftable and made of Stone and looking a bit like Mossy Stone Bricks.
[ADDED] Cobalt, Nickel, Germanium and Draconium "Storage Set" (Chests, Mass Storages, Shelves, Adv Crafting Tables, Hoppers etc). Also made it easier for me to add more "Storage Sets" by rewriting the Code a little.
[ADDED] A few Recipes regarding BoP Mud and GT6 Mud.
[ADDED] Tin Alloy Fluid Pipes.
[ADDED] Mud Version of GT6 Ores to fit in better with the muddy Swampwater of GT6. (SERIOUSLY, IT'S LIKE SAND ORES, OR NETHERRACK ORES, JUST THAT IT BELONGS TO MUDDY WATER IN NEWLY GENERATED SWAMPS!!! WHY THE FUCK IS EVERYBODY HYPED ABOUT THIS?!?)
[ADDED]
Some Tools will now autocollect their Drops instead of letting Item Entities fall on the ground, if the Player has enough Inventory Space.
This also applies to certain Materials you can craft Tools out of. You know, the "Magnetic" Variant.
Amoung those Tools (its about half of ALL Tools that can do that) is the Wrench for example, meaning you autocollect whatever you Wrench, no matter what Material the Wrench is.
That kindof fixed the Issue of "Removing Hoppers above a Crucible" as a Side Effect, since the Hopper would not Drop as Item in this case (If you have Space in your Inventory).
As Examples, here are a few Tools that Automatically have this Ability even without being Magnetic: Construction Pickaxes, Wrenches, Mining Drills and the Plow.
[ADDED]
Made several Extruder Recipes accessible much earlier.
The Tier 1 Extruder no longer needs Tungsten Carbide to be crafted, instead it uses Steel.
New Low Heat Extruder Shapes can be made using any Type of regular Steel.
Several Low Tier Metals count as Simple for the Extruder now, meaning they have a fixed low cost and can be formed using the Low Heat Shapes.

## V6.05.44

[NOTE] Users of the Custom Veins etc in my Worldgen Config have to manually set the amount of Custom Veins, as it no longer defaults to 8, in order to prevent Debug Error Messages from appearing in the Log (due to NULL Material in Config). And yes the Debug Errors about Worldgen Ores are for Users, not for me, and they are in the GregTech.log
[FIXED] A HUGE Maths Error in the Extruder Recipe Code. It used about 10 times more Energy in some cases than it should have used (all the Metal related Recipes basically). Now it will just use 25% more Energy than a Crucible would.
[FIXED] A Stupid Error in the Extruder Recipe Code that made Wax, Plastic and Rubber Stuff cost exactly the same no matter how many Items the Recipe Outputs.
[FIXED] Fluid Filters resetting again.
[CHANGED] Dungeon Loot Chests will now be replaced with GT6 Chests that only generate their Loot once you open or break them and not before that.
[CHANGED] A tiny thing in the Crafting Recipe Searching Code, might make the Adv Crafting Table create less of a spike when being used.
[CHANGED] Moved Mineral Water production from Mixer to Injector.
[CHANGED] The Tooltip for contained Materials got a bit slimmed down and more overviewable.
[ADDED] GT6 Blocks that have Covers on them now have a Tooltip stating that a Crowbar can be used to remove them.
[ADDED] XP Orbs now get combined if there is more than 32 of them in one World at once. The resulting larger Orb will have the despawn Age of the youngest Orb.
[ADDED] Ender Garbage Bin (only top side) and Ender Garbage Dump (any side) are now accessible via Funnel/Tap.
[ADDED] Recipe for Calcium => Calcium Carbonate (Calcite), mixing Water and CO2. It has Hydrogen Gas as a Byproduct.
[ADDED] Draconium Fluid Pipes. A very high Tier Type of Pipes for people, who have a Draconium Adding Mod installed.
[ADDED]
More proper Titanium Processing.
The Centrifuging of molten Ilmenite into Rutile and Hematite is no longer possible.
You generally don't need a Crucible to process Titanium containing Ores anymore, except for the final step of shaping the resulting Titanium Dust into whatever you need, like Plates or something.
Instead you need Sulfuric Acid to make Rutile and Green Vitriol.
Rutile (or Ilmenite directly) + Coke + Chlorine + Calcite in Burner Mixer is needed to make it into Titanium Chloride.
Titanium Chloride + Sodium or Magnesium = Titanium + Salt.
This change also fixes the Niobium-Titanium Crucible in the Tech Tree, so that it can be used again to progress.
[ADDED]
My own Type of 3D Universal Fluid Cells that follows my standard set of Rules for Fluid Containers, and are all stackable up to 64 and Gas Proof.
Since I was not able to settle for a specific Name of them, due to "Cell", "Capsule" and "Container" being already taken by other Mods and "Can" not really fitting the purpose, I decided to go for "Capsule-Cell-Container".
There is 22 different possible Materials they can be made of, which includes Plastic, all the Wax Types and lots of Metals.
1 Unit of the Material it is made of equals 1000L of Fluid. Usually Drums are better, but those can't be made of Wax or Tin.
They can only be made using the Extruder and the Capsule-Cell-Container Shape.
Did I mention that you can paint them too, just like all the other GT6 Containers?



##V6.05.43

[FIXED] Calcification Display of the Boilers.
[FIXED] 3 Mixer Recipes missing their Output Fluid.

## V6.05.42

[REMOVED] The GT6 Meta-IC2-Cell-Item, because it won't ever be used anyways (I have a better System for that kinda stuff by now, see Measuring Pots). Also removed some unused Textures aswell.
[REMOVED] Recipe for the Universal Fluid Cell of IC2-Exp. I also replaced the Universal Cell with Empty Cells in Recipes that needed it.
[REMOVED] The "cheaty" Recipes from the Metal Former. The Metal Former itself is still craftable due to compat Reasons.
[CHANGED] IC2-Exp Empty Fuel Rods are now made with Zirconium instead of Steel.
[ADDED] Plantalyzer, a Machine that scans IC2 Crops and Forestry Saplings, similar to how the Bumblelyzer does it, but it does not use Honey at all.
[ADDED] Queue Hopper, a Hopper that remembers the order at which things came in, and always emits the first inserted Item and works it's way to the last inserted Item in an ordered fashion. Professionals would call it a FIFO (First IN, First OUT). You can manually change the Order in its GUI ofcourse.
[ADDED] Glow Glass, a variant of my Clear Glass that emits light like Glowstone. It is produced with the Injector, 1 Glowstone Dust per piece (or half a Glowstone Dust per Slab) and a Block of GT6 Clear Glass. Aside from emitting a constant Light Level this Block uses the same Texture as the normal Clear Glass.
[ADDED] The Chemical Formula Tooltips back. Now even with Subscript Numbers instead of normal ones!
[ADDED] Satanic Bumblebees that produce Soul Combs (Soulsand & Soulsand Oil). Spoiler alert do not continue reading if you wanna find out the combo yourself, it is the combination of CITSILIHIN and CINOMED (you have to read those in reverse).
[ADDED] A Book containing Descriptions of all current GT6 Tools. It is added to all Loot Lists that contain Books of that kind.

## V6.05.41

[REWRITE]
The Worldgen Code of GT6 got improved a lot, and that did change quite a lot of internals on how my Worldgen works, including the Config Files. This will also let GalacticGreg crash very hard, due to the massive Changes I made (not that that Addon is needed anymore since I add that Compat myself now).
[COMPAT] Galacticraft & GalaxySpace
Moon and Mars now have GT6 Rocks in their Worldgen.
Moon, Mars and Asteroids now have GT6 Ores. Mars and Asteroids even have Naquadah and Dilithium related Ores.
Schematics and Keys now go into Book Shelves.
Scanner and Printer can now copy NASA Workbench Schematics, and the Schematics can ofcourse be stored on USB just like Books. This is especially useful in Multiplayer since the NASA Workbench eats those things per Player.
[FIXED] GT6 Dungeons were spawning in Twilight Forest and on other Planets (now they don't anymore).
[FIXED] A Bug that caused an exponential Worldgen Loop. I don't know if that Bug was in 6.05.40 already or if it was purely in-Dev, but it's fixed now. (that damn Bug was the reason for wasting a shitload of my time)
[CHANGED] AE Grindstone, because it is way too exploitable to use that thing the way it is (especially because it made Aluminium way too easy if Aluminium Ores are present). I decided to add a lot of Crop related Recipes to it, and kept the Quartz and some low Tier ones, but I removed ALL OTHER RECIPES in it.
[CHANGED] Lead Armors from Thermal Foundation and Galaxy Space now count as Radiation Proof like a Hazmat Suit. (does not apply to IC2 Items that happen to be radioactive)
[CHANGED] The Recipes for dyeing Blocks in the Bath now use less Dye. Using the Spray Cans is still twice as "Dye-Effective" as the Bath.
[IMPROVED] Implemented AEs IMovableTile Interface on my TileEntities. Teleporting them should cause less Issues now.

## V6.05.40

[NOTE] Bear has Advanced Rocketry on his Server, and for some reason it turned off The Galacticraft Oxygen System, as if you have used the Config for that (and that caused by just updating GT6, it even fixes itself if you downgrade GT6). If that happens to you too, make sure to check everything Advanced Rocketry Config related, maybe it somehow gets ignored or corrupted.
[COMPAT] Galacticraft
Made most GT6 Blocks
Sealable (Bricks, Glass, Concrete, Asphalt, Long Distance Wires, Dry C-Foam etc),
Conditionally Sealable (for Slabs that are only sealable on one side) or
Entirely Unsealable (Stone/Cobblestone/Mossy/Cracked variants of Rock, Wood of any kind, Bales, Wet C-Foam and ALL Machines).
C-Foamed Wires and Pipes will always be sealable. Most Covers that aren't considered simple Attachments can seal things aswell, Canvas is NOT sealable so you need C-Foam behind it, Huge Pipes without C-Foam are NOT sealable either.
[COMPAT] Galacticraft
I made all shaped Crafting Table Recipes of Galacticraft use Plates (and the different variants of Copper/Iron/Steel) as a potential alternative to the Compressed Items, without messing up OreDict, in order to make Crafting less of a hassle. This does NOT apply to the Recipes inside the NASA Workbench or Machines.
GT6 Batteries are now working to charge Galacticraft things. (I intentionally made GT6 Batteries not chargeable in GC Stuff, so it is one way)
GT6 Wrenches now work on Galacticraft Machines.
GC Machines can now be powered by GT6 EU. I tried my best to make it as lossless as possible, please don't use absurd Voltages like anything past HV.
Bushes do count as Leaves for the Oxygen Collector now.
Desh related Material Data Issues got resolved.
Oxygen Tanks can now be filled in a Canning Machine (Taps on Drums are NOT Canning Machines, I won't make it THAT easy on you!)
Blacklisted Oxygen Canisters for the Tap and some other things! The only GT6 thing that can fill those Canisters now, is the Canning Machine (emptying them via Funnel is no problem).
[FIXED] All Aluminium Ores now crush into Alumina (and they drop twice as many crushed Ores now), and they cannot be smelted into Aluminium either, so even if someone doesn't disable Aluminium Worldgen from other Mods they still have to go through GT6 Aluminium Processing to make it useful (unless they use other Mods Machines to crush it).
[FIXED] Low Tier Rotational Pumps were not working at all for some reason.
[FIXED] GT6 Brown Clay and Mud were preventing Mobspawns ontop of them despite being "natural" Blocks.
[CHANGED] The Wood Plate that is outputted by Recycling Recipes of Vanilla Objects got replaced by the "Generic Wood Plank" Block, so it is placeable now. Also all Planks can now be Crated, not just the Wood Plate ones.
[CHANGED] Made Chisel Purpur Blocks compatible with Et-Futurum Purpur whereever possible, and removed the Chisel Purpur Block Recipe if Et-Futurum is installed.
[CHANGED] Ender Bumblebees now have slightly different requirements if Et-Futurum is installed. They will in that case always require either Chorus Flowers or the Dragon Egg, anything else that they usually accept doesn't count then.



## v6.05.39

* [修复] 电解机和离心分离机在许多情况下不给含杂粉尘和纯净粉尘提供副产品。
* [修复] 大黄蜂不能再攻击骷髅，因为骷髅是-嗯…骨架。
* [修复] 手钻不使用钢杆(或者是铁杆?好吧，反正其中一个没有正确地工作)来加固砖。
* [修复] 大黄蜂不再在太空中产卵了(银河战舰等)。
* [改动] 锤子勘探只消耗以前耐久的1 / 10。
* [新增] 液态氧(与星空兼容)。为此还有一个冷冻配方。
* [新增] 现在可以在焊机中制造转子。这也减少了他们1个螺丝的回收材料量。
* [新增] 你不需要再把盐和水混合到电解盐水中(但这仍然是可行的)。这两种成分可以直接注入到电解机中，而无需预混合。岩盐(KCl)现在也有用了，在电解机中产出目前还无用的KOH。
* [新增] 混凝土和钢筋混凝土砌块。
  混凝土没有行走加速，那仍然是沥青的工作。具体的配方是 石头 + 方解石 + 灰烬，然后将产生的粉末与水混合，然后放入烘干机中。它的增强型需要在烘干机中使用一些铁或钢棒，或者只是使用类似于岩石类型的钻头。混凝土的默认颜色是浅灰色，可以很容易地画出来。与c -泡沫不同的是，它不是预先着色的，但你可以在干块上使用水和染料给它染色，就像沥青一样。它的质地非常光滑，比泡沫塑料更光滑。普通混凝土需要石镐水平，钢筋混凝土需要钻石镐水平，需要4倍的时间来打破它。普通混凝土和钢筋混凝土的防爆阻力为12(16和以上是TNT的威力不能穿透的)。比较:玄武岩= 18(强化后36)，c-泡沫=24，黑曜石=36(通过GT6和IC2得到此值)，黑色/红色花岗岩= 36(强化后72)。
* [新增] 高压锅，这一次与旧的略有不同，用大量不锈钢制成。(仍然是单步运行)
  它是由底部的蒸汽直接驱动的，是一个不能加速的过程，因为它是一个基于时间的机器。
  大多数(如果不是全部的话)配方运行时要不间断地使用每秒32蒸汽能，但知道大多数人来说，他们只会拍一个更强大的锅炉，以即时填补它，所以他们不需要考虑及时扑灭燃烧室，这也很好。如果人们使用蒸汽箱，那将不会是什么好事情，但幸运的是，在GT6中没有这样的东西。:P
  : 与NaOH的铝土矿处理从浸洗机(原文bath，我也不知道是不是这么翻译)进入这台机器。
  大多数石英类似物质都可以结晶，这也包括琥珀尘埃，ic2 - exp能量尘埃(有这东西？)(压缩配方现在被移除)和来自应用能源的石英种子。
* [新增] 燃烧混合器。
  :这是混合器的防火变体。它被用来尽可能快地燃烧混合的结果。它需要一个点火器启动这个混合器，以及常用的马达/涡轮机。
  :一些我曾不常注意的化学配方将被移到这个混合器。
  :一旦我注意到一些合成我忘记移动它们的时候，也会有一些被移到这里。
  :如果你找到了需要燃烧的配方来产出一些东西，请通知我。(加热不算是燃烧!)
  氢+氧=水确实是燃烧的，这是一个很好的建议，以备将来参考。


## v6.05.33
* [修复] 僵尸猪人不再会掉落我添加到僵尸身上的材料。相反，他们现在掉落更多不同的与地狱相关的材料。
* [改动] 冒险模式斧现在是冒险模式刀。
* [改动] 充满脏水和海水的木桶可以被偷偷的右键清空。
* [改动] 现在所有的树的叶子都有快速腐烂的功能。如果需要，它可以在配置中关闭。这使得快速的叶子腐烂变得毫无价值，因为它现在被集成到GT6中。
* [添加] 僵尸现在也可以掉落普通的小石头，与燧石掉落几率相同。
* [添加] 顺带一提，煤和褐煤可以用于点火。(之前忘了把它加到更新日志里了)

## v6.05.27
* [改进] 部分沼泽水与海水的生成。并且也修复了新生成的海洋和沼泽群系中的光照问题，因为Minecraft太怠惰了。
* [新增] 沼泽水在干燥器中的配方（比现有任何获取蒸馏水的方法更低效，但这能产生泥土！）

## v6.05.26
* [修复] 关于GT地牢的光照问题。
* [移除] 移除 **实用拓展** *(Actually Additions)* 的发酵桶配方，因为油的来源没那么简单。
* [移除] 移除Dropbox链接。
* [改动] 将锤子探矿所勘探的样品翻倍。
* [改动] 现在制作冰淇淋需要牛奶，另新增蜂蜜冰淇淋。
* [改进] GT地牢中的地狱门房间会生成一些火柴等与地狱相关的物品，同时左右双方还会生成地狱疣农场。
* [改进] GT地牢中的工作室会有一个一定生成所有GT说明书的书架。
* [新增] 第五个健康指标：血脂。高血脂会导致心脏病突发(譬如连吃两块黄油)。
* [新增] 当加载 **暮色森林** *(Twilight Forest)* 且此地牢已经生成一个末地门房间或地狱门房间时，GT地牢中会生成一个通向暮色森林的传送门(传送门未打开)房间，此房间会生成一个含一颗钻石，16个活根和一本暮色森林手册(为不会扔钻石的萌新准备)的箱子。
* [新增] GT地牢会生成一个 **Mystcraft** 图书馆，只会在此地牢生成末地门房间时生成，会有一个Mystcraft传送门。
* [新增] 脏水，会在沼泽生成，与海水十分相似，但不会向四周蔓延，且能制成脏水瓶和脏水桶。
* [新增] ☆★☆(重点)大理石、闪长岩、花岗岩、采掘砖块等会生成GT矿石，**凿子2** *(Chisel)* **把未来带回现实** *(Et Futurum)* 以及 **铁路** *(Railcraft)* 再也不会吞矿脉辣
* [新增] 药瓶，能够在任何时候饮用，回复20心，消耗10饥饿值/饱和度（饥饿buff）

## v6.05.25
* [兼容] GT6的铲子在农田中可以像普通的铲子一样放置水稻田了，并且也可以用GT6的木桶为其供水。（显然这是做得到的事情）
* [修复] 气体燃烧室不再拥有相邻的开/关特性，作者之前一直忘记改这玩意了。
* [改动] 你可以用木桶装蒸馏水了，然而这么做会让蒸馏水变回普通水。


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

* [兼容] 增加对 **实用拓展** *(Actually Additions)* 物品的支持：6种晶体已有对应的矿石，也可以在物质复制机使用特殊合成表获得。
* [兼容] 现已支持林业扩展 *Binnie's Mod* 的pre-15版本，但不建议升级至该版本，除非你已经阅读了其更新日志并决定升级。你也可以使用Binnie-Patcher并停留在pre-14版本，因为pre-15移除了大量物品，例如所有的饮料。作者将会尽量支持两种版本。
* [兼容] 更好地支持了 **更多武器** *(Balkon's Weapon Mod)* 模组。
* [修复] 鲜奶油和椰奶油可以在GT搅拌盆使用防腐木棍制作（木棍不会被消耗）。
* [修复] 移除了将镀锌钢等镀件的锭削成棒的不合理合成表。
* [改动] 提升了GT6炉的工作速度并加工单位过程内消耗的HU从400减至256。
* [改动] 扫描仪将给出所点击方块更详尽的数据。
* [改动] 调试工具 *(Debug Items)* 将不能被非创造模式下的玩家或者自动化工具（例如漏斗）从GT6方块中提取出来或随之消失而掉落。
* [新增] 添加了黑麦、燕麦、大麦和水稻对应的作物和谷物垛。这些谷物垛在世界中正如普通小麦垛一样不会腐烂，所以可以安全地将其用于装饰。
* [新增] 草垛会在提示中显示其是否已经干燥。

## v6.05.22
* [兼容] 兼容了  **把未来带回现实** *(Et Futurum)* 的物品，例如可以使用GT6的铲子在草地上生成道路及其他一小部分合成表。
* [修复] 修复了与 **双重快捷栏** *(Dual-Hotbars)* 的一个冲突。
* [修复] 修复了太小的能量包既不会被接受也不会消失、最终导致有时卡在变压器的问题。
* [修复] 修复了由于作物扫描器覆盖了所有行为而导致的通常和调试扫描器不扫描作物以外物品的问题。

## v6.05.21
* [兼容] 增加对 **实用拓展** *(Actually Additions)* 物品的支持。
* [兼容] 增加对 **大型反应堆** *(Big Reactors)* 物品的支持以及类似于铀和沥青铀矿处理链的合成表。
* [修复] 修复了坩埚温度的问题：当向坩埚里加入温度高于坩埚熔点的物体时，坩埚温度不再会升至该物体温度，这使得制作黑曜石工具需要燃烧室或加热器。
* [修复] GT树叶现在遵循流畅图像品质了。
* [修复] 右键能放置火把的工具（例如镐子、铲子、钻头）现在可以放置 **星系** *(GalactiCraft)* 模组中的萤石火把了。
* [改动] 如果安装了**实用拓展** *(Actually Additions)* 模组，IC2咖啡作物会改用该模组的咖啡豆。
* [改动] 改动了花生酱配方，因此花生在两种榨汁机中又会产出坚果油了。
* [新增] 地下生物群系的石头现在能泛型化地使用普通石头和原石了。（译注：即类似矿物使用空矿石+元数据区分矿物类型的方法）
* [新增] 装箱机现在能制作废料箱，拆箱机在NEI中也有了一个拆箱的伪合成表。
* [新增] 大型蒸汽涡轮现在可以从正面9个方块接受蒸汽，包括这些方块的侧面。这意味着你可以摆放成将蒸汽涡轮可见的样子。（注1：作者仍没有做好涡轮的正确材质）（注2：这个改动不会影响蒸馏水输出或者任何已经存在或展示场合的配置）
* [新增] 现在可以从除菌丝以外的任何土中筛滤出 **海洋物语** *(Mariculture)* 中的鱼饵。
* [新增] 重新添加了便携式扫描仪（针对作物）和调试扫描仪（无限能量）。
* [新增] 添加了便携式作物扫描仪，比便携式扫描仪便宜但是只能扫描IC2作物。
* [新增] 添加了电动修剪器，类似电动剪枝器。
* [新增] 普通炼药锅现在能通过水龙头填满。
* [新增] 能精确采集草方块、菌丝、粘土块和灰化土的铲子，这些铲子也在采集沙子和泥土材质的方块方面比普通铲子快。

## v6.05.12

* 修复了某坚果从任何树叶掉落的bug
* 加入空木箱，功能类似木板
