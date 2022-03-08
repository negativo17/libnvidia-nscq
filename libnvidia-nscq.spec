%global real_name libnvidia_nscq

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 11-6

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        510.47.03
Release:        1%{?dist}
Summary:        NVSwitch Configuration and Query Library (NSCQ)
License:        NVIDIA Driver
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz

%description
The NSCQ library currently provides topology information of the NVSwitches and
GPUs to clients of the library such as DCGM.

%package        devel
Summary:        Development files for NVSwitch Configuration and Query Library (NSCQ)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      %{name}-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}

%description devel
This package provides development files for the NVSwitch Configuration and Query
Library (NSCQ).

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch ppc64le
%setup -q -T -b 1 -n %{real_name}-linux-ppc64le-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 2 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_libdir}
cp -fr lib/lib* %{buildroot}%{_libdir}/

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.2.0
%{_libdir}/%{name}.so.%{version}

%files devel
%{_libdir}/%{name}.so

%changelog
* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 1:510.47.03-1
- Update to 510.47.03 (CUDA 11.6.1).

* Fri Jan 28 2022 Simone Caronni <negativo17@gmail.com> - 1:510.39.01-1
- First build with the new tarball components.

