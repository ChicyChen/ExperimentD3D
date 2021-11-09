import os
import subprocess
from tqdm import tqdm
from multiprocessing import Pool
import pymeshlab

def convert(obj_path):
    # try:
    load_folder = os.path.join(obj_path, 'parts_ply')
    print(load_folder)
    save_folder = os.path.join(obj_path, 'parts_off')

    part_paths = [f.path for f in os.scandir(load_folder)]
    print(part_paths)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for part in part_paths:
        target_mesh = save_folder+'/'+part[-5:-3]+'off'
        print(part)
        print(target_mesh)
        
        source_mesh = part
        target_mesh_off = target_mesh
        ms = pymeshlab.MeshSet()
        ms.load_new_mesh(source_mesh)
        ms.save_current_mesh(target_mesh_off)
        
        # subprocess.run(["xvfb-run meshlabserver", "-i", part, "-o", target_mesh], shell=True, check=True)

    # except Exception as ex:
    #     print("Wrong")
    #     return 


# cad_folder = '/data/siyich/cad_sapien'
# cad_classes = [f.name for f in os.scandir(cad_folder)]

# for cad_category in cad_classes:

#     folder_path = os.path.join(cad_folder, cad_category)
#     object_paths = [f.path for f in os.scandir(folder_path)]

#     # Parallel
#     threads = 8  # number of threads in your computer
#     convert_iter = Pool(threads).imap(convert, object_paths) 
#     for _ in tqdm(convert_iter, total=len(object_paths)):
#         pass

cad_folder = '/data/siyich/cad_sapien_2'
cad_classes = [f.name for f in os.scandir(cad_folder)]

for cad_category in cad_classes:

    folder_path = os.path.join(cad_folder, cad_category)
    
    object_paths = [f.path for f in os.scandir(folder_path)]
    print(object_paths)
    for obj_path in object_paths:
        convert(obj_path) 

print("ended")
     
