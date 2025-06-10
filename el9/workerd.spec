Name:           workerd
Version:        1.%VERSION%.0
Release:        1%{?dist}
Summary:        The JavaScript / Wasm runtime that powers Cloudflare Workers

License:        Apache License 2.0
URL:            https://blog.cloudflare.com/workerd-open-source-workers-runtime/

%description
workerd (pronounced: "worker-dee") is a JavaScript / Wasm server runtime based on the same code that powers Cloudflare Workers.
You might use it:
    As an application server, to self-host applications designed for Cloudflare Workers.
    As a development tool, to develop and test such code locally.
    As a programmable HTTP proxy (forward or reverse), to efficiently intercept, modify, and route network requests.

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $RPM_BUILD_ROOT/usr/local/bin
install -p -m 0755 %{_sourcedir}/bazel-bin/src/workerd/server/workerd $RPM_BUILD_ROOT/usr/local/bin/%{name}


%files
%doc README.md RELEASE.md
%license LICENSE
/usr/local/bin/%{name}

# %changelog
