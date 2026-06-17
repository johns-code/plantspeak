param(
    [string]$PcToolsPath = $env:PLANTSPEAK_PC_TOOLS,
    [string]$DeviceName = "P531-Handheld",
    [int]$TimeoutSeconds = 8,
    [int]$MeasurementBurstCount = 1,
    [string]$EvidenceDir = "docs/test-evidence",
    [switch]$RequireLiveBoard
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($PcToolsPath)) {
    $PcToolsPath = "C:\Users\johns\531 Project\P531_Handheld"
}

if (!(Test-Path -LiteralPath (Join-Path $PcToolsPath "pc_tools\test_icd_regression.py"))) {
    if ($RequireLiveBoard) {
        throw "pc_tools regression script was not found under '$PcToolsPath'."
    }
    Write-Host "pc_tools regression script not found; live ICD smoke skipped."
    exit 0
}

$root = Resolve-Path -LiteralPath "."
$evidencePath = Join-Path $root $EvidenceDir
New-Item -ItemType Directory -Force -Path $evidencePath | Out-Null
$rawLog = Join-Path $evidencePath "live-icd-smoke-raw.log"
$summaryJson = Join-Path $evidencePath "live-icd-smoke-summary.json"

Push-Location $PcToolsPath
try {
    $outputPath = Join-Path $env:TEMP "plantspeak_live_icd_smoke_stdout.log"
    $errorPath = Join-Path $env:TEMP "plantspeak_live_icd_smoke_stderr.log"
    Remove-Item -LiteralPath $outputPath -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath $errorPath -ErrorAction SilentlyContinue
    $process = Start-Process -FilePath "python" -ArgumentList @(
        "pc_tools\test_icd_regression.py",
        "--name", $DeviceName,
        "--timeout", $TimeoutSeconds,
        "--meas-burst-count", $MeasurementBurstCount
    ) -NoNewWindow -Wait -PassThru -RedirectStandardOutput $outputPath -RedirectStandardError $errorPath
    $exitCode = $process.ExitCode
    $output = @()
    if (Test-Path -LiteralPath $outputPath) {
        $output += Get-Content -LiteralPath $outputPath
    }
    if (Test-Path -LiteralPath $errorPath) {
        $output += Get-Content -LiteralPath $errorPath
    }
}
finally {
    Pop-Location
}

[System.IO.File]::WriteAllText($rawLog, ($output -join [Environment]::NewLine), [System.Text.UTF8Encoding]::new($false))
$logText = [System.IO.File]::ReadAllText($rawLog)

if ($RequireLiveBoard -and $exitCode -ne 0) {
    throw "Live ICD smoke failed with exit code $exitCode. See '$rawLog'."
}

$requiredPasses = @(
    "PASS PING",
    "PASS GET_INFO",
    "PASS GET_STATUS",
    "PASS START_MEAS",
    "PASS UNKNOWN_OPCODE",
    "PASS SET_PERIPH_POWER final off"
)
$missing = @($requiredPasses | Where-Object { $logText -notmatch [regex]::Escape($_) })
$status = if ($exitCode -eq 0 -and $missing.Count -eq 0) { "pass" } else { "fail" }

if ($RequireLiveBoard -and $status -ne "pass") {
    throw "Live ICD smoke did not contain all required PASS markers: $($missing -join ', ')."
}

$summary = [pscustomobject]@{
    gate = "live-icd-smoke"
    status = $status
    exit_code = $exitCode
    device_name = $DeviceName
    pc_tools_path = $PcToolsPath
    measurement_burst_count = $MeasurementBurstCount
    required_pass_markers = $requiredPasses
    missing_pass_markers = $missing
    raw_log = $rawLog
}
$json = $summary | ConvertTo-Json -Depth 5
[System.IO.File]::WriteAllText($summaryJson, $json, [System.Text.UTF8Encoding]::new($false))

Write-Host "Live ICD smoke status: $status"
Write-Host "Summary: $summaryJson"
