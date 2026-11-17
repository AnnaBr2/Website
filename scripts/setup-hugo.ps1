# Downloads the pinned standard Hugo release without changing system PATH.
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$projectRoot = Split-Path $PSScriptRoot -Parent
$version = (Get-Content (Join-Path $projectRoot '.hugo-version') -Raw).Trim()
if ($version -notmatch '^\d+\.\d+\.\d+$') { throw 'Invalid .hugo-version value.' }
$architecture = [System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture.ToString().ToLowerInvariant()
if ($architecture -eq 'x64') { $architecture = 'amd64' }
if ($architecture -notin @('amd64', 'arm64')) { throw "Unsupported architecture: $architecture" }
$destination = Join-Path $projectRoot '.tools/hugo'
New-Item -ItemType Directory -Path $destination -Force | Out-Null
$archiveName = "hugo_${version}_windows-${architecture}.zip"
$archivePath = Join-Path $destination $archiveName
$checksumsPath = Join-Path $destination 'checksums.txt'
$releaseUrl = "https://github.com/gohugoio/hugo/releases/download/v$version"
Invoke-WebRequest "$releaseUrl/$archiveName" -OutFile $archivePath
Invoke-WebRequest "$releaseUrl/hugo_${version}_checksums.txt" -OutFile $checksumsPath
$checksumLine = Get-Content $checksumsPath | Where-Object { ($_ -split '\s+')[-1] -eq $archiveName }
if (@($checksumLine).Count -ne 1) { throw 'Expected exactly one release checksum.' }
$expected = ($checksumLine -split '\s+')[0]
$actual = (Get-FileHash -LiteralPath $archivePath -Algorithm SHA256).Hash
if ($actual -ne $expected) { throw 'Hugo archive checksum mismatch.' }
Expand-Archive -LiteralPath $archivePath -DestinationPath $destination -Force
& (Join-Path $destination 'hugo.exe') version
if ($LASTEXITCODE -ne 0) { throw 'Hugo installation verification failed.' }
Write-Host 'Ready. Preview with: & .\.tools\hugo\hugo.exe server -D'
