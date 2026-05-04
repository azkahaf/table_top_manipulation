import mujoco
import mujoco.viewer

# Load your scene
model = mujoco.MjModel.from_xml_path("scene.xml")
data = mujoco.MjData(model)

# Launch viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()