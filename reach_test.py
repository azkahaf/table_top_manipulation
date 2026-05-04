import numpy as np
import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("panda.xml")
data = mujoco.MjData(model)

mujoco.mj_resetData(model, data)

# set cube pose manually
data.qpos[7:10] = [0.2, 0, 0.78]
data.qpos[10:14] = [1, 0, 0, 0]

mujoco.mj_forward(model, data)

cube_id = model.body("cube1").id
ee_id = model.body("hand").id

with mujoco.viewer.launch_passive(model, data) as viewer:
    viewer.cam.distance = 2.5
    viewer.cam.azimuth = 120
    viewer.cam.elevation = -30
    viewer.cam.lookat[:] = [0, 0, 0.7]

    while viewer.is_running():

        cube_pos = data.xpos[cube_id]
        ee_pos = data.xpos[ee_id]

        # simple fixed joint target (correct test)
        target = np.array([0, -0.8, 0, -2.2, 0, 2.0, 0.8])
        data.ctrl[:7] = target

        mujoco.mj_step(model, data)
        viewer.sync()