# reference: http://graphics.im.ntu.edu.tw/~robin/courses/cg03/model/
import open3d as o3d

if __name__ == '__main__':
    # Read the PLY file:
    file_name = "bunny.ply" #***************************** 원하는 파일명으로 수정 *********************************#
    mesh = o3d.io.read_triangle_mesh("C:/Users/SKH/Github_local/3D_Modeling_with_Three.js/pointcloudprocessing/data/"+ file_name)

    # Import data from open3D:
    # bunny = o3d.data.BunnyMesh()
    # mesh = o3d.io.read_triangle_mesh(bunny.path)

    # Visualize:
    mesh.compute_vertex_normals() # compute normals for vertices or faces
    o3d.visualization.draw_geometries([mesh])

    # Sample 1000 points:
    pcd = mesh.sample_points_uniformly(number_of_points=1000)

    # visualize:
    o3d.visualization.draw_geometries([pcd])

    # Save into ply file:
    o3d.io.write_point_cloud("../output/"+ file_name+"_pcd.ply", pcd)
