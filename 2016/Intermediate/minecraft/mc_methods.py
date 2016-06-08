import time
import random
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()

def nyan_cat():
    """Generates a constant trail of wool blocks of various colors underneath the player."""
    while True:
        x, y, z = mc.player.getPos() 
        # Pick a random color for the wool.
        color = random.randint(1, 15)
        # Create a wool block of that color underneath where the player is
        # standing.
        mc.setBlock(x, y - 1, z, 35, color)
        time.sleep(0.1)

def make_tnt_block(size):
    """Generates a cube of a certain size (e.g., passing in 4 will create a 4x4x4 cube) near the player."""
    x, y, z = mc.player.getPos()
    # Pass `1` as the optional `data` parameter to make the TNT armed.
    mc.setBlocks(x + 1, y, z + 1, x + size, y - 1 + size, z + size, block.TNT, 1)


def turn_blocks_to_diamonds():
    """Listens for any block events (right-clicks on blocks while holding the sword) and converts any such block to a diamond block."""
    while True:
        # Each time this is called, it will return a list of all the events
        # that happened since the last time you called it.
        events = mc.events.pollBlockHits()
        for event in events:
            # Each event points to the position of the block that was clicked
            # on.
            x, y, z = event.pos
            mc.setBlock(x, y, z, block.DIAMOND_BLOCK)
        time.sleep(0.1)
        
def get_random_place():
    """Returns the X, Y, and Z coordinates for a random "safe" place in the game world."""
    # Worlds in MCPI are small. The X and Z coordinates range from -128 to
    # 128.
    y = -64
    # Sometimes we get a Y value of -64, which is no good for teleportation.
    # Try again if that happens.
    while y == -64:
        x, z = [random.randint(-128, 128) for i in range(2)]
        # Use that X/Z coordinate pair to find a Y-height that is guaranteed to
        # be safe.
        y = mc.getHeight(x, z)
    return [x, y, z]
        
def tree_teleportation():
    """
    All trees in your world now have magic powers.
    
    (Teleport to a random place whenever you right-click with a sword on a tree block.)
    """
    while True:
        events = mc.events.pollBlockHits()
        for event in events:
            x, y, z = event.pos
            # Find the block at that location.
            last_block = mc.getBlockWithData(x, y, z)
            # All varieties of wood have the same block ID.
            if last_block.id == block.WOOD.id:
                mc.postToChat("Teleporting!")
                x, y, z = get_random_place()
                mc.player.setPos(x, y, z)
            time.sleep(0.1)
