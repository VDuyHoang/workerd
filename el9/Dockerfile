FROM rockylinux/rockylinux:9 AS builder
ARG BAZEL_VERSION=8.3.1
ARG UID=1000
RUN yum install -y git patch tcl epel-release rpm-build wget && \
  dnf copr -y enable @fedora-llvm-team/llvm-snapshots centos-stream-9-x86_64 && \
  yum -y install clang19 lld19 clang19-devel && \
  wget https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-linux-x86_64 -O /usr/bin/bazel && \
  chmod +x /usr/bin/bazel && \
  useradd -u ${UID} -m joe
RUN mkdir -p /home/joe/workerd
WORKDIR /home/joe/workerd
COPY . .
RUN echo "build:linux --action_env=CC=/usr/bin/clang-19" >> .bazelrc
RUN echo "build:linux --host_action_env=CC=/usr/bin/clang-19" >> .bazelrc
RUN chown -R joe:joe /home/joe/workerd && chmod +x el9/entrypoint.sh
USER joe
RUN git config core.hooksPath githooks
ENTRYPOINT ["el9/entrypoint.sh"]
