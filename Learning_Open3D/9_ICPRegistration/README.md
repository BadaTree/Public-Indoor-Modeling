# ICP Registration
The examples included above are based on the tutorial from Open3D using both Python and C++. Hope this can help you! 

To deal with outliers, Robust kernels perform better than the standard point-to-plane ICP algorithm.

Point-to-Plane ICP algorithm has a faster convergence speed than the Point-to-Point ICP algorithm, which is shown in the ICPRegistration.
[**C++ Examples**](https://github.com/LYON-WANG/Learning_Open3D/blob/master/9_ICPRegistration/src/ICPRegistration.cpp)

[**Python Examples**](https://github.com/LYON-WANG/Learning_Open3D/blob/master/9_ICPRegistration/ICPRegistration.py)

**RUN C++ Example:** 
```
  mkdir build
  cd build
  cmake ..
  make
  cd ../bin
  ./ICPRegistration
  ./RobustICP
```

## Common Function Summary:
  - Point-to-Point ICP
  ```
  Python: o3d.pipelines.registration.registration_icp(source, target, threshold, trans_init,
          o3d.pipelines.registration.TransformationEstimationPointToPoint())

  C++: auto reg_p2p = open3d::pipelines::registration::RegistrationICP(*source, *target, threshold,
                trans_init, open3d::pipelines::registration::TransformationEstimationPointToPoint());
  ```
  - Point-to-Plane ICP
  ```
  Python: o3d.pipelines.registration.registration_icp(source, target, threshold, trans_init,
          o3d.pipelines.registration.TransformationEstimationPointToPlane())

  C++: auto reg_p2p = open3d::pipelines::registration::RegistrationICP(*source, *target, threshold,
                trans_init, open3d::pipelines::registration::TransformationEstimationPointToPlane());
  ```
  - Robust ICP
  ```
  Python: loss = o3d.pipelines.registration.TukeyLoss(k=sigma)
          p2l = o3d.pipelines.registration.TransformationEstimationPointToPlane(loss)
          reg_p2l = o3d.pipelines.registration.registration_icp(source_noisy, target,
                                                      threshold, trans_init,
                                                      p2l)

  C++:
  ```
  