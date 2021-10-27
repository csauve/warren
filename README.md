# Warren
Warren is a Halo Custom Edition map originally created for the [Halo Modding Reclaimers][reclaimers] Discord server's season 2 map contest. Its environment takes visual inspiration from the 343 Guilty Spark campaign mission and is set somewhere nearby.

![](screenshot.png)
![](screenshot2.png)

Warren is based on [contest layout #3][blaze] designed by Blaze Lightcap. Compared to the `warren_beta.map` released for the contest, this final version has received a few minor layout changes, lightmap fixes, and improved netgame flag/equipment placements. The map plays best with 8-12 players and supports all gametypes.

## Building the map
The [Halo Editing Kit (HEK)][hek] is required to build this map. In order to compile Warren from tags, its tagset must first be assembled. Paste the following tagsets into the HEK's `tags` folder, replacing files as needed, in the order shown:

1. [HEK base tags][11]: Already included in the HEK, but you may want to repair them if your tagset is dirty or corrupted.
2. [Fresh MP/SP tagset (Refined Project)][12]: A more complete tag set extracted from Halo's stock maps.
3. [Jesse's high resolution HUD][13]: A higher quality player HUD by Jesse, found under `enhancements`.
4. The tags included in this repo.

If you have done this correctly, you should be able to build the map cache using Tool:

```sh
# creates maps/warren.map
tool.exe build-cache-file levels\warren\warren
```

Final lightmaps were run with quality and stop parameters: `1 0.01`.

Rebuilt versions of this map which aim to be multiplayer-compatible should forge their CRC32 checksum to `0x7ADF1DB3` (invader-build can do this).

## Assets
Source assets are also included under this repo's `data` folder. You can use the included Python script to synchronize data and tags from this repo to/from the HEK if you want to keep its files separate:

```sh
python hek-sync.py <hek-root>
```

Texture sources are `.kra` files for the free 2D software [Krita][krita]. They are exported to flattened `.tif` files and then compiled to `.bitmap` tags using Tool.

The map's BSP was made in [Blender][blender] and exported to JMS using [General_101's Toolset][toolset]. It contains the following objects:

* **frame**: Only children of this reference frame are exported to the JMS file
  * **bsp**: Main level geometry
  * **fog**: Contains plane which is assigned a fog volume in Sapien
  * **playerclip**: Contains player-only collision surfaces meant to stop players from going out of bounds
  * **portals**: Geometry which divides the map into clusters for rendering, sound, and weather purposes
  * **weatherpoly**: Contains weather polyhedra for masking cluster weather particles under overhangs and indoors

[hek]: http://hce.halomaps.org/hek/
[krita]: https://krita.org/en
[reclaimers]: https://discord.gg/reclaimers
[blaze]: https://www.artstation.com/artwork/q93akL
[toolset]: https://github.com/General-101/Halo-Asset-Blender-Development-Toolset
[blender]: https://www.blender.org/
[11]: https://cdn.discordapp.com/attachments/523620962390769695/654482973390929932/editor_tags.7z
[12]: https://www.dropbox.com/s/j6fb3ox6z1xmzzq/fresh_mp_sp_custom_edition_tagset.7z?dl=1
[13]: https://www.dropbox.com/s/p2d76dsu47axrao/refined_halo1_replacement_tags.7z?dl=1
