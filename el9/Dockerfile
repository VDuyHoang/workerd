FROM rockylinux/rockylinux:9 AS builder
ARG BAZEL_VERSION=8.2.1
ARG UID=1000
RUN yum install -y git patch tcl epel-release rpm-build && \
  dnf copr -y enable @fedora-llvm-team/llvm-snapshots centos-stream-9-x86_64 && \
  dnf copr -y enable lihaohong/bazel && \
  yum -y install clang19 lld19 clang19-devel bazel
RUN useradd -u ${UID} -m joe
RUN mkdir -p /home/joe/workerd
WORKDIR /home/joe/workerd
COPY . .
RUN echo "build:linux --action_env=CC=/usr/bin/clang-19" >> .bazelrc
RUN echo "build:linux --host_action_env=CC=/usr/bin/clang-19" >> .bazelrc
RUN chown -R joe:joe /home/joe/workerd && chmod +x el9/entrypoint.sh
USER joe
RUN git config core.hooksPath githooks
ENTRYPOINT ["el9/entrypoint.sh"]
# RUN bazel build --config=release_linux //src/workerd/server:workerd

# FROM scratch as artifact
# COPY --from=builder /home/joe/workerd/bazel-bin/src/workerd/server/workerd /workerd-linux-x86_64
#fedora-llvm-team/llvm-snapshots no more rhel9
# bazel-8.2.1
