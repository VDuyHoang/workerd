#!/bin/bash
set -e
# bazel build
bazel build --config=release_linux //src/workerd/server:workerd
supportedCompatibilityDate=$(cat src/workerd/io/supported-compatibility-date.txt);
version=${supportedCompatibilityDate//-/};
echo "TagVersion:v1.$version";
sed -i "s/%VERSION%/${version}/g" el9/workerd.spec
#rpmbuild -ba --build-in-place --define "_topdir $(pwd)/rpm" el9/workerd.spec
# create rpm package
rpmbuild --define "_topdir $(pwd)" \
 --define "_sourcedir $(pwd)" \
 --define "_builddir $(pwd)" --define "_rpmdir $(pwd)" \
 --define "_srcrpmdir /tmp" \
 -bb el9/workerd.spec
# copy the package to the output directory
cp /home/joe/workerd/x86_64/workerd-*.rpm ~/output/
# copy the workerd binary to the output directory
cp bazel-bin/src/workerd/server/workerd ~/output/
