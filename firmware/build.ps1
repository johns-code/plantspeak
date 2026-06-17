param(
    [string]$Configuration = "Release",
    [string]$UV4Path = $env:KEIL_UV4_PATH,
    [string]$ProjectPath = $env:PLANTSPEAK_KEIL_PROJECT,
    [string]$Target = $env:PLANTSPEAK_KEIL_TARGET,
    [string]$EvidenceDir = "docs/test-evidence",
    [switch]$RequireToolchain
)

$ErrorActionPreference = "Stop"

Write-Host "PlantSpeak firmware build contract"
Write-Host "Configuration: $Configuration"

if ([string]::IsNullOrWhiteSpace($Target)) {
    $Target = "DA14531"
}

if ([string]::IsNullOrWhiteSpace($UV4Path) -or [string]::IsNullOrWhiteSpace($ProjectPath)) {
    if ($RequireToolchain) {
        throw "KEIL_UV4_PATH and PLANTSPEAK_KEIL_PROJECT are required when -RequireToolchain is set."
    }
    Write-Host "KEIL_UV4_PATH or PLANTSPEAK_KEIL_PROJECT is not set; contract-only build evidence is active."
    exit 0
}

if (!(Test-Path -LiteralPath $UV4Path)) {
    throw "uVision executable was not found at '$UV4Path'."
}
if (!(Test-Path -LiteralPath $ProjectPath)) {
    throw "Keil project was not found at '$ProjectPath'."
}

$evidenceRoot = Resolve-Path -LiteralPath "."
$evidencePath = Join-Path $evidenceRoot $EvidenceDir
New-Item -ItemType Directory -Force -Path $evidencePath | Out-Null

$rawLog = Join-Path $evidencePath "keil-da14531-build-raw.log"
$summaryJson = Join-Path $evidencePath "keil-da14531-build-summary.json"
$projectDir = Split-Path -Parent $ProjectPath

Remove-Item -LiteralPath $rawLog -ErrorAction SilentlyContinue

Write-Host "uVision: $UV4Path"
Write-Host "Project: $ProjectPath"
Write-Host "Target: $Target"
Write-Host "Raw log: $rawLog"

Push-Location $projectDir
try {
    & $UV4Path -r $ProjectPath -t $Target -o $rawLog
    $uv4ExitCode = $LASTEXITCODE
}
finally {
    Pop-Location
}

if (!(Test-Path -LiteralPath $rawLog)) {
    $deadline = (Get-Date).AddSeconds(120)
    while ((Get-Date) -lt $deadline -and !(Test-Path -LiteralPath $rawLog)) {
        Start-Sleep -Milliseconds 500
    }
}

$deadline = (Get-Date).AddSeconds(120)
do {
    if (Test-Path -LiteralPath $rawLog) {
        $logText = Get-Content -LiteralPath $rawLog -Raw
        if ($logText -match '0 Error\(s\)') {
            break
        }
    }
    Start-Sleep -Milliseconds 500
} while ((Get-Date) -lt $deadline)

if (!(Test-Path -LiteralPath $rawLog)) {
    throw "uVision did not produce the expected build log '$rawLog'."
}

$logText = Get-Content -LiteralPath $rawLog -Raw
if ([string]::IsNullOrWhiteSpace($logText)) {
    throw "uVision produced an empty build log."
}
if ($logText -notmatch '0 Error\(s\)') {
    throw "uVision build log does not contain a zero-error result."
}

$outputDir = Join-Path $projectDir "out_DA14531\Objects"
$outputs = @("ble_app_peripheral_531.axf", "ble_app_peripheral_531.hex", "ble_app_peripheral_531.bin") | ForEach-Object {
    $path = Join-Path $outputDir $_
    if (Test-Path -LiteralPath $path) {
        $file = Get-Item -LiteralPath $path
        [pscustomobject]@{
            path = $file.FullName
            size_bytes = $file.Length
            sha256 = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
            last_write_time = $file.LastWriteTime.ToString("o")
        }
    }
}

$summary = [pscustomobject]@{
    gate = "keil-da14531-build"
    status = "pass"
    uv4_exit_code = $uv4ExitCode
    target = $Target
    project_path = $ProjectPath
    raw_log = $rawLog
    result = (($logText | Select-String -Pattern '".*\.axf" - 0 Error\(s\).*' -AllMatches).Matches.Value | Select-Object -Last 1)
    outputs = @($outputs)
}
$json = $summary | ConvertTo-Json -Depth 5
[System.IO.File]::WriteAllText($summaryJson, $json, [System.Text.UTF8Encoding]::new($false))

Write-Host "Firmware build gate passed."
Write-Host "Summary: $summaryJson"
