param(
    [string]$ToolPath = $env:SMARTSNIPPETS_TOOLBOX,
    [string]$SdkPath = $env:DA14531_SDK_PATH,
    [string]$FirmwareBin = $env:PLANTSPEAK_FIRMWARE_BIN,
    [string]$JLinkSerial = $env:PLANTSPEAK_JLINK_SERIAL,
    [string]$EvidenceDir = "docs/test-evidence",
    [switch]$ConfirmFlash
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($ToolPath)) {
    $ToolPath = "C:\Program Files\SmartSnippetsToolbox\SmartSnippetsToolbox5.0.26\SmartSnippetsToolbox.exe"
}
if ([string]::IsNullOrWhiteSpace($SdkPath)) {
    $SdkPath = "C:\DA14531_SDK6\DA145xx_SDK\6.0.24.1464"
}
if ([string]::IsNullOrWhiteSpace($FirmwareBin)) {
    $FirmwareBin = "C:\Users\johns\531 Project\P531_Handheld\Keil\out_DA14531\Objects\ble_app_peripheral_531.bin"
}
if ([string]::IsNullOrWhiteSpace($JLinkSerial)) {
    $probeSummary = Join-Path (Resolve-Path -LiteralPath ".") "docs/test-evidence/jlink-probe-summary.json"
    if (Test-Path -LiteralPath $probeSummary) {
        $JLinkSerial = (Get-Content -LiteralPath $probeSummary -Raw | ConvertFrom-Json).serial_number
    }
}

$programmer = Join-Path $SdkPath "config\toolbox_resources\DA1453x\common\jtag_programmer.bin"
$root = Resolve-Path -LiteralPath "."
$evidencePath = Join-Path $root $EvidenceDir
New-Item -ItemType Directory -Force -Path $evidencePath | Out-Null
$rawLog = Join-Path $evidencePath "smart-snippets-flash-raw.log"
$summaryJson = Join-Path $evidencePath "smart-snippets-flash-summary.json"

$required = @{
    ToolPath = $ToolPath
    SdkPath = $SdkPath
    FirmwareBin = $FirmwareBin
    Programmer = $programmer
    JLinkSerial = $JLinkSerial
}
foreach ($item in $required.GetEnumerator()) {
    if ([string]::IsNullOrWhiteSpace([string]$item.Value)) {
        throw "$($item.Key) is required."
    }
    if ($item.Key -ne "JLinkSerial" -and !(Test-Path -LiteralPath $item.Value)) {
        throw "$($item.Key) was not found at '$($item.Value)'."
    }
}

if (!$ConfirmFlash) {
    $summary = [pscustomobject]@{
        gate = "smart-snippets-flash"
        status = "deferred"
        reason = "Flash requires -ConfirmFlash because it erases and writes target SPI flash."
        tool_path = $ToolPath
        sdk_path = $SdkPath
        firmware_bin = $FirmwareBin
        jlink_serial = $JLinkSerial
    }
    $json = $summary | ConvertTo-Json -Depth 4
    [System.IO.File]::WriteAllText($summaryJson, $json, [System.Text.UTF8Encoding]::new($false))
    Write-Host "Flash gate deferred. Re-run with -ConfirmFlash to erase/write/verify target SPI flash."
    exit 0
}

$commands = @(
    @("-sdk", $SdkPath, "-type", "spi", "-chip", "DA14531", "-jtag", $JLinkSerial, "-cmd", "erase", "-firmware", $programmer, "-y"),
    @("-sdk", $SdkPath, "-type", "spi", "-chip", "DA14531", "-jtag", $JLinkSerial, "-cmd", "write", "-file", $FirmwareBin, "-bootable", "-verify", "-max", "0x20000", "-firmware", $programmer, "-y")
)

$allOutput = New-Object System.Collections.Generic.List[string]
$exitCodes = New-Object System.Collections.Generic.List[int]
foreach ($args in $commands) {
    $allOutput.Add("COMMAND: $ToolPath $($args -join ' ')")
    $output = & $ToolPath @args 2>&1
    $exitCodes.Add($LASTEXITCODE)
    foreach ($line in $output) {
        $allOutput.Add([string]$line)
    }
}
[System.IO.File]::WriteAllText($rawLog, ($allOutput -join [Environment]::NewLine), [System.Text.UTF8Encoding]::new($false))

$logText = [System.IO.File]::ReadAllText($rawLog)
$passed = ($exitCodes | Where-Object { $_ -ne 0 }).Count -eq 0 -and
    $logText -match "Memory burning completed successfully" -and
    $logText -match "SPI Flash memory verification succeeded"

if (!$passed) {
    throw "SmartSnippets flash did not produce the expected success and verify messages. See '$rawLog'."
}

$summary = [pscustomobject]@{
    gate = "smart-snippets-flash"
    status = "pass"
    tool_path = $ToolPath
    sdk_path = $SdkPath
    firmware_bin = $FirmwareBin
    firmware_sha256 = (Get-FileHash -LiteralPath $FirmwareBin -Algorithm SHA256).Hash.ToLowerInvariant()
    jlink_serial = $JLinkSerial
    raw_log = $rawLog
}
$json = $summary | ConvertTo-Json -Depth 4
[System.IO.File]::WriteAllText($summaryJson, $json, [System.Text.UTF8Encoding]::new($false))

Write-Host "SmartSnippets flash gate passed."
Write-Host "Summary: $summaryJson"
