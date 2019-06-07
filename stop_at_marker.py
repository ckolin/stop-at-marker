bl_info = {
    "name": "Stop Playback at Marker",
    "description": "Always stops playback at marker when enabled",
    "blender": (2, 80, 0),
    "category": "Animation"
}

import bpy

def marker_stopper(scene):
    for marker in scene.timeline_markers.values():
        if marker.frame == scene.frame_current:
            bpy.ops.screen.animation_cancel(restore_frame=False)
            break

def register():
    bpy.app.handlers.frame_change_post.append(marker_stopper)

def unregister():
    bpy.app.handlers.frame_change_post.remove(marker_stopper)
    