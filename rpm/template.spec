Name:           ros-jade-dynamixel-controllers
Version:        0.4.1
Release:        0%{?dist}
Summary:        ROS dynamixel_controllers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/dynamixel_controllers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-control-msgs
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-dynamixel-driver
Requires:       ros-jade-dynamixel-msgs
Requires:       ros-jade-rospy
Requires:       ros-jade-std-msgs
Requires:       ros-jade-trajectory-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-generation

%description
This package contains a configurable node, services and a spawner script to
start, stop and restart one or more controller plugins. Reusable controller
types are defined for common Dynamixel motor joints. Both speed and torque can
be set for each joint. This python package can be used by more specific robot
controllers and all configurable parameters can be loaded via a yaml file.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Jan 19 2017 Antons Rebguns <arebgun@gmail.com> - 0.4.1-0
- Autogenerated by Bloom

* Wed Jun 24 2015 Antons Rebguns <arebgun@gmail.com> - 0.4.0-0
- Autogenerated by Bloom

