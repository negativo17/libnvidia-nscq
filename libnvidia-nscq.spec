%global real_name libnvidia_nscq

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-0

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        535.54.03
Release:        1%{?dist}
Summary:        NVSwitch Configuration and Query Library (NSCQ)
License:        NVIDIA Driver
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

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

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-aarch64-%{version}-archive
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
* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 1:535.54.03-1
- Update to 535.54.03.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:530.30.02-1
- Update to 530.30.02.

* Sat Feb 25 2023 Simone Caronni <negativo17@gmail.com> - 1:525.85.12-1
- Update to 525.85.12.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:525.60.13-1
- Update to 525.60.13.

* Fri Nov 11 2022 Simone Caronni <negativo17@gmail.com> - 1:520.61.05-1
- Update to 520.61.05.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:515.65.01-1
- Update to 515.65.01.

* Thu Jun 23 2022 Simone Caronni <negativo17@gmail.com> - 1:515.43.04-1
- Update to 515.43.04.

* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 1:510.47.03-1
- Update to 510.47.03 (CUDA 11.6.1).

* Fri Jan 28 2022 Simone Caronni <negativo17@gmail.com> - 1:510.39.01-1
- First build with the new tarball components.

