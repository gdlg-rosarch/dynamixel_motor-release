# Script generated with Bloom
pkgdesc="ROS - This package provides low level IO for Robotis Dynamixel servos. Fully supports and was tested with AX-12, AX-18, RX-24, RX-28, MX-28, RX-64, EX-106 models. Hardware specific constants are defined for reading and writing information from/to Dynamixel servos. This low level package won't be used directly by most ROS users. The higher level dynamixel_controllers and specific robot joint controllers make use of this package."
url='http://ros.org/wiki/dynamixel_driver'

pkgname='ros-kinetic-dynamixel-driver'
pkgver='0.4.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('python2-pyserial'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-rospy'
)

conflicts=()
replaces=()

_dir=dynamixel_driver
source=()
md5sums=()

prepare() {
    cp -R $startdir/dynamixel_driver $srcdir/dynamixel_driver
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

