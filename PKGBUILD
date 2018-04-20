# Script generated with Bloom
pkgdesc="ROS - This package contains a configurable node, services and a spawner script to start, stop and restart one or more controller plugins. Reusable controller types are defined for common Dynamixel motor joints. Both speed and torque can be set for each joint. This python package can be used by more specific robot controllers and all configurable parameters can be loaded via a yaml file."
url='http://ros.org/wiki/dynamixel_controllers'

pkgname='ros-kinetic-dynamixel-controllers'
pkgver='0.4.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-message-generation'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-control-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-dynamixel-driver'
'ros-kinetic-dynamixel-msgs'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-trajectory-msgs'
)

conflicts=()
replaces=()

_dir=dynamixel_controllers
source=()
md5sums=()

prepare() {
    cp -R $startdir/dynamixel_controllers $srcdir/dynamixel_controllers
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

