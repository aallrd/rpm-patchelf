# rpm-internal-patchelf

Build a RPM package for the **internal-patchelf** project.

## RPM build

```
$ docker run --rm -it --volume $(pwd):/specs --volume $(pwd):/output localhost:5000/aallrd/internal-build-rpm --build
[INFO] [14:32:47] RPM spec file: patchelf.spec
[...]
[SUCCESS] [14:32:54] Binary RPM file(s):
[SUCCESS] [14:32:54] * /root/rpmbuild/RPMS/x86_64/internal-patchelf-0.9-1.el6.x86_64.rpm
[SUCCESS] [14:32:54] * /root/rpmbuild/RPMS/x86_64/internal-patchelf-debuginfo-0.9-1.el6.x86_64.rpm
[SUCCESS] [14:32:54] Source RPM file(s):
[SUCCESS] [14:32:54] * /root/rpmbuild/SRPMS/internal-patchelf-0.9-1.el6.src.rpm
```

## RPM installation

### Using YUM

```
# Configure the vendor repo on the server
$ cat <<EOF >> /etc/yum.repos.d/vendors.repo

[vendor-internal]
name=internal
baseurl=http://localhost:4000/vendors/internal
enabled=1
gpgcheck=0
proxy=_none_
EOF

# Install the package using Yum
$ yum install -y --disablerepo=* --enablerepo=vendor-internal internal-patchelf
```

### Using RPM

```
$ wget http://localhost:4000/vendors/internal/internal-patchelf-0.9-1.el6.x86_64.rpm
$ rpm -ivh internal-patchelf-0.9-1.el6.x86_64.rpm
Preparing...                ########################################### [100%]
   1:internal-patchelf               ########################################### [100%]
```

## Usage

```
$ /opt/internal/root/bin/internal-patchelf --help
syntax: /opt/internal/root/bin/internal-patchelf
  [--set-interpreter FILENAME]
  [--page-size SIZE]
  [--print-interpreter]
  [--print-soname]              Prints 'DT_SONAME' entry of .dynamic section. Raises an error if DT_SONAME doesn't exist
  [--set-soname SONAME]         Sets 'DT_SONAME' entry to SONAME.
  [--set-rpath RPATH]
  [--remove-rpath]
  [--shrink-rpath]
  [--print-rpath]
  [--force-rpath]
  [--add-needed LIBRARY]
  [--remove-needed LIBRARY]
  [--replace-needed LIBRARY NEW_LIBRARY]
  [--print-needed]
  [--no-default-lib]
  [--debug]
  [--version]
  FILENAME
```
