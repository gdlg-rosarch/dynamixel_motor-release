# Script generated with Bloom
pkgdesc="ROS - This stack contains packages that are used to interface with Robotis Dynamixel line of servo motors. This stack was tested with and fully supports AX-12, AX-18, RX-24, RX-28, MX-28, RX-64, MX-64, EX-106 and MX-106 models."
url='http://ros.org/wiki/dynamixel_driver'

pkgname='ros-kinetic-dynamixel-motor'
pkgver='0.4.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-dynamixel-controllers'
'ros-kinetic-dynamixel-driver'
'ros-kinetic-dynamixel-msgs'
'ros-kinetic-dynamixel-tutorials'
)

conflicts=()
replaces=()

_dir=dynamixel_motor
source=()
md5sums=()

prepare() {
    cp -R $startdir/dynamixel_motor $srcdir/dynamixel_motor
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

