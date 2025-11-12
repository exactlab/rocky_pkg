Name:           pnetcdf
Version:        1.12.3
Release:        1%{?dist}
Summary:        Parallel I/O Library for NetCDF File Access

License:        Custom
URL:            https://parallel-netcdf.github.io/
Source0:        https://parallel-netcdf.github.io/Release/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  openmpi-devel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  netcdf-openmpi-devel
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

Requires:       openmpi
Requires:       hdf5-openmpi
Requires:       netcdf-openmpi

%description
PNetCDF is a high-performance parallel I/O library for accessing files in 
format compatibility with Unidata's NetCDF. PNetCDF is built on top of MPI-IO.

%package devel
Summary:        Development files for pnetcdf
Requires:       %{name} = %{version}-%{release}
Requires:       openmpi-devel

%description devel
Development files and headers for pnetcdf library.

%prep
%setup -q

%build
module load mpi/openmpi-x86_64
export CC=mpicc
export CXX=mpicxx
export MPICC=mpicc
export MPICXX=mpicxx

%configure \
    --enable-shared \
    --disable-static \
    --enable-fortran \
    --enable-cxx

make %{?_smp_mflags}

%install
module load mpi/openmpi-x86_64
make install DESTDIR=%{buildroot}

# Remove libtool archives
find %{buildroot} -name "*.la" -delete

%files
%license COPYING
%doc README RELEASE_NOTES
%{_libdir}/libpnetcdf.so.*

%files devel
%{_includedir}/*.h
%{_includedir}/*.inc
%{_includedir}/*.mod
%{_includedir}/pnetcdf*
%{_libdir}/libpnetcdf.so
%{_libdir}/pkgconfig/pnetcdf.pc
%{_bindir}/pnetcdf-config
%{_bindir}/pnetcdf_version
%{_bindir}/cdfdiff
%{_bindir}/ncmpidiff
%{_bindir}/ncmpidump
%{_bindir}/ncmpigen
%{_bindir}/ncoffsets
%{_bindir}/ncvalidator
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Nov 11 2024 Builder <builder@localhost> - 1.12.3-1
- Initial package for Rocky Linux 9