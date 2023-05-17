scene_number = 1
last = 4
with open("game\chapter_2.rpy", "a") as file:
    while scene_number <= last:
        scene_text = f"scene bg dytwoskoolazmisaysmply {scene_number} with Dissolve(0.8)"
        file.write(scene_text + "\n")
        file.write("pause\n")
        scene_number += 1