更新日志 *(1.7.10)*

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
* [兼容] 更好地支持了 **生长工艺** *(Growthcraft)* 模组的社区版本。例如它的竹子可以用在焦炉里面了（我因同样的理由为**超多生态群系** *(Biomes O' Plenty)*也增加了相同的配方）。
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
