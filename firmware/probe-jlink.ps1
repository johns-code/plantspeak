param(
    [string]$JLinkPath = $env:JLINK_EXE_PATH,
    [string]$EvidenceDir = "docs/test-evidence",
    [switch]$RequireProbe
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($JLinkPath)) {
    $candidates = @(
        "C:\Program Files\SEGGER\JLink_V856\JLink.exe",
        "C:\Program Files (x86)\SEGGER\JLink_V856\JLink.exe",
        "C:\Program Files\SEGGER\JLink_V722b\JLink.exe",
        "C:\Program Files (x86)\SEGGER\JLink_V722b\JLink.exe"
    )
    $JLinkPath = $candidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
}

if ([string]::IsNullOrWhiteSpace($JLinkPath) -or !(Test-Path -LiteralPath $JLinkPath)) {
    if ($RequireProbe) {
        throw "J-Link executable was not found."
    }
    Write-Host "J-Link executable not found; probe skipped."
    exit 0
}

$root = Resolve-Path -LiteralPath "."
$evidencePath = Join-Path $root $EvidenceDir
New-Item -ItemType Directory -Force -Path $evidencePath | Out-Null

$scriptPath = Join-Path $env:TEMP "plantspeak_jlink_probe.jlink"
$rawLog = Join-Path $evidencePath "jlink-probe-raw.log"
$summaryJson = Join-Path $evidencePath "jlink-probe-summary.json"

@"
ShowEmuList
Exit
"@ | Set-Content -LiteralPath $scriptPath -Encoding ascii

$probeOutput = & $JLinkPath -CommanderScript $scriptPath
$jlinkExitCode = $LASTEXITCODE
[System.IO.File]::WriteAllText($rawLog, ($probeOutput -join [Environment]::NewLine), [System.Text.UTF8Encoding]::new($false))

if (!(Test-Path -LiteralPath $rawLog)) {
    throw "J-Link probe did not produce '$rawLog'."
}

$logText = Get-Content -LiteralPath $rawLog -Raw
$connected = $logText -match 'J-Link\[0\]'
$serial = $null
if ($logText -match 'Serial number:\s*(\d+)') {
    $serial = $Matches[1]
}

if ($RequireProbe -and !$connected) {
    throw "No connected J-Link emulator was found."
}

$summary = [pscustomobject]@{
    gate = "jlink-emulator-probe"
    status = $(if ($connected) { "pass" } else { "deferred" })
    jlink_exit_code = $jlinkExitCode
    jlink_path = $JLinkPath
    connected = $connected
    serial_number = $serial
    raw_log = $rawLog
}
$json = $summary | ConvertTo-Json -Depth 4
[System.IO.File]::WriteAllText($summaryJson, $json, [System.Text.UTF8Encoding]::new($false))

Write-Host "J-Link probe status: $($summary.status)"
Write-Host "Summary: $summaryJson"
